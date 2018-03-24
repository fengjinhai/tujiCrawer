#encoding:utf-8

webInfo = {
    'wed114.cn':{
        'category':'美妆', 
        'domain':'wed114.cn', 
        'sourceUrl':{
                'http://www.wed114.cn/jiehun/meirong/list_110_1.html':1403,
                'http://www.wed114.cn/jiehun/fushi/list_112_1.html':311,
                'http://www.wed114.cn/jiehun/shishangbaobao/list_352_1.html':16,
            },
        'urlPattern':'http://www.wed114.cn/jiehun/.*/\d+.html',
        'bodyPattern':{"tag":"div", "class":["substance"]},
        'myposPattern': {"tag":"div", "class":["position"]}, 
        'imgPattern':ur'(?is)(<img.*?>)',
        'detailFenyePattern':['.html','_%d.html'],
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'fenyePattern':['1.html','%d.html'],
        'isAlbum':1
     },

    'tuku.wed114.cn':{
        'category':'美妆', 
        'domain':'tuku.wed114.cn', 
        'sourceUrl':{
                'http://www.wed114.cn/jiehun/tuku/fushidapei/list_107_1.html':22,
                'http://www.wed114.cn/jiehun/tuku/caizhuangfaxing/list_104_1.html':46,
            },
        'urlPattern':'http://www.wed114.cn/jiehun/tuku/.*/\d+.html',
        'fenyePattern':['1.html','%d.html'],
        'detailFenyePattern':['.html', '_%d.html'],
        'titleXpath':'//span[@id="txttitle"]/text()',
        'imgXpath':'//img[@id="bigimg"]/@src',
        'contentXpath': '//div[@class="intro"]/p/text()', 
        'timeXpath':'//div[@class="weninfo"]/text()',
        'myposXpath':'//dl[@class="picnav"]/span/a/text()',
        'detailFyXpath':'//span[@id="total"]/text()',
        'isAlbum':2

     },


     'product.efu.com.cn':{
            'category':'美妆',
            'domain':'product.efu.com.cn',
            'sourceUrl':{
                    'http://product.efu.com.cn/list-170-0-0-0-1.html':4600,
                    'http://product.efu.com.cn/topic-1-0-1.html':140,
            },
            'urlPattern':'http://product.efu.com.cn/topicshow-.*.html',
            'fenyePattern':['1.html', '%d.html'],
            'bodyPattern':{"tag":"ul", "class":["thumbs"]},
            'myposPattern': {"tag":"div", "class":["corpCrumbs"]},
            'textPattern': {"tag":"div", "class":["proNewBox-l"]},
            'imgReplace':[['small_','big_']],
            'imgPattern':ur'(?is)(<img.*?>)',
            'imgUrlPattern':'http.*\.(jpg|jpeg|JPG|png)',
            'isAlbum':1
     },
     'fashion.efu.com.cn':{
            'category':'美妆',
            'domain':'fashion.efu.com.cn',
            'sourceUrl':{
                    'http://fashion.efu.com.cn/showlist-0-1-0.html':260,
            },
            'urlPattern':'http://fashion.efu.com.cn/show-\d+.html',
            'fenyePattern':['-1-', '-%d-'],
            'bodyPattern':{"tag":"div", "id":["thumbnail"]},
            'myposPattern': {"tag":"div", "class":["newsCrumbs"]},
            'textXpath': '//h1/text()',
            'imgPattern':ur'(?is)(<img.*?>)',
            'imgUrlPattern':'http.*\.(jpg|jpeg|JPG|png)',
            'isAlbum':1
     },

     'news.fashion.efu.com.cn':{
            'category':'美妆',
            'domain':'news.fashion.efu.com.cn',
            'sourceUrl':{
                    'http://fashion.efu.com.cn/list-19-1-0.html':480,
            },
            'urlPattern':'http://fashion.efu.com.cn/newsview-\d+-1.html',
            'fenyePattern':['-1-', '-%d-'],
            'bodyPattern':{"tag":"div", "id":["Cnt-Main-Article-EFU"]},
            'myposPattern': {"tag":"div", "class":["newsCrumbs"]},
            'textXpath': '//h1/text()',
            'detailFenyePattern':['1.html','%d.html'],
            'imgPattern':ur'(?is)(<img.*?>)',
            'imgUrlPattern':'http.*\.(jpg|jpeg|JPG|png)',
            'isAlbum':1
     },
    'haobizhi.com':{
            'category':'美妆',
            'domain':'haobizhi.com',
            'sourceUrl':{
                    'http://www.haobizhi.com/meinv/1.htm':150,
            },
            'urlPattern':'http://www.haobizhi.com/bizhi/\d+.htm',
            'fenyePattern':['1.htm', '%d.htm'],
            'bodyPattern':{"tag":"div", "class":["pic"]},
            'myposPattern': {"tag":"div", "class":["breadcrumb"]},
            'detailFenyePattern':['', '%d.htm'],
            'imgPattern':ur'(?is)(<img.*?>)',
            'imgUrlPattern':'http.*\.(jpg|jpeg|JPG|png)',
            'isAlbum':1
    },
 

    'jb51.net':{
        'category':'美妆', 
        'domain':'jb51.net', 
        'sourceUrl':{
                'http://sc.jb51.net/wenshen/list_1.html':105,
                'http://sc.jb51.net/zhuanti/meijiatupian/index_1.html':12,
                'http://sc.jb51.net/zhuanti/rentiyishu_1.html':50,
            },
        'urlPattern':'http://sc.jb51.net/.*/\d+.htm',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"div", "class":["content-b","content-bb"]},
        'myposPattern': {"tag":"div", "class":["pos"]}, 
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'isAlbum':1
    },

    'win4000.com':{
        'category':'美妆', 
        'domain':'win4000.com', 
        'sourceUrl':{'http://www.win4000.com/meinvtag23_1.html':9},
        'urlPattern':'http://www.win4000.com/meinv\d+.html',
        'bodyPattern':{"tag":"p", "class":["scroll-img"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgReplace':[['_100.jpg','']],
        'myposPattern': {"tag":"div", "class":["mei-location"]}, 
        'textPattern': {"tag":"div", "class":["tags"]}, 
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'fenyePattern':['1.html','%d.html'],
        'isAlbum':1
    },

     'mxmop.com':{
            'category':'美妆',
            'domain':'mxmop.com',
            'sourceUrl':{
                    'http://www.mxmop.com/faxing/page/1/':455,
            },
            'urlPattern':'http://www.mxmop.com/.*/\d+.html',
            'fenyePattern':['/1/', '/%d/'],
            'bodyPattern':{"tag":"div", "id":["itemContainer"]},
            'publishTimeXpath':'//span[@class="content-time"]/text()',
            'textXpath':'//div[@id="container"]/div[2]/p[2]/text()',
            'myposPattern': {"tag":"div", "id":["crumb"]},
            'imgPattern':ur'(?is)(<img.*?>)',
            'imgUrlPattern':'http.*\.(jpg|jpeg|JPG|png)',
            'isAlbum':1
     },

    'ivsky.com':{
        'category':'美妆', 
        'domain':'ivsky.com', 
        'sourceUrl':{
                'http://www.ivsky.com/tupian/meirong_t1365/index_1.html':67,
                'http://www.ivsky.com/tupian/huazhuang_t5414/index_1.html':37,
                'http://www.ivsky.com/tupian/shishang_t1517/index_1.html':79,
            },
        'urlPattern':'http://www.ivsky.com/tupian/.*\d+.html',
        'bodyPattern':{"tag":"img", "id":["imgis"]},
        'imgPattern':ur'(?is)(<img.*?>)',
         'myposPattern': {"tag":"div", "class":["pos"]}, 
        'fenyePattern':['_1.html','_%d.html'],
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'textPattern': {"tag":"div", "class":["al_info"]}, 
        'isAlbum':1
        },
    'qqtn.com':{
        'category':'美妆',
        'domain':'qqtn.com',
        'sourceUrl':{
                'http://www.qqtn.com/health/mj_164_1.html':3,
            },
        'urlPattern':'http://www.qqtn.com/health/\d+_1.html',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"div", "class":["m-main"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'isAlbum':1
    },

    'zol.com.cn':{
        'category':'美妆', 
        'domain':'zol.com.cn', 
        'sourceUrl':{
                'http://desk.zol.com.cn/chemo/1.html':3,
            },
        'urlPattern':'zol.com.cn/.*_\d+_\d+.html',
        'myposPattern': {"tag":"div", "class":["location"]}, 
        'textPattern': {"tag":"div", "class":["tag-link"]}, 
        'bodyPattern':{"tag":"div", "class":["photo-set-list"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'fenyePattern':['1.html','%d.html'],
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'imgReplace':[['/t_s144x90','/t_s960x600']],
        'isAlbum':1
        },

    '85814.com':{
        'category':'美妆', 
        'domain':'85814.com', 
        'sourceUrl':{
                'http://www.85814.com/tags/明星发型_1':51,
                'http://www.85814.com/tags/女生发型_1':65,
                'http://www.85814.com/tags/男生发型_1':43,
                'http://www.85814.com/tags/流行发型_1':57,
            },
        'urlPattern':'http://www.85814.com/\d+',
        'fenyePattern':['_1','_%d'],
        'detailFenyePattern':['.html', '_%d.html'],
        'titleXpath':'//h1/text()',
        'imgXpath':'//*[@id="d"]/dd/p/img/@src',
        'contentXpath': '//*[@id="d"]/dd/i/a/text()', 
        'timeXpath':'',
        'myposXpath':'',
        'detailFyXpath':'//h1/em/text()',
        'isAlbum':2
        },

  'vsuch.com':{
        'category':'美妆',
        'domain':'vsuch.com',
        'sourceUrl':{
                'http://beauty.vsuch.com/StarBeauty/index.html':102,
                'http://beauty.vsuch.com/MakeUp/index.html':217,
                'http://beauty.vsuch.com/Skin/index.html':180,
                'http://beauty.vsuch.com/HairStyle/index.html':136,
                'http://beauty.vsuch.com/BeautyBody/index.html':55,
                'http://beauty.vsuch.com/Nail/index.html':30,
                'http://beauty.vsuch.com/Fragrance/index.html':40,
                'http://luxury.vsuch.com/jewelry/index.html':34,
                'http://luxury.vsuch.com/watch/index.html':98,
                'http://luxury.vsuch.com/bag/index.html':25,
                'http://luxury.vsuch.com/footwear/index.html':19,
                'http://star.vsuch.com/starnews/index.html':156,
                'http://dress.vsuch.com/fashiontrend/index.html':74,
                'http://dress.vsuch.com/style/index.html':92,
                'http://dress.vsuch.com/show/index.html':24,
                'http://dress.vsuch.com/showparty/index.html':40,
                'http://dress.vsuch.com/collocation/index.html':256,
            },
        'urlPattern':'http://.*vsuch.com/\d+/.*/\d+.html',
        'fenyePattern':['index.html', '%d.html'],
        'bodyPattern':{"tag":"div", "class":["mcontent"]},
        'myposPattern': {"tag":"div", "class":["position"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http://pic.vsuch.com/\d+/\d+/\d+.(jpg|jpeg|gif|JPG|png)',
        'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },


    'woouu.com':{
        'category':'美妆', 
        'domain':'woouu.com', 
        'sourceUrl':{
                'http://www.woouu.com/beautiful/':78,
            },
        'urlPattern':'http://www.woouu.com/beautiful/\d+.html',
        'fenyePattern':['', 'list3%d.html'],
        'titleXpath':'//div[@class="page-header"]/h3/text()',
        'imgXpath':'//body/div[3]/div/div/img/@src',
        'contentXpath': '//p[@id="description_jianjie"]/text()',
        'timeXpath':'',
        'myposXpath':'',
        'isAlbum':0
        },


}

