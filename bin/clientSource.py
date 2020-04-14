#coding=utf-8
import traceback
import json
import re
import sys
import time
import urllib
import hashlib
sys.path.append("../lib")
from log import *
from myDb import *
from download import ScrapyClient 
sys.path.append("../conf")
sys.path.append("./process")
import list_extract as le
#import tupian_extract as tupian
#import tuji_extract as tuji
import extract_pagenum as pe
#from updateFile import crawerInfo 
from original_url import webInfo 

class ClientSource():
    def getFenye(self, info, history = False):
        fenyeUrlList = []
        if history:
            for sourceUrl, pageNum in info['sourceUrl'].items():
                if pageNum == 1:
                    fenyeUrlList.append(sourceUrl)
                else:
                    fenyeUrlList.append(sourceUrl)
                    for i in range(1, pageNum):
                        if info['fenyePattern'][0] == "":
                            fenye = sourceUrl + info['fenyePattern'][1]
                        else:
                            fenye = sourceUrl.replace(info['fenyePattern'][0], info['fenyePattern'][1])
                        fenyeUrlList.append(fenye%i)
        else:
            fenyeUrlList = info['sourceUrl'].keys()
        return fenyeUrlList 

    def parse(self, url, page, urlPattern):
        detailUrlSet = set()
        try:
            links = le.parse(url, page)
            for anchor, link in links:
                dataPattern = re.search(urlPattern, link)
                if not dataPattern:
                    continue
                detailUrlSet.add(link)
        except:
            traceback.print_exc()
            print('parse url error : %s'%url)
        return detailUrlSet

    def getSourceUrl(self, url, page, urlPattern):
        sourceUrlDic =  {}
        try:
            encoding, links = le.parse(url, page)
            if not encoding: return False
            for anchor, link in links:
                dataPattern = re.search(urlPattern, link)
                if not dataPattern:
                    continue
                sourceUrlDic[link] = ''
        except:
            traceback.print_exc()
            print('parse url error : %s'%url)
        return sourceUrlDic 

    def process(self, fenyeUrl, detailUrlSet, info): 
        domain = info['domain'] 
        category = info['category']
        isAlbum = info['isAlbum']
        for link in detailUrlSet:
            if 'urlReplace' in info:
                link = link.replace(info['urlReplace'][0][0], info['urlReplace'][0][1])
            self.rukuSourceLink(link, fenyeUrl, category, domain, isAlbum)
        return True

    def getDetailUrl(self, fenyeUrl, info): 
        page = scrapyClient.getPage(fenyeUrl)
        detailUrlSet = self.parse(fenyeUrl, page, info['urlPattern'])
        if len(detailUrlSet) == 0:
            print ('url:%s can not get detail page url'%fenyeUrl)
        self.process(fenyeUrl, detailUrlSet, info)
        return True

    def getSourceFy(self, sourceUrl, info): 
        fyList = []
        page = scrapyClient.getPage(sourceUrl)
        if not page:
            return fyList
        pageNum = pe.pageNumExtract(page, info['domain'])
        fyList.append(sourceUrl)
        if pageNum > 1:
            for i in range(1, pageNum+1):
                if info['sourceFenyePattern'][0] == "":
                    urlNew = sourceUrl + info['sourceFenyePattern'][1]%i
                else:
                    urlNew = sourceUrl.replace(info['sourceFenyePattern'][0], info['sourceFenyePattern'][1]%i)
                fyList.append(urlNew)
        return fyList

    def checkExitUrl(self, _id):
        sql = "select count(1) from tbl_content where urlSign='%s'"%_id
        ret = getDB(sql, 'tuji')
        return ret[0][0]

    def rukuSourceLink(self, link, url, category, domain, isAlbum):
        _id = hashlib.md5(link.encode()).hexdigest()[:24]
        if self.checkExitUrl(_id):
            print("sourceUrl: %s exist"%url)
            return True
        x = time.localtime(time.time())
        nowTime = time.strftime('%Y-%m-%d %H:%M:%S',x)
        rukuDic = {
                'urlSign': _id, 
                'url': link, 
                'sourceUrl': url, 
                'domain': domain, 
                'isAlbum': isAlbum, 
                'category': category,
                'images':'',
                'text':'',
                'crawlTime': nowTime,
                'status': 0,
                }
        print ('ruku:%s'%json.dumps(rukuDic, ensure_ascii=False))
        try:
            writeDB('tbl_content', rukuDic)
        except Exception as e:
            logger.error(e)

    def run(self, domain, info, history = 0): 
        fenyeUrlList = self.getFenye(info, history)
        for fenyeUrl in fenyeUrlList:
            self.getDetailUrl(fenyeUrl, info)
        return True

if __name__ == "__main__":
    scrapyClient = ScrapyClient()
    clientSource = ClientSource()
    for domain, info in webInfo.items():
        clientSource.run(domain, info, 1)
