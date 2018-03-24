#coding=utf-8
import traceback
import json
import re
import MySQLdb
import sys
import time
import hashlib
sys.path.append("../lib")
from log import *
from myDb import *
from download import getPage
sys.path.append("../conf")
sys.path.append("./process")
#from original_url_renwu import webInfo 
import list_extract as le
import tupian_extract as tupian
import tuji_extract as tuji
import extract_pagenum as pe
from updateFile import crawerInfo 

class ClientPage():
    def tupianParse(self, info, urlSign, page, url, domain):
        encoding, picUrl, title, text, publishTime, mypos, pageNum = tupian.parse(url, page, info)
        if not publishTime or publishTime == '':
            x = time.localtime(time.time())
            publishTime = '0000-00-00 00:00:00'
        if not encoding:
            print "encoding None"
            return False
        text = text.replace('\r', '').replace('\n',' ').replace('\t','')
        sql  = "update tbl_content_2 set title = '%s', publishTime = '%s', status = 2, text = '%s', mypos = '%s', picUrl = '%s' where urlSign = '%s'"\
        %(MySQLdb.escape_string(title.encode('utf-8')), publishTime.encode('utf-8'), MySQLdb.escape_string(text.encode('utf-8')), MySQLdb.escape_string(mypos.encode('utf-8')), picUrl.encode('utf-8'), urlSign.encode('utf-8'))
        print sql
        doDB(sql, 'chuilei')
        return True


    def tujiParse2(self, info, urlSign, page, url, domain):
        encoding, picUrl, title, text, publishTime, mypos, pageNum = tupian.parse(url, page, info)
        images = [picUrl]
        if info.has_key('detailFenyePattern'):
            if pageNum > 1:
                for i in range(2, pageNum+1):
                    urlNew = url.replace(info['detailFenyePattern'][0], info['detailFenyePattern'][1]%i)
                    page = getPage(urlNew)
                    if not page:
                        retStatus = self.changeStatus(urlSign, 1)
                        print 'down url:%s failed'%urlNew
                        continue
                    fenyeEncoding, fenyePicUrl, fenyeTitle, fenyeText, fenyePublishTime, fenyeMypos, fenyePageNum = tupian.parse(url, page, info)
                    text = text + fenyeText
                    images.append(fenyePicUrl)
        if not publishTime:
            x = time.localtime(time.time())
            publishTime = '0000-00-00 00:00:00'
        text = text.replace('\r', '').replace('\n',' ').replace('\t','')
        picInfo = []
        if len(images) == 0:
            retStatus = self.changeStatus(urlSign, 1)
            print 'url:%s has no pic'%url
            return False
        for i in range(len(images)):
            picInfo.append({'picUrl':images[i], 'picDesc':'', 'pic_seq':i})
        imgJson = json.dumps(picInfo, ensure_ascii= False)
        sql  = "update tbl_content_2 set title = '%s', publishTime = '%s', status = 2, text = '%s', mypos = '%s', images = '%s' where urlSign = '%s'"\
        %(MySQLdb.escape_string(title.encode('utf-8')), publishTime.encode('utf-8'), MySQLdb.escape_string(text.encode('utf-8')), MySQLdb.escape_string(mypos.encode('utf-8')), imgJson.encode('utf-8'), urlSign.encode('utf-8'))
        print sql
        doDB(sql, 'chuilei')
        return True

    def tujiParse(self, info, urlSign, page, url, domain):
        encoding, title, text, publishTime, images, mypos = tuji.parse(url, page, info)
        if title == "" and images == "":
            retStatus = self.changeStatus(urlSign, 1)
            print 'parse url:%s parse failed'%url
            return False
            
        if info.has_key('detailFenyePattern'):
            pageNum = pe.pageNumExtract(page, domain)
            if pageNum > 1:
                for i in range(2, pageNum+1):
                    if info['detailFenyePattern'][0] == "":
                        urlNew = url + info['detailFenyePattern'][1]%i
                    else:
                        urlNew = url.replace(info['detailFenyePattern'][0], info['detailFenyePattern'][1]%i)
                    page = getPage(urlNew)
                    if not page:
                        retStatus = self.changeStatus(urlSign, 1)
                        print 'down url:%s failed'%urlNew
                        continue
                    fenyeEncoding, fenyeTitle, fenyeText, fenyePublishTime, fenyeImages, fenyeMypos = tuji.parse(url, page, info)
                    if fenyeTitle == "" and fenyeImages == "":
                        retStatus = self.changeStatus(urlSign, 1)
                        print 'parse url:%s parse failed'%url
                        continue
                    text = text + fenyeText
                    images = images + fenyeImages
        if not publishTime:
            x = time.localtime(time.time())
            publishTime = '0000-00-00 00:00:00'
        #if not encoding:
        #    print "encoding None"
        #    return False
        text = text.replace('\r', '').replace('\n',' ').replace('\t','')
        picInfo = []
        if len(images) == 0:
            retStatus = self.changeStatus(urlSign, 1)
            print 'url:%s has no pic'%url
            return False
        for i in range(len(images)):
            picInfo.append({'picUrl':images[i], 'picDesc':'', 'pic_seq':i})
        imgJson = json.dumps(picInfo, ensure_ascii= False)
        sql  = "update tbl_content_2 set title = '%s', publishTime = '%s', status = 2, text = '%s', mypos = '%s', images = '%s' where urlSign = '%s'"\
        %(MySQLdb.escape_string(title.encode('utf-8')), publishTime.encode('utf-8'), MySQLdb.escape_string(text.encode('utf-8')), MySQLdb.escape_string(mypos.encode('utf-8')), imgJson.encode('utf-8'), urlSign.encode('utf-8'))
        print sql
        doDB(sql, 'chuilei')
        return True

    def changeStatus(self, urlSign, status):
        sql  = "update tbl_content_2 set status = %d where urlSign = '%s'"%(status, urlSign)
        doDB(sql, 'chuilei')

    def run(self, domain, info):
        sql = "select urlSign, url, domain, isAlbum from tbl_content_2 where domain = '%s' \
        and status = 0 and category='%s';"%(domain, info['category'])
        res = getDB(sql, 'chuilei')
        for item in res:
            urlSign = item[0]
            url = item[1]
            print url
            domain = item[2]
            isAlbum = item[3]
            page = getPage(url)
            #page = page.decode('utf-8','ignore')
            if not page:
                retStatus = self.changeStatus(urlSign, 1)
                print 'down url:%s failed'%url
                continue
            if isAlbum == 0:
                ret = self.tupianParse(info, urlSign, page, url, domain)
                if not ret:
                    retStatus = self.changeStatus(urlSign, 1)
                    print 'parse url:%s failed'%url
                    continue
            elif isAlbum == 1:
                ret = self.tujiParse(info, urlSign, page, url, domain)
                if not ret:
                    retStatus = self.changeStatus(urlSign, 1)
                    print 'parse url:%s failed'%url
                    continue
            elif isAlbum == 2:
                ret = self.tujiParse2(info, urlSign, page, url, domain)
                if not ret:
                    retStatus = self.changeStatus(urlSign, 1)
                    print 'parse url:%s failed'%url
                    continue

if __name__ == "__main__":
    catgInfo = crawerInfo()
    clientPage = ClientPage()
    #clientPage.run(domain)
    for catg, webInfo in catgInfo.items(): 
        for domain, info in webInfo.items():
            clientPage.run(domain, info)
