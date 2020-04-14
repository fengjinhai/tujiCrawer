#coding=utf-8
import traceback
import json
import os
import re
import sys
import time
sys.path.append("../lib")
from log import *
from myDb import *
from download import ScrapyClient 
sys.path.append("../conf")

class DownAlbum():
    def mkdir(self, path):
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path) 

    def downLoadImages(self, urlSign, url, filename, imagesList):
        picNum = len(imagesList)
        succNum = 0
        for imgUrl in imagesList:
            self.mkdir("./source/%s"%filename)
            imgName = "./source/%s/%s.jpg"%(filename, imgUrl['pic_seq'])
            imgData = scrapyClient.getImage(imgUrl['picUrl'])
            if not imgData:
                print ('Failed: download image urlSign: %s, url:%s, imageUrl: %s'%(urlSign, url, imgUrl))
                continue
            succNum += 1
            f = open(imgName, 'wb')
            f.write(imgData)
            f.close()
            print ('Successful: download image urlSign: %s, url:%s, imageUrl: %s'%(urlSign, url, imgUrl))
        if picNum - succNum < 5:
            return True
        return False

    def addTag(self, urlSign, tagStr, author):
        tagList = tagStr.split(" ")
        for tag in tagList:
            rukuDic = {
                    'urlSign': urlSign,
                    'tag': tag,
                    'author': author
                    }
            try:
                writeDB('tag_content', rukuDic)
            except Exception as e:
                logger.error(e)

    def changeStatus(self, urlSign, status):
        sql  = "update tbl_content set status = %d where urlSign = '%s'"%(status, urlSign)
        doDB(sql, 'tuji')

    def run(self):
        sql = "select urlSign, url, sourceUrl, images, text from tbl_content where status = 2"
        res = getDB(sql, 'tuji')
        for item in res:
            urlSign = item[0]
            url = item[1]
            sourceUrl = item[2]
            images = item[3]
            imagesList = json.loads(images)
            author = int(sourceUrl.split("/")[-2])
            filename = "%d_%s"%(author, url.split("/")[-2])
            status = self.downLoadImages(urlSign, url, filename, imagesList)
            if status:
                self.changeStatus(urlSign, 3)
                self.addTag(urlSign, item[4], author)
            else:
                retStatus = self.changeStatus(urlSign, 4)
                print ('Failed: download album urlSign: %s, url:%s'%(urlSign, url))

if __name__ == "__main__":
    scrapyClient = ScrapyClient()
    downAlbum = DownAlbum()
    downAlbum.run()
