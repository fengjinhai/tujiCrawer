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
from original_url import webInfo 
import list_extract as le
import tupian_extract as tupian
import tuji_extract as tuji
import extract_pagenum as pe

class ClientSource():
    def parse(self, url, page, urlPattern):
        detailUrlList = []
        encoding, links = le.parse(url, page)
        if not encoding: return False
        for anchor, link in links:
            dataPattern = re.search(urlPattern, link)
            if not dataPattern:
                continue
            detailUrlList.append(link)
        return detailUrlList

    def run(self): 
        info = {
            'category':'植物', 
            'domain':'deskbz.com', 
            'sourceUrl':'http://www.deskbz.com/zhiwu/',
            'urlPattern':'http://www.deskbz.com/zhiwu/\d+.html',
            'bodyPattern':{"tag":"div", "class":["picturebox"]},
            'imgPattern':ur'(?is)(<img.*?>)',
            'imgUrlPattern':ur'http.*.(jpg|jpeg|png)',
            'isAlbum':1
        }
        domain = info['domain'] 
        category = info['category']
        urlPattern = info['urlPattern']
        isAlbum = info['isAlbum']
        page = open('./page.html').read()
        detailUrlList = self.parse(info['sourceUrl'], page, urlPattern)
        if not detailUrlList:
            print 'url:%s can not get detail page url'%fenyeUrl
            return False
        for link in detailUrlList:
            self.rukuSourceLink(link, info['sourceUrl'], category, domain, isAlbum)

    def checkExitUrl(self, _id):
        sql = "select count(1) from tbl_content where urlSign='%s'"%_id
        ret = getDB(sql, 'tujiCrawer')
        return ret[0][0]

    def rukuSourceLink(self, link, url, category, domain, isAlbum):
        if isinstance(link, unicode): link = link.encode('utf-8', 'ignore')
        if isinstance(url, unicode): url = url.encode('utf-8', 'ignore')
        _id = hashlib.md5(link).hexdigest()[:24]
        #if self.checkExitUrl(_id): return True
        x = time.localtime(time.time())
        nowTime = time.strftime('%Y-%m-%d %H:%M:%S',x)
        rukuDic = {
                'urlSign': _id, 
                'url': link, 
                'sourceUrl': url, 
                'domain': domain, 
                'isAlbum': isAlbum, 
                'category': category,
                'crawlTime': nowTime,
                'status': 0,
                }
        try:
            writeDB('tbl_content', rukuDic)
        except Exception, e:
            logger.error(e)

if __name__ == "__main__":
    clientSource = ClientSource()
    clientSource.run()
