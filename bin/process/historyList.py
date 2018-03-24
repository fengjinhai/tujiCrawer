#encoding=utf-8
import time
import sys
import re
import datetime
sys.path.append("../lib")
from download import getPage
from clientSource import *

webInfo ={
        'category':'美图', 
        'sourceName':'中关村在线', 
        'domain':'zol.com', 
        'sourceUrl':'http://sj.zol.com.cn/bizhi/',
        'urlPattern':'http.*/bizhi/.*\.html',
    }




client = Client()
for i in range(2, 430):
    url = "http://www.5857.com/list-11-0-0-0-0-0-%d.html"%i
    print url
    page = getPage(url)
    if not page:
        print 'down url:%s failed'%url
        continue
    client.parse(page, webInfo['sourceUrl'], webInfo['category'],  webInfo['sourceName'], webInfo['domain'], webInfo['urlPattern'])

#page = open('./page').read()
#client = Client()
#client.parse(page, webInfo['sourceUrl'], webInfo['category'],  webInfo['sourceName'], webInfo['domain'], webInfo['urlPattern'])
