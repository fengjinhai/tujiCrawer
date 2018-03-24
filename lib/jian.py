# -*- coding:utf-8 -*- 
from langconv import *


# 转换繁体到简体 
line = '為因應本院公共化政策並加速圖檔資料開放，特釋出300dpi約20Mb之文物圖像，民眾無需申請，不限用途，不用付費，可直接下載使用，相關規範均依「政府資料開放授權條款1.0版」辦理，歡迎各界多加利用。'
line = Converter('zh-hans').convert(line.decode('utf-8')) 
line = line.encode('utf-8') 
print line
# 转换简体到繁体 
#line = Converter('zh-hant').convert(line.decode('utf-8')) 
#line = line.encode('utf-8')
