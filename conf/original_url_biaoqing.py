#encoding:utf-8
webInfo = {
    'chinaz.com':{
        'category':'表情', 
        'domain':'chinaz.com', 
        'sourceUrl':{'http://sc.chinaz.com/biaoqing/index.html':464},
        'urlPattern':'http://sc.chinaz.com/biaoqing/\d+.htm',
        'fenyePattern':['.html', '_%d.html'],
        'bodyPattern':{"tag":"div", "class":["down_img"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'isAlbum':1
    },
    'ghost64.com':{
        'category':'表情', 
        'domain':'ghost64.com', 
        'sourceUrl':{
                'http://www.ghost64.com/qqbiaoqing/dongwubiaoqing_1.html':62,
                'http://www.ghost64.com/qqbiaoqing/katongbiaoqing_1.html':105,
                'http://www.ghost64.com/qqbiaoqing/wenzibiaoqing_1.html':9,
                'http://www.ghost64.com/qqbiaoqing/renwubiaoqing_1.html':89,
                'http://www.ghost64.com/qqbiaoqing/gaoxiaobiaoqing_1.html':143,
                'http://www.ghost64.com/qqbiaoqing/jieribiaoqing_1.html':19,
                'http://www.ghost64.com/qqbiaoqing/alibiaoqing_1.html':5,
            },
        'urlPattern':'http://www.ghost64.com/.*/.*/\d+.html',
        'fenyePattern':['_1.html', '_%d.html'],
        'bodyPattern':{"tag":"div", "class":["con_area"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'isAlbum':1
    },
    'qqleyuan.cc':{
        'category':'表情', 
        'domain':'qqleyuan.cc', 
        'sourceUrl':{'http://qqleyuan.cc/q/qqbiaoqing/list1.html':429},
        'urlPattern':'http://qqleyuan.cc/q/\d+.html',
        'fenyePattern':['list1.html', 'list%d.html'],
        'bodyPattern':{"tag":"div", "class":["pic_body"]},
        'imgPattern':ur'src=.*',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'isAlbum':1
    },
    '047258.com':{
        'category':'表情', 
        'domain':'047258.com', 
        'sourceUrl':{'http://www.047258.com/cate/6/p/1.html':334},
        'urlPattern':'http://www.047258.com/content/\d+.html',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"div", "class":["am-margin-top-xl"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'isAlbum':1
    },

    'fuhaodq.com':{
        'category':'表情', 
        'domain':'fuhaodq.com', 
        'sourceUrl':{
                    'https://www.fuhaodq.com/qqbq/index.html':567
            },
        'urlPattern':'https://www.fuhaodq.com/.*bq/\d+.html',
        'fenyePattern':['.html', '_%d.html'],
        'bodyPattern':{"tag":"div", "id":["zoom"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'isAlbum':1
    },

    'doutula.com':{
        'category':'表情', 
        'domain':'doutula.com', 
        'sourceUrl':{
                'https://www.doutula.com/article/list/?page=1':504,
                'https://www.doutula.com/photo/list/?page=1':887
            },
        'urlPattern':'www.doutula.com/.*/\d+',
        'fenyePattern':['page=1', 'page=%d'],
        'bodyPattern':{"tag":"div", "class":["swiper-slide", "artile_des"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'(http://){0,1}img.doutula.com/production/uploads/image.{0,50}(jpg|png|gif)',
        'isAlbum':1
    },

    'qq1234.org':{
        'category':'表情', 
        'domain':'qq1234.org', 
        'sourceUrl':{
                'http://www.qq1234.org/QQbiaoqing/daquan/list_20_1.html':38,
                'http://www.qq1234.org/QQbiaoqing/GaoXiao/list_21_1.html':34,
                'http://www.qq1234.org/QQbiaoqing/biaoqingbao/list_22_1.html':70,
                'http://www.qq1234.org/QQbiaoqing/yuanchuang/list_23_1.html':19,
            },
        'urlPattern':'http://www.qq1234.org/QQbiaoqing/(daquan|GaoXiao|biaoqingbao|yuanchuang)/\d+/\d+/\d+.html',
        'fenyePattern':['1.html', '%d.html'],
        'myposPattern': {"tag":"p", "class":["main-title"]}, 
        'bodyPattern':{"tag":"div", "class":["info"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'isAlbum':1
    },
    'haatoo.com':{
        'category':'表情', 
        'domain':'haatoo.com', 
        'sourceUrl':{
                'http://www.haatoo.com/v/zhutibiaoqing/1':90,
                'http://www.haatoo.com/v/baomanbiaoqing/1':90,
                'http://www.haatoo.com/v/jinguanchangbiaoqing/1':90,
                'http://www.haatoo.com/v/renwubiaoqing/1':90,
                'http://www.haatoo.com/v/weixinbiaoqing/1':90,
                'http://www.haatoo.com/v/dongmanbiaoqing/1':90,
                'http://www.haatoo.com/v/zhenshibiaoqing/1':2,
                'http://www.haatoo.com/v/doubibiaoqing/1':90,
                'http://www.haatoo.com/v/qitabiaoqing/1':50,
            },
        'myposPattern': {"tag":"span", "class":["crumbs"]}, 
        'titlePattern': {"tag":"span", "class":["albumName"]}, 
        'urlPattern':'http://www.haatoo.com/vvv/\d+',
        'textPattern':{"tag":"div", "id":["noContent"]},
        'fenyePattern':['/1', '/%d'],
        'bodyPattern':{"tag":"div", "class":["message"]},
        'imgPattern':ur'src=.*',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'isAlbum':1
    },

    'huiyi8.com':{
        'category':'表情', 
        'domain':'huiyi8.com', 
        'sourceUrl':{
                'http://www.huiyi8.com/qqbq/index.html':19,
            },
        'urlPattern':'http://www.huiyi8.com/sc/\d+.html',
        'fenyePattern':['index.html', '%d.html'],
        'bodyPattern':{"tag":"div", "class":["imgcont"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'isAlbum':1
    },

    'vvfeng.com':{
        'category':'表情', 
        'domain':'vvfeng.com', 
        'sourceUrl':{
                'http://www.vvfeng.com/biaoqing/1.htm':19,
            },
        'urlPattern':'http://www.vvfeng.com/article/\d+.htm',
        'fenyePattern':['1.htm', '%d.htm'],
        'bodyPattern':{"tag":"div", "class":["cxtMain"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http://www.vvfeng.com/data/upload/ueditor.{0,30}(jpg|jpeg|gif|JPG|png)',
        'isAlbum':1
    },

    'qq.yh31.com':{
        'category':'表情', 
        'domain':'qq.yh31.com', 
        'sourceUrl':{
                'http://qq.yh31.com/zjbq/List_1.html':19,
            },
        'urlPattern':'http://qq.yh31.com/zjbq/\d+.html',
        'fenyePattern':['1.htm', '%d.htm'],
        'myposPattern': {"tag":"div", "class":["r_navigation"]}, 
        'bodyPattern':{"tag":"div", "class":["c_content_overflow"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'isAlbum':1
    },

    'wzfzl.cn':{
        'category':'表情', 
        'domain':'wzfzl.cn', 
        'sourceUrl':{
                'https://www.wzfzl.cn/qqbiaoqing/list_33_1.html':51,
            },
        'urlPattern':'https://www.wzfzl.cn/qqbiaoqing/\d+.html',
        'fenyePattern':['1.htm', '%d.htm'],
        'myposPattern': {"tag":"div", "class":["pos"]}, 
        'bodyPattern':{"tag":"div", "class":["artcon"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },

    'ubiaoqing.com':{
        'category':'表情', 
        'domain':'ubiaoqing.com', 
        'sourceUrl':{
                'http://www.ubiaoqing.com/new/1':6150,
            },
        'urlPattern':'http://www.ubiaoqing.com/biaoqingbao/\d+',
        'fenyePattern':['/1', '/%d'],
        'titleXpath':'//h1/text()',
        'imgXpath':'//body/div[1]/div[1]/div[1]/div[1]/img/@src',
        'contentXpath':'//strong/text()',
        'timeXpath':'',
        'myposXpath':'',
        'isAlbum':0
    },

    'qqtn.com':{
        'category':'表情',
        'domain':'qqtn.com',
        'sourceUrl':{
                'http://www.qqtn.com/bq/weixinbq_1.html':14,
                'http://www.qqtn.com/bq/gaoxiaobq_1.html':63,
                'http://www.qqtn.com/bq/shbq_1.html':10,
                'http://www.qqtn.com/bq/dtbq_1.html':36,
                'http://www.qqtn.com/bq/baozoubq_1.html':8,
                'http://www.qqtn.com/bq/jgzbq_1.html':8,
                'http://www.qqtn.com/bq/dmbq_1.html':14,
                'http://www.qqtn.com/bq/liaotianbq_1.html':21,
                'http://www.qqtn.com/bq/keaibq_1.html':42,
                'http://www.qqtn.com/bq/wenzibq_1.html':49,
                'http://www.qqtn.com/bq/maimbq_1.html':12,
                'http://www.qqtn.com/bq/tuzibq_1.html':7,
                'http://www.qqtn.com/bq/gguaibq_1.html':22,
                'http://www.qqtn.com/bq/jingdianbq_1.html':10,
                'http://www.qqtn.com/bq/yuancbq_1.html':19,
                'http://www.qqtn.com/bq/jieribq_1.html':12,
            },
        'urlPattern':'http://www.qqtn.com/article/article_\d+_\d+.html',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"div", "class":["m_qmview"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },

	'qqtn.com':{
        'category':'表情',
        'domain':'qqtn.com',
        'sourceUrl':{
                'http://www.qqtn.com/bq/weixinbq_1.html':14,
	        	'http://www.qqtn.com/bq/gaoxiaobq_1.html':63,
                'http://www.qqtn.com/bq/shbq_1.html':10,
		        'http://www.qqtn.com/bq/dtbq_1.html':36,
	        	'http://www.qqtn.com/bq/baozoubq_1.html':8,
		        'http://www.qqtn.com/bq/jgzbq_1.html':8,
		        'http://www.qqtn.com/bq/dmbq_1.html':14,
		        'http://www.qqtn.com/bq/liaotianbq_1.html':21,
		        'http://www.qqtn.com/bq/keaibq_1.html':42,
		        'http://www.qqtn.com/bq/wenzibq_1.html':49,
		        'http://www.qqtn.com/bq/maimbq_1.html':12,
		        'http://www.qqtn.com/bq/tuzibq_1.html':7,
		        'http://www.qqtn.com/bq/gguaibq_1.html':22,
		        'http://www.qqtn.com/bq/jingdianbq_1.html':10,
		        'http://www.qqtn.com/bq/yuancbq_1.html':19,
		        'http://www.qqtn.com/bq/jieribq_1.html':12,
            },
        'urlPattern':'http://www.qqtn.com/article/article_\d+_\d+.html',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"div", "class":["m_qmview"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
	    'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },

    'qq.yh31.com':{
        'category':'表情',
        'domain':'qq.yh31.com',
        'sourceUrl':{
                'http://qq.yh31.com/zjbq/List_1.html':19,
            },
        'urlPattern':'http://qq.yh31.com/zjbq/\d+.html',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"div", "class":["c_content_overflow"]},
        'myposPattern': {"tag":"div", "class":["r_navigation"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },
    

    'ld12.com':{
        'category':'表情',
        'domain':'ld12.com',
        'sourceUrl':{
                'http://www.ld12.com/qq/qqbq/48_1.html':132,
            },
        'urlPattern':'http://www.ld12.com/qq/qqbq/(\d+|((gaoxiao|keai|gaoguai)/\d+)).html',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"div", "class":["content"]},
        'myposPattern': {"tag":"div", "class":["breadcrumb"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
	'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },

    'ffpic.com':{
        'category':'表情',
        'domain':'ffpic.com',
        'sourceUrl':{
                'http://www.ffpic.com/biaoqing/index.html':220,
            },
        'urlPattern':'http://www.ffpic.com/biaoqing/\d+.html',
        'fenyePattern':['.html', '_%d.html'],
        'bodyPattern':{"tag":"div", "class":["pic"]},
        'myposPattern': {"tag":"p", "class":["path"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
	'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },
 
    'qq745.com':{
        'category':'表情',
        'domain':'qq745.com',
        'sourceUrl':{
                'http://www.qq745.com/weixinbiaoqing/list_1.html':28,
            },
        'urlPattern':'http://www.qq745.com/weixinbiaoqing/(\d+|(.*/\d+/\d+/\d+)).html',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"ul", "class":["img-list3"]},
        'myposPattern': {"tag":"div", "class":["location"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png|PNG)',
	    'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },

    'jiuwa.net':{
        'category':'表情',
        'domain':'jiuwa.net',
        'sourceUrl':{
                'http://www.jiuwa.net/face/p-1':28,
                'http://www.jiuwa.net/photo/p-1':1303,
            },
        'urlPattern':'http://www.jiuwa.net/(face|photo)/\d+/',
        'fenyePattern':['p-1', 'p-%d'],
        'bodyPattern':{"tag":"ul", "class":["pic-con face-list", "pic-con"]},
        'myposPattern': {"tag":"div", "class":["tags"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
	    'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },

    'qqface.knowsky.com':{
        'category':'表情',
        'domain':'qqface.knowsky.com',
        'sourceUrl':{
                'http://qqface.knowsky.com/index_1.htm':70,
            },
        'urlPattern':'http://qqface.knowsky.com/qqbiaoqing_\d+.htm',
        'fenyePattern':['1.htm', '%d.htm'],
        'bodyPattern':{"tag":"div", "class":["fontviewinfopic"]},
        'myposPattern': {"tag":"div", "class":["pt"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
    	'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },

    '007360.com':{
        'category':'表情',
        'domain':'007360.com',
        'sourceUrl':{
                'http://www.007360.com/qqbq/list_29_1.html':54,
            },
        'urlPattern':'http://www.w2qq.com/.*/\d+.html',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"ul", "class":["artCon"]},
        'myposPattern': {"tag":"div", "class":["currentSite"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
	    'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },

}
