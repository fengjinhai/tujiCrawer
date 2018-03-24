#coding=utf-8
import re
import lxml
import lxml.etree
import lxml.html
import html_util
import text_util

MIN_ANCHOR_LEN = 3 

EXCLUDED_URL_PATTERN = ur'.+http://|'\
        ur'http://www.sogou.com/.*|'\
        ur'http://clk.optaim.com/.*|'\
        ur'http://www.bing.com/.*|'\
        ur'.*ad-plus.cn.*'

EXCLUDED_ANCHOR_PATTERN = ur'\|$|'\
        ur'┊$'


def is_useful_link(anchor, urls):
    anchor = anchor.strip()
    #if anchor =='': return False
    if len(urls) == 0: return False
    if not html_util.is_valid_url(urls[0]): return False
    #if text_util.get_cn_num(anchor) < MIN_ANCHOR_LEN: return False
    if re.findall(EXCLUDED_ANCHOR_PATTERN, anchor): return False
    if re.findall(EXCLUDED_URL_PATTERN, urls[0]): return False
    return True

def parse(url, html):
    encoding, html = html_util.get_unicode_str(html)
    if encoding == '': return '',[]
    doc = lxml.html.document_fromstring(html)
    doc.make_links_absolute(url)
    links = [(lxml.etree.tounicode(node,method='text'), node.xpath('@href'))\
            for node in doc.xpath('//a')]
    links = [(re.sub(ur'\s+',' ',x), y[0].strip()) for x, y in links if is_useful_link(x, y)]
    return encoding,links

if __name__ == "__main__":
    url = 'http://www.gexing.com/'
    html = open('page1.html').read()
    encoding, links = parse(url, html)
    for x,y in links:
        print x.encode('utf-8'),y.encode('utf-8')
