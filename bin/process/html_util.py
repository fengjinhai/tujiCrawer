import re, htmlentitydefs
import chardet

ENCODINGS = ['utf-8', 'gb18030']

url_validation_regex = re.compile(r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

def is_valid_url(url):
    return url_validation_regex.match(url) is not None

##
# http://effbot.org/zone/re-sub.htm#unescape-html
# Removes HTML or XML character references and entities from a text string.
#
# @param text The HTML (or XML) source text.
# @return The plain text, as a Unicode string, if necessary.
def unescape(text):
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return re.sub("&#?\w+;", fixup, text)

def get_unicode_str(html):
    if isinstance(html, (unicode,)):
        return 'unicode', html
    elif isinstance(html, (str, )):
        for enc in ENCODINGS:
            try:
                html = html.decode(enc)
                return enc, html
            except:
                pass
        enc = chardet.detect(html)['encoding']
        try:
            html = html.decode(enc, 'ignore')
            return enc, html
        except:
            pass
    return '', html


