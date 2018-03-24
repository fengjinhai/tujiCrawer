#encoding:utf-8
webInfo = {
    'tooopen.com':{
         'category':'人物',
         'domain':'tooopen.com',
         'sourceUrl':{
                 'http://www.tooopen.com/img/88_0_1_1.aspx':1553,  
             },
         'fenyePattern':['1.aspx', '%d.aspx'],
         'urlPattern':'http://www.tooopen.com/view/\d+.html',
         'bodyPattern':{"tag":"div", "class":["pic-box"]},
         'myposPattern': {"tag":"div", "class":["loca"]},
         'textPattern': {"tag":"li", "class":["key"]},
         'imgPattern':ur'(?is)(<img.*?>)',
         'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
         'isAlbum':1
        },

     'taopic.com':{
         'category':'人物',
         'domain':'taopic.com',
         'sourceUrl':{
                 'http://www.taopic.com/tuku/renwutupian/list_1.html':6296,
             },
         'urlPattern':'http://www.taopic.com/tuku/\d+/\d+.html',
         'fenyePattern':['1.html', '%d.html'],
         'bodyPattern':{"tag":"div", "class":["viewBoxPad"]},
         'myposPattern': {"tag":"div", "class":["crumbs"]},
         'textPattern': {"tag":"div", "class":["viewBoxPad"]},
         'imgPattern':ur'(?is)(<img.*?>)',
         'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
         'isAlbum':1
        },

     'gexing.com':{
         'category':'人物',
         'domain':'gexing.com',
         'sourceUrl':{
                 'http://www.gexing.com/shaitu/1':6778,
             },
         'urlPattern':'http://www.gexing.com/shaitu/\d+.html',
         'fenyePattern':['/1', '/%d'],
         'bodyPattern':{"tag":"ul", "class":["ttTxtImg"]},
         'textPattern': {"tag":"div", "class":["left"]},
         'titleXpath': '//h2/text()',
         'imgPattern':ur'(?is)(<img.*?>)',
         'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
         'isAlbum':1
        },

    'guandongphoto.com':{
        'category':'人物', 
        'domain':'guandongphoto.com', 
        'sourceUrl':{'http://www.guandongphoto.com/forum-6-2.html':469},
        'urlPattern':'http://www.guandongphoto.com/thread-\d+-\d+-\d+.html',
        'fenyePattern':['2.html', '%d.html'],
        'titleXpath':'//span[@id="thread_subject"]/text()',
        'imgXpath':'//ignore_js_op/img/@file',
        'contentXpath':'//*[@id="postmessage_8351674"]/text()',
        'timeXpath':'//tbody/tr[1]/td[2]/div[1]/div[2]/div[2]/div[2]/em[1]/text()',
        'myposXpath':'//div[@class="z"]/a/text()',
        'isAlbum':0
    },

    'quanjing.com':{
        'category':'人物', 
        'domain':'quanjing.com', 
        'sourceUrl':{
            'http://www.quanjing.com/category/103003/1.html':1606,
            'http://www.quanjing.com/category/103008/1.html':1660,
            'http://www.quanjing.com/category/103023/1.html':16667,
            'http://www.quanjing.com/category/103111/1.html':393,
        },
        'urlPattern':'http://www.quanjing.com/imgbuy/.*.html',
        'fenyePattern':['1.html', '%d.html'],
        'titleXpath':'//div[@class="keylisttitcon"]/text()',
        'imgXpath':'//img[@id="picurl"]/@src',
        'contentXpath':'//ul[@id="Ul1"]/li/a/text()',
        'timeXpath':'',
        'myposXpath':'',
        'isAlbum':0
    },
    'search.quanjing.com':{
        'category':'人物', 
        'domain':'search.quanjing.com', 
        'sourceUrl':{
            'http://www.quanjing.com/search.aspx?q=帅哥||1|200|1|2||||':14217,
            'http://www.quanjing.com/search.aspx?q=亲情||1|200|1|2||||':414,
            'http://www.quanjing.com/search.aspx?q=白领||1|200|1|2||||':4260,
            'http://www.quanjing.com/search.aspx?q=运动||1|200|1|2||||':6305,
            'http://www.quanjing.com/search.aspx?q=小清新||1|200|1|2||||':204,
            'http://www.quanjing.com/search.aspx?q=女人||1|200|1|2||||':21571,
            'http://www.quanjing.com/search.aspx?q=家庭||1|200|1|2||||':3486,
            'http://www.quanjing.com/search.aspx?q=快乐家庭||1|200|1|2||||':2292,
        },
        'urlPattern':'http://www.quanjing.com/imgbuy/.*.html',
        'fenyePattern':['1|2||||', '%d|2||||'],
        'titleXpath':'//div[@class="keylisttitcon"]/text()',
        'imgXpath':'//img[@id="picurl"]/@src',
        'contentXpath':'//ul[@id="Ul1"]/li/a/text()',
        'timeXpath':'',
        'myposXpath':'',
        'isAlbum':0
    },

     'tuku.cn':{
         'category':'人物',
         'domain':'tuku.cn',
         'sourceUrl':{
                 'http://www.tuku.cn/aclass.aspx?id=23&Page=1':4,
                 'http://www.tuku.cn/aclass.aspx?id=15&Page=1':3,
                 'http://www.tuku.cn/aclass.aspx?id=18&Page=1':4,
             },
         'urlPattern':'http://www.tuku.cn/class.aspx\?typeid=\d+',
         'fenyePattern':['Page=1', 'Page=%d'],
         'bodyPattern':{"tag":"span", "id":["class_DataList1"]},
         'myposPattern': {"tag":"div", "class":["mianbaoxie"]},
         'textPattern': {"tag":"div", "class":["gallery_jieshao"]},
         'imgPattern':ur'(?is)(<img.*?>)',
         'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
         'imgReplace':[['/s0','/0']],
         'detailFenyePattern':['', '&Page=%d'],
         'isAlbum':1
        },

     'ivsky.com':{
         'category':'人物',
         'domain':'ivsky.com',
         'sourceUrl':{
                 'http://www.ivsky.com/tupian/renwutupian/index_1.html':89,
             },
         'urlPattern':'http://www.ivsky.com/tupian/.*?_v\d+/',
         'fenyePattern':['1.html', '%d.html'],
         'bodyPattern':{"tag":"ul", "class":["pli"]},
         'myposPattern': {"tag":"div", "class":["pos"]},
         'textPattern': {"tag":"div", "class":["al_p"]},
         'imgPattern':ur'(?is)(<img.*?>)',
         'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
         'imgReplace':[['/t/','/pre/']],
         'detailFenyePattern':['', 'index_%d.html'],
         'isAlbum':1
        },

    '588ku.com':{
        'category':'人物',
        'domain':'588ku.com',
        'sourceUrl':{
                'http://588ku.com/?m=peitu&a=category&type=9&page=1':500,
            },
        'urlPattern':'http://588ku.com/peitu/\d+.html',
        'fenyePattern':['page=1', 'page=%d'],
        'bodyPattern':{"tag":"div", "class":["img-l-box"]},
        'myposPattern': {"tag":"div", "class":["illustration"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|JPG|png)',
        #'imgReplace':[['img.zhuoku.com','bizhi.zhuoku.com']],
        #'textXpath':'//div[@id="liebiaom"]/h1/text()',
	'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },

    'warting.com':{
        'category':'人物',
        'domain':'warting.com',
        'sourceUrl':{
                'http://www.warting.com/pic/people/list_1.html':47,
            },
        'urlPattern':'http://www.warting.com/pic/\d+/\d+/\d+.html',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"div", "class":["picshow_second"]},
        'myposPattern': {"tag":"div", "class":["location"]},
        'textXpath':'//div[@class="layout article_con"]/h1/text()',
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        #'imgReplace':[['/s/','/l/']],
        'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },

    'tupianzj.com':{
        'category':'人物',
        'domain':'tupianzj.com',
        'sourceUrl':{
                'http://www.tupianzj.com/sheying/ren/list_7_1.html':26,
                'http://www.tupianzj.com/meinv/xiezhen/list_179_1.html':131,
            },
        'urlPattern':'http://www.tupianzj.com/((meinv)|(sheying/ren))/\d+/\d+.html',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"div", "id":["bigpic_all"]},
        'myposPattern': {"tag":"div", "class":["weizhi970"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*?-.*?\.(jpg|jpeg|gif|JPG|png)',
        'textXpath':'//div[@class="viewbox_titlefo"]/h1/text()',
        'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },

    'sc.chinaz.com':{
        'category':'人物',
        'domain':'sc.chinaz.com',
        'sourceUrl':{
                'http://sc.chinaz.com/tupian/renwutupian.html':508,
            },
        'fenyePattern':['.html', '_%d.html'],
        'urlPattern':'http://sc.chinaz.com/tupian/\d+.htm',
        'myposPattern': {"tag":"div", "class":["dangqian"]},
        'bodyPattern':{"tag":"div", "class":["imga"]},
        'textXpath':'//div[@class="text_wrap"]/h2/a/text()',
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*?\.(jpg|jpeg|gif|JPG|png)',
        'isAlbum':1
    },

    'win4000.com':{
        'category':'人物',
        'domain':'win4000.com',
        'sourceUrl':{
                'http://www.win4000.com/meinvtag23_1.html':9,
            },
        'fenyePattern':['1.html', '%d.html'],
        'urlPattern':'http://www.win4000.com/meinv\d+.html',
        'myposPattern': {"tag":"p", "class":["mei-location"]},
        'bodyPattern':{"tag":"ul", "id":["scroll"]},
        'textXpath':'//div[@class="where clearfix"]/h1/text()',
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*?\.(jpg|jpeg|gif|JPG|png)',
        'imgReplace':[['_100.jpg','']],
        'isAlbum':1
    },

    'jj20.com':{
        'category':'人物',
        'domain':'jj20.com',
        'sourceUrl':{
                'http://www.jj20.com/bz/rwtx/list_8_1.html':13,
            },
        'fenyePattern':['1.html', '%d.html'],
        'urlPattern':'http://www.jj20.com/bz/rwtx/.*?/\d+.html',
        'myposPattern': {"tag":"div", "class":["fl"]},
        'bodyPattern':{"tag":"div", "class":["tu-st"]},
        'textXpath':'//div[@class="wzfz tu-tit fix"]/h1/span/text()',
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*?\.(jpg|jpeg|gif|JPG|png)',
        'imgReplace':[['-lpp.jpg','.jpg']],
        'isAlbum':1
    },

    'sc.jb51.net':{
        'category':'人物',
        'domain':'sc.jb51.net',
        'sourceUrl':{
                'http://sc.jb51.net/picture/figure/list_34_1.html':346,
                'http://sc.jb51.net/zhuanti/qinglvtupian_1.html':22,
                'http://sc.jb51.net/zhuanti/xingganmeinv/index_1.html':32,
                'http://sc.jb51.net/zhuanti/rentiyishu_1.html':50,
                'http://sc.jb51.net/zhuanti/shuaigetupian_1.html':30,
                'http://sc.jb51.net/zhuanti/motetupian_1.html':25,
            },
        'fenyePattern':['1.html', '%d.html'],
        'urlPattern':'http://sc.jb51.net/picture/(figure|design)/\d+.htm',
        'myposPattern': {"tag":"div", "class":["pos"]},
        'bodyPattern':{"tag":"div", "class":["content-b"]},
        'textXpath':'//div[@class="content-b"]/strong[1]/text()',
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*?\.(jpg|jpeg|gif|JPG|png)',
        #'imgReplace':[['-lpp.jpg','.jpg']],
        'isAlbum':1,
    },
}
