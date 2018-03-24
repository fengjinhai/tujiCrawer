#encoding:utf-8
import json
import re
import os
import sys
import re
import traceback
import html_util
from bs4 import BeautifulSoup
titleDic = {'uumnt.com':'', '17786.com':'', 'hiapk.com':'', 'cnmo.com':'', 'zol.com':''}
def pageNumExtractBak(html):
    encoding, html = html_util.get_unicode_str(html)
    for line in html.split('\n'):
        line = line.strip().encode('utf-8')
        if '下一页' in line:
            print line
            if '4.htm' in line:
                return 4
            elif '3.htm' in line:
                return 3
            elif '2.htm' in line:
                return 2
    return 0

titleFeature = ['center', 'pageheader', 'title']
pageFeature = ['page', 'pagebar', 'page_css', 'pageS', 'pages', 'lblPageCount', 'pagePg', 'page-bd', 'dede_pages', 'itempage', 'pagenavi', 'pageart','NewPages','content-page', 'fenye', 'totalpage', 'art_yema', 'x_page', 'show1', 'pageturning', 'efu-page', 'cpages', 'pnum']
def has_page_class(tag):
    return (tag.get('class') and tag.get('class')[0] in pageFeature) or (tag.get('id') and tag.get('id') in pageFeature)

def has_title_class(tag):
    return (tag.get('class') and tag.get('class')[0] in titleFeature) or (tag.get('id') and tag.get('id') in titleFeature)


def getFeatureHtml(html, feature):
    soup = BeautifulSoup(html, "html5lib")
    if feature == 'page':
        result = soup.find_all(has_page_class)
    if feature == 'title':
        result = soup.find_all(has_title_class)
    if len(result) != 0:
        return str(result[0]).replace("\n", "")
    return False

def pageNumExtractByTitle(html):
    pageNum = 0
    try:
        res = getFeatureHtml(html, 'title')
        print res
        pageData = re.findall('\d+/\d+', res)
        if len(pageData) > 0:
            pageNum = int(pageData[0].split('/')[-1])
        return pageNum 
    except:
        traceback.print_exc()
        pass
    return 0

def pageNumExtractByPage(html):
    maxNum = 0
    try:
        res = getFeatureHtml(html, 'page')
        if not res:
            return maxNum
        #pageData = re.findall('共\d+页', res)
        for pattern in ['>\.\.\.\d+<', '共\d+页', '\d+</i>', '>\d+<']:
            pageData = re.findall(pattern, res)
            if len(pageData) > 0:
                for item in pageData:
                    result = re.search('\d+', item)
                    if not result:
                        continue
                    num = int(result.group())
                    if num > maxNum:
                        maxNum =  num
                return maxNum
    except:
        traceback.print_exc()
        pass
    return 0

def pageNumExtract(html, domain=''):
    if titleDic.has_key(domain):
        ret = pageNumExtractByTitle(html)
    else:
        ret = pageNumExtractByPage(html)
    return ret

if __name__ == "__main__":
    html = open('./page.html').read()
    print pageNumExtract(html, 'zcool.com.cn')
