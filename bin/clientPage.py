#coding=utf-8
import datetime
import traceback
import json
import re
import pymysql
import sys
import time
import hashlib
sys.path.append("../lib")
from log import *
from myDb import *
from download import ScrapyClient 
sys.path.append("../conf")
sys.path.append("./process")
from original_url import webInfo 
#import tupian_extract as tupian
import tuji_extract as tuji
import extract_pagenum as pe

class ClientPage():
    def tupianParse(self, info, urlSign, page, url, domain):
        encoding, picUrl, title, text, publishTime, mypos, pageNum = tupian.parse(url, page, info)
        if not publishTime or publishTime == '' or publishTime < '2000':
            x = time.localtime(time.time())
            publishTime = ''
        if not encoding:
            print ("encoding None")
            return False
        text = text.replace('\r', '').replace('\n',' ').replace('\t','')
        sql  = "update tbl_content set title = '%s', publishTime = '%s', status = 2, text = '%s', mypos = '%s', picUrl = '%s' where urlSign = '%s'"\
        %(pymysql.escape_string(title.encode('utf-8')), publishTime.encode('utf-8'), pymysql.escape_string(text.encode('utf-8')), pymysql.escape_string(mypos.encode('utf-8')), picUrl.encode('utf-8'), urlSign.encode('utf-8'))
        print (sql)
        doDB(sql, 'tuji')
        return True

    def checkExitUrl(self, _id):
        sql = "select count(1) from tbl_content where urlSign='%s' and status != 0"%_id
        ret = getDB(sql, 'tuji')
        return ret[0][0]

    def tujiParse(self, info, urlSign, page, url, domain):
        textSet = set()
        title, text, publishTime, images, mypos = tuji.parse(url, page, info)
        textSet.add(text)
        #if self.checkExitUrl(_id):
        #    print("pageUrl: %s exist"%url)
        #    return True
        if title == "" and images == "":
            retStatus = self.changeStatus(urlSign, 1)
            print ('parse url:%s parse failed'%url)
            return False
        if 'detailFenyePattern' in info:
            pageNum = pe.pageNumExtract(page, domain)
            if pageNum > 1:
                for i in range(2, pageNum+1):
                    if info['detailFenyePattern'][0] == "":
                        urlNew = url + info['detailFenyePattern'][1]%i
                    else:
                        urlNew = url.replace(info['detailFenyePattern'][0], info['detailFenyePattern'][1]%i)
                    print(urlNew)
                    page = scrapyClient.getPage(urlNew)
                    if not page:
                        retStatus = self.changeStatus(urlSign, 1)
                        print ('down url:%s failed'%urlNew)
                        continue
                    fenyeTitle, fenyeText, fenyePublishTime, fenyeImages, fenyeMypos = tuji.parse(url, page, info)
                    if fenyeTitle == "" and fenyeImages == "":
                        retStatus = self.changeStatus(urlSign, 1)
                        print ('parse url:%s parse failed'%url)
                        continue
                    textSet.add(fenyeText)
                    images = images + fenyeImages
        if not publishTime or publishTime < '2000':
            publishTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #if not encoding:
        #    print "encoding None"
        #    return False
        text = "".join(textSet)
        text = text.replace('\r', '').replace('\n',' ').replace('标签：','')
        picInfo = []
        if len(images) == 0:
            retStatus = self.changeStatus(urlSign, 1)
            print ('url:%s has no pic'%url)
            return False
        for i in range(len(images)):
            picInfo.append({'picUrl':images[i], 'picDesc':'', 'pic_seq':i})
        imgJson = json.dumps(picInfo, ensure_ascii= False)
        sql  = "update tbl_content set title = '%s', publishTime = '%s', status = 2, text = '%s', mypos = '%s', images = '%s' where urlSign = '%s'"\
        %(pymysql.escape_string(title), publishTime, pymysql.escape_string(text), pymysql.escape_string(mypos), imgJson, urlSign)
        print (sql)
        doDB(sql, 'tuji')
        return True

    def changeStatus(self, urlSign, status):
        sql  = "update tbl_content set status = %d where urlSign = '%s'"%(status, urlSign)
        doDB(sql, 'tuji')

    def run(self, domain, info):
        sql = "select urlSign, url, domain, isAlbum from tbl_content where domain = '%s' \
        and status = 0 and category='%s';"%(domain, info['category'])
        res = getDB(sql, 'tuji')
        for item in res:
            urlSign = item[0]
            url = item[1]
            print (url)
            domain = item[2]
            isAlbum = item[3]
            page = scrapyClient.getPage(url)
            if not page:
                retStatus = self.changeStatus(urlSign, 1)
                print ('down url:%s failed'%url)
                continue
            if isAlbum == 0:
                ret = self.tupianParse(info, urlSign, page, url, domain)
                if not ret:
                    retStatus = self.changeStatus(urlSign, 1)
                    print ('parse url:%s failed'%url)
                    continue
            elif isAlbum == 1:
                ret = self.tujiParse(info, urlSign, page, url, domain)
                if not ret:
                    retStatus = self.changeStatus(urlSign, 1)
                    print ('parse url:%s failed'%url)
                    continue
            elif isAlbum == 2:
                ret = self.tujiParse2(info, urlSign, page, url, domain)
                if not ret:
                    retStatus = self.changeStatus(urlSign, 1)
                    print ('parse url:%s failed'%url)
                    continue

if __name__ == "__main__":
    scrapyClient = ScrapyClient()
    clientPage = ClientPage()
    for domain, info in webInfo.items():
        clientPage.run(domain, info)
