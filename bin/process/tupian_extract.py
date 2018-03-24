#coding=utf-8
from __future__ import division
import traceback
import re
import json
import sys
import hashlib
import dateutil.parser as dtparser
import lxml
import lxml.html
import lxml.etree
import html_util
sys.path.append("../../lib")
from download import getPage
sys.path.append("../../conf")
       
RE_TIME = (ur'(?is)((?:0?|[12])\d\s*:+\s*[0-5]\d'
           ur'(?:\s*:+\s*[0-5]\d)?(?:\s*[,:.]*\s*(?:am|pm))?)')

RE_MONTH = ur'(?:(?:jan|feb|mar|apr|may|jun|aug|sep|oct|nov|dec)[a-z]*)'
RE_DATETIME = (ur'(?is)((?:' + RE_MONTH +
               ur'[.,\-\s]*\d{1,2}[.,\-\s]*(\d{4}))|(?:\d{1-2}[.,\-\s]*' + RE_MONTH +
               ur'[.,\-\s]*(\d{4}))|(?:(\d{4}-)\d{1,2}-\d{1,2})|'
               ur'(?:(\d{4}年){0,1}\d{1,2}月\d{1,2}日))')

def strtotime(publish_time):
    # 抽取发表时间
    time = ''
    t_time = re.findall(RE_TIME, publish_time)
    if len(t_time) > 0:
        time = t_time[0]
    date = ''
    t_date = re.findall(RE_DATETIME, publish_time)
    if len(t_date) > 0:
        date = t_date[0][0]
    if not date: return ''
    if date:
        RE_DT_REPLACE = ur'年|月'
        date = re.sub(RE_DT_REPLACE,'-', date).replace(u'日', ' ')
        date = re.sub(ur'[,.\-\s]+', ' ', date)
        date = re.sub(ur'\s+', ' ', date)
    if time:
        time = re.sub(ur'\s+', '', time)
        time = re.sub(ur':+', ':', time)
    t = '%s, %s' % (date, time) if date else time
    try:
        s = str(dtparser.parse(t, fuzzy=True))
    except:
        s = ''
    return s

def getDataByXpath(doc, Xpath, isPos = 0):
    if Xpath == '':
        return ''
    items = doc.xpath(Xpath)
    if isPos:
        retStr = ' '.join(items)
        return retStr.strip()
    if len(items)>0:
        return ''.join(items).strip()
    return ''

def getPageNum(doc, webInfo):
    maxNum = 1
    if not webInfo.has_key('detailFyXpath'):
        return maxNum 
    if webInfo.has_key('detailFyXpath') == '':
        return maxNum
    res = getDataByXpath(doc, webInfo['detailFyXpath'])
    for pattern in ['>\.\.\.\d+<', '共\d+页', '\d+</i>', '>\d+<', '/\d+']:
        pageData = re.findall(pattern, res.encode('utf-8'))
        if len(pageData) > 0:
            for item in pageData:
                result = re.search('\d+', item)
                if not result:
                    continue
                num = int(result.group())
                if num > maxNum:
                    maxNum =  num
    return maxNum

def parse(url, html, webInfo):
    encoding, html = html_util.get_unicode_str(html)
    if encoding == '': return '', '', '', '', '', ''
    try:
        doc = lxml.html.document_fromstring(html)
        doc.make_links_absolute(url)
        page = lxml.etree.tounicode(doc, method='html')
    except:
        traceback.print_exc()
        pass
    picUrl = getDataByXpath(doc, webInfo['imgXpath'])
    title = getDataByXpath(doc, webInfo['titleXpath'])
    text = getDataByXpath(doc, webInfo['contentXpath'], 1)
    publishTime = getDataByXpath(doc, webInfo['timeXpath'])
    mypos = getDataByXpath(doc, webInfo['myposXpath'], 1)
    publishTime = strtotime(publishTime)
    detailFy = getPageNum(doc, webInfo)
    '''
    print "标题：" + title.encode('utf-8','ignore')
    print "时间：" + publishTime.encode('utf-8','ignore')
    print "内容：" + text.encode('utf-8','ignore')
    print "图片：" + picUrl.encode('utf-8','ignore')
    print "导航：" + mypos.encode('utf-8','ignore')
    '''
    return encoding, picUrl, title, text, publishTime, mypos, detailFy

if __name__ == "__main__":
    from original_url import webInfo 
    #html = open('page.html').read()
    #encoding, picUrl, title, text, publishTime, mypos, detailFy = parse('http://www.quanjing.com/imgbuy/ul0347-4320.html',html, webInfo['quanjing.com'])
    url = sys.argv[1]
    domain = sys.argv[2]
    html = getPage(url)
    encoding, picUrl, title, text, publishTime, mypos, detailFy = parse(url, html, webInfo[domain])
    print "标题：" + title.encode('utf-8','ignore')
    print "时间：" + publishTime.encode('utf-8','ignore')
    print "内容：" + text.encode('utf-8','ignore')
    print "图片：" + picUrl.encode('utf-8','ignore')
    print "导航：" + mypos.encode('utf-8','ignore')
    print "分页：" + str(detailFy)
