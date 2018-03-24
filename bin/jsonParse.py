#coding=utf-8
import sys
import traceback
import json
import re
sys.path.append("../lib")
from download import getPage
sys.path.append("../conf")
from original_url import webInfo 
from clientSource import ClientSource 


def getJsonData(url):
    retDtaJson = getPage(url)
    retDataDic = json.loads(retDtaJson)
    return retDataDic

def Parse(data):
    retList = []
    for item in data:
        retList.append(item['url'])
    return retList

if __name__ == "__main__":
    clientSource = ClientSource()
    info = webInfo['tuchong.com']
    sourceDic = info['sourceUrl']
    domain = info['domain'] 
    category = info['category']
    isAlbum = info['isAlbum']
    for sourceUrl, pageNum in sourceDic.items():
        for i in range(1, pageNum+1):
            if i == 1:
                fenyeUrl = sourceUrl
            else:
                fenyeUrl = sourceUrl.replace(info['fenyePattern'][0], info['fenyePattern'][1]%i)
            dataDic = getJsonData(fenyeUrl)
            urlList = Parse(dataDic['postList'])
            for link in urlList:
                clientSource.rukuSourceLink(link, fenyeUrl, category, domain, isAlbum)
     
