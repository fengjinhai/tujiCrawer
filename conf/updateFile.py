#encoding:utf-8
import os
import json
import sys
sys.path.append('/home/img/tujiCrawer/conf/')
from original_url_artist import webInfo as artistInfo
from original_url_biaoqing import webInfo as biaoqingInfo
from original_url_dongman import webInfo as dongmanInfo
from original_url_dongwu import webInfo as dongwuInfo
from original_url_jiazhuang import webInfo as jiazhuangInfo
from original_url_meizhuang import webInfo as meizhuangInfo
from original_url_renwu import webInfo as renwuInfo
from original_url_sucai import webInfo as sucaiInfo
from original_url_yule import webInfo as yuleInfo
from original_url_zhiwu import webInfo as zhiwuInfo


preFix = '/home/img/tujiCrawer/conf/'
def getNotAllowDomain():
    notUpdate = {
        '7kk.com':'经常挂',
        'warting.com':'访问速度太慢',
        'bz.putaojiayuan.com':'经常挂',
        'doutula.com':'经常挂',
        'sootuu.com':'经常挂',
        'plant.cila.cn':'容易封禁',
        'huabaike.com':'编码',
        'pp.163.com':'js',
        'guandongphoto.com':'',
        'search.quanjing.com':'js',
        }
    f = open('%snotAllowDomain.txt'%preFix)
    datalines = f.readlines()
    f.close()
    notAllowDomain = {}
    for line in datalines: 
        notAllowDomain[line.strip()] = ''
    notAllow = dict(notUpdate.items()+notAllowDomain.items())
    return notAllow

def crawerInfo():
    notAllow = getNotAllowDomain()
    dayCrawer = {}
    allCrawer = {
        'artist': artistInfo,
        'biaoqing': biaoqingInfo,
        'dongman': dongmanInfo,
        'dongwu':dongwuInfo,
        'jiazhuang':jiazhuangInfo,
        'meizhuang':meizhuangInfo,
        'renwu':renwuInfo,
        'sucai':sucaiInfo,
        'yule':yuleInfo,
        'zhiwu':zhiwuInfo,
    }
    for catg, info in allCrawer.items():
        for domain, domainInfo in info.items():
            if notAllow.has_key(domain):
                continue
            if dayCrawer.has_key(catg):
                dayCrawer[catg][domain] = domainInfo
            else:
                dayCrawer[catg] = {domain:domainInfo}
    return dayCrawer
