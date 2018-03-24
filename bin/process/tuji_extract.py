#coding=utf-8
from __future__ import division
import traceback
import chardet
import re
import json
import sys
import hashlib
import dateutil.parser as dtparser
import lxml
import lxml.html
import lxml.etree
import html_util
from bs4 import BeautifulSoup
sys.path.append("../../lib")
from download import getPage
sys.path.append("../../conf")
RE_MULTI_NEWLINE = ur'\n+'

RE_IGNORE_BLOCK = {
'doctype' : ur'(?is)<!DOCTYPE.*?>', # html doctype
'comment' : ur'(?is)<!--.*?-->', # html comment
'script' : ur'(?is)<script.*?>.*?</script>', # javascript
'style' : ur'(?is)<style.*?>.*?</style>', # css
#'special' : ur'&.{2,5};|&#.{2,5};',
}

RE_NEWLINE_BLOCK = {
'div' : ur'(?is)<div.*?>',
'p' : ur'(?is)<p.*?>',
'a' : ur'(?is)<a.*?>',
'br' : ur'(?is)<br.*?>',
'hr' : ur'(?is)<hr.*?>',
'h' : ur'(?is)<h\d+.*?>',
'li' : ur'(?is)<li\d+.*?>',
}

RE_IMG = ur'(?is)(<img.*?>)'

RE_IMG_SRC = ur'(?is)<img.+?src=(\'|")(.+?)(\'|").*?>'
RE_TAG = ur'(?is)<.*?>'

RE_TITLE = ur'(?is)<title.*?>(.+?)</title>'
RE_H = ur'(?is)<h\d+.*?>(.*?)</h\d+>'

RE_TIME = (ur'(?is)((?:0?|[12])\d\s*:+\s*[0-5]\d'
           ur'(?:\s*:+\s*[0-5]\d)?(?:\s*[,:.]*\s*(?:am|pm))?)')

RE_MONTH = ur'(?:(?:jan|feb|mar|apr|may|jun|aug|sep|oct|nov|dec)[a-z]*)'
RE_DATETIME = (ur'(?is)((?:' + RE_MONTH +
               ur'[.,\-\s]*\d{1,2}[.,\-\s]*(\d{4}))|(?:\d{1-2}[.,\-\s]*' + RE_MONTH +
               ur'[.,\-\s]*(\d{4}))|(?:(\d{4}-)\d{1,2}-\d{1,2})|'
               ur'(?:(\d{4}年){0,1}\d{1,2}月\d{1,2}日))')

## parameters
BLOCKS_WIDTH = 3
THRESHOLD = 200

## 导航条特征
NAV_SPLITERS = [
    ur'\|',
    ur'┊',
    # 外文空格较多，需要空格计算每行字符数
    #ur'\s+',
]

#尾部特征
       
def strtotime(date, time):
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

def has_class(html, htmlAttr):
    classFeature = []
    idFeature = []

    if htmlAttr.has_key('id'):
        idFeature = htmlAttr['id']
    if htmlAttr.has_key('class'):
        classFeature = htmlAttr['class']
    def x(tag):
        if tag.get('class'):
            for classItem in tag.get('class'):
                if classItem in classFeature:
                    return classItem in classFeature
        if tag.get('id'):
            return tag.get('id') in idFeature
    return x


def lineProcess(item):
    for k,v in RE_IGNORE_BLOCK.iteritems():
        item = re.sub(v, '', str(item))
    text = re.sub(RE_TAG, '', str(item))
    text = text.replace('\n','').replace(';','').replace('    ', '').replace('\r', '')
    text = text.replace('&gt','').replace('nbsp','').replace('&amp','')
    return text

def getDataByXpath(doc, Xpath):
    if Xpath == '':
        return ''
    items = doc.xpath(Xpath)
    retStr = ' '.join(items)
    text = lineProcess(retStr.encode('utf-8'))
    return unicode(text, "utf-8")

#return (tag.get('class') and tag.get('class')[0] in classFeature) or (tag.get('id') and tag.get('id') in idFeature)

def getText(html, pattern):
    soup = BeautifulSoup(html, "lxml")
    result = soup.find_all(has_class(html, pattern))
    if len(result) != 0:
        res = []
        for item in result:
            text = lineProcess(item)
            res.append(text)
        return unicode(' '.join(res), "utf-8")
    return u""


def getBody(html, htmlAttr):
    soup = BeautifulSoup(html, "lxml")
    result = soup.find_all(has_class(html, htmlAttr))
    if len(result) != 0:
        res = []
        for item in result:
            for line in str(item).split('\n'):
                if '相关新闻' in line or '喜欢就赞一下吧' in line or '相关推荐' in line:
                    break
                res.append(str(line))
        return unicode("\n".join(res), "utf-8")
    return u""

def checkSpecialImg(item, imgUrlPattern):
    for term in item.split(' '):
        res = re.search(imgUrlPattern, term)
        if res:
            if 'big' in term or 'onclick' in term:
                return True
    return False

def HtmlTagStrip(html, webInfo):
    images = []
    for item in re.findall(webInfo['imgPattern'], html):
        if not item:
            continue
        #print item.encode('utf-8')
        #print webInfo['imgUrlPattern']
        if checkSpecialImg(item, webInfo['imgUrlPattern']):
            for term in item.split(' '):
                res = re.search(webInfo['imgUrlPattern'], term)
                if res:
                    img = (res.group())
                    if 'big' in term or 'onclick' in term:
                        images.append(img)
        else:
            #print webInfo['imgUrlPattern']
            res = re.search(webInfo['imgUrlPattern'], item)
            #print res
            if res:
                img = (res.group())
                images.append(img)
            
    for k,v in RE_IGNORE_BLOCK.iteritems():
        html = re.sub(v, '', html)
    for k,v in RE_NEWLINE_BLOCK.iteritems():
        html = re.sub(v, '\n', html)
    html = re.sub(RE_MULTI_NEWLINE, '\n', html)
    html = re.sub(RE_TAG, '', html)
    lines = []
    for line in html.split('\n'):
        if len(line) == 0:
            continue
        else:
            lines.append(line.strip())
    html = '\n'.join(lines)
    return images, html 

def get_main_content(html, bodyHtml, webInfo):
    if not isinstance(html, unicode):return '', '', '', {}
    title = ''.join(re.findall(RE_TITLE, html)).strip()# + re.findall(RE_H, html)
    html = re.sub(ur"(?is)</a><a",'</a> <a',html)
    h = re.findall(RE_H, html)
    for ht in h:
        ht = ht.strip()
        if ht == '': continue
        if title.startswith(ht):
            title = ht
            break
    title = html_util.unescape(title)
    text = re.sub(RE_TAG, '', html)
    # 抽取发表时间
    time = ''
    t_time = re.findall(RE_TIME, text)
    if len(t_time) > 0:
        time = t_time[0]
    date = ''
    t_date = re.findall(RE_DATETIME, text)
    if len(t_date) > 0:
        date = t_date[0][0]
    images, text = HtmlTagStrip(bodyHtml, webInfo)       
    return title, strtotime(date, time), text, images


def parse(url, html,  webInfo):
    encoding, html = html_util.get_unicode_str(html)
    if 'ISO' in encoding:
        return '', '', '', '','',''
    if encoding == '': return '', '', '', '','',''
    newHtml = ''
    imgList = []
    for x in html.split('\n'):
        if x.count('<img') > 1:
            x = x.replace(u'<img', u'\n<img')
        newHtml = newHtml + "\n"  + x
    html = newHtml
    try:
        doc = lxml.html.document_fromstring(html)
        doc.make_links_absolute(url)
        html = lxml.etree.tounicode(doc, method='html')
    except:
        traceback.print_exc()
        pass
    newHtml = getBody(html, webInfo['bodyPattern'])
    if newHtml == "":
        return '','','','','','' 
    title, time, text, images = get_main_content(html, newHtml, webInfo)
    mypos = ''
    if webInfo.has_key('textPattern'):
        text = getText(html, webInfo['textPattern'])
    if webInfo.has_key('titlePattern'):
        title = getText(html, webInfo['titlePattern'])
    if webInfo.has_key('myposPattern'):
        mypos = getText(html, webInfo['myposPattern'])
    if webInfo.has_key('textXpath'):
        text = getDataByXpath(doc, webInfo['textXpath'])
    if webInfo.has_key('titleXpath'):
        title = getDataByXpath(doc, webInfo['titleXpath'])
    if webInfo.has_key('myposXpath'):
        mypos = getDataByXpath(doc, webInfo['myposXpath'])
    if webInfo.has_key('publishTimeXpath'):
        time = getDataByXpath(doc, webInfo['publishTimeXpath'])
        time = strtotime(time, '')

    if webInfo.has_key('imgReplace'):
        patternList = webInfo['imgReplace']
        for picUrl in images:
            for pattern in patternList:
                picUrl = picUrl.replace(pattern[0], pattern[1])
            imgList.append(picUrl)
    else:
        imgList = images
    #print time.encode('utf-8')
    #print text.encode('utf-8')
    return encoding, title, text, time, imgList, mypos

if __name__ == "__main__":
    from original_url_sucai import webInfo
    #html = open('page.html').read()
    #enc, title, text, time, images, mypos = parse('http://www.guandongphoto.com/thread-1035924-1-11.html',html, webInfo['guandongphoto.com'])
    url = sys.argv[1]
    domain = sys.argv[2]
    html = getPage(url)
    enc, title, text, time, images, mypos = parse(url,html, webInfo[domain])
    print "标题："+title.encode('utf-8','ignore')
    print "mypos："+mypos.encode('utf-8','ignore')
    print "时间："+time.encode('utf-8','ignore')
    print "内容：\n"+text.encode('utf-8','ignore')
    print '='*10
    print '图片:'
    print images
