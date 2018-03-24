#encoding:utf-8
webInfo = {
    '588ku.com': {
        'category': '动物',
        'domain': '588ku.com',
        'sourceUrl': {
            'http://588ku.com/?m=peitu&a=category&keyword=dongwu&type=10&page=1': 400,
            'http://588ku.com/?m=peitu&a=category&keyword=mengchong&type=6&page=1': 346
        },
        'urlPattern': 'http://588ku.com/.*/\d+.html',
        'fenyePattern': ['page=1', 'page=%d'],
        'bodyPattern': {'tag': 'div','class': ['img-l-box']},'imgPattern': u'(?is)(<img.*?>)',
        'textXpath': u'//div[@class="desc"]/dl[1]/dd/span/text()',
        'imgUrlPattern': 'http.*\.(jpg|jpeg|gif|JPG|png)',
        'myposXpath': '//div[@class="bread-nav"]/span/text()',
        'isAlbum': 1
   },
   'warting.com': {
        'category': '动物',
        'domain': 'warting.com',
        'sourceUrl': {
            'http://www.warting.com/wallpaper/animal/list_1.html': 9,
	    'http://www.warting.com/pic/animal/list_1.html': 23
	},
        'urlPattern': 'http://www.warting.com/.*/\d+/\d+.html',
        'fenyePattern': ['1.html', '%d.html'],
        'bodyPattern': {'tag': 'ul','class': ['picshow_first', 'picshow_third', 'picshow_second']},'imgPattern': u'(?is)(<img.*?>)',
        'myposPattern': {'tag': 'div','class': ['location']},'imgUrlPattern': 'http.*\.(jpg|jpeg|gif|JPG|png)',
        'textPattern': {'tag': 'div','class': ['article_bd']},
        'detailFenyePattern': ['.html', '_%d.html'],
        'isAlbum': 1
    },
    'tuku.cn': {
        'category': '动物',
        'domain': 'tuku.cn',
        'sourceUrl': {
            'http://www.tuku.cn/wallpapers.aspx?id2=39&Page=1': 6,
            'http://www.tuku.cn/aclass.aspx?id=3&Page=1': 3
        },
        'urlPattern': 'http://www.tuku.cn/.*typeid=\d+',
        'bodyPattern': {'tag': 'from','id': ['form1']},'imgPattern': u'(?is)(<img.*?>)',
        'fenyePattern': ['Page=1', 'Page=%d'],
        'imgUrlPattern': u'http://image5.tuku.cn/pic/.*/s\d+.(jpg|jpeg)',
        'detailFenyePattern': ['', '&Page=%d'],
        'imgReplace': [['/s0', '/0'], ['/s1', '/1'], ['/s2', '/2'], ['/s3', '/3'], ['/s4', '/4'], ['/s5', '/5']],
        'isAlbum': 1
    },
    'niutuku.com': {
        'category': '动物',
        'domain': 'niutuku.com',
        'sourceUrl': {
            'http://niutuku.com/hd/4/index.shtml': 300,
	    'http://niutuku.com/bizhi/7/index.shtml': 25,
	    'http://niutuku.com/bizhi/53/index.shtml': 3,
	    'http://niutuku.com/bizhi/54/index.shtml': 4,
	    'http://niutuku.com/shoujibizhi/5/index.shtml': 49
	},
        'urlPattern': 'http://niutuku.com/(hd|shoujibizhi|bizhi)/\d+.shtml',
        'bodyPattern': {'tag': 'dl','class': ['container', 'preview']},'imgPattern': u'(?is)(<img.*?>)',
        'myposPattern': {'tag': 'div','class': ['place']},'fenyePattern': [
		      '.shtml', '_%d.shtml'],
        'imgUrlPattern': u'http.*\.(jpg|jpeg|gif|JPG|png)',
        'imgReplace': [['190', '960']],
        'isAlbum': 1
    },
    'ivsky.com': {
        'category': '动物',
	'domain': 'ivsky.com',
	'sourceUrl': {
            'http://www.ivsky.com/tupian/dongwutupian/index_1.html': 134,
	    'http://www.ivsky.com/bizhi/dongwu/index_1.html': 20
	 },
	'urlPattern': 'http://www.ivsky.com/.{0,30}/.{0,60}/',
	'bodyPattern': {'tag': 'ul','class': ['pli', 'il', 'ali']},
        'imgPattern': u'(?is)(<img.*?>)',
	'fenyePattern': ['_1.html', '_%d.html'],
	'imgUrlPattern': u'http.*\.(jpg|jpeg|gif|JPG|png)',
	'textPattern': {'tag': 'div','class': ['al_info']},
        'imgReplace': [['/t/', '/pre/']],
        'isAlbum': 1
    },
    'pchome.net': {
        'category': '动物',
        'domain': 'pchome.net',
	'sourceUrl': {
             'http://download.pchome.net/wallpaper/dongwu/p1/': 31,
	     'http://download.pchome.net/wallpaper/notebook/dongwu/t24p1/': 21,
	     'http://download.pchome.net/wallpaper/pad/dongwu/p1/': 6,
	     'http://download.pchome.net/wallpaper/mobile/dongwu/p1/': 14
         },
        'urlPattern': 'http://download.pchome.net/wallpaper/info-.*.html',
        'imgUrlPattern': u'http.*\.(jpg|jpeg|gif|JPG|png)',
        'fenyePattern': [
        'p1/', 'p%d/'],
        'detailFenyePattern': ['-1-', '-%d-'],
        'titleXpath': '//h3/a/text()',
        'imgXpath': '//img[@id="bigImg"]/@src',
        'contentXpath': '',
        'timeXpath': '',
        'myposXpath': '//div[@class="location-nav"]/div/a/text()',
        'detailFyXpath': '//h3/span/text()',
        'isAlbum': 2
    },
    '50tu.com': {
        'category': '动物',
        'domain': '50tu.com',
	    'sourceUrl': {'http://50tu.com/bizhi/dongwu/index.html': 18
        },
        'urlPattern': 'http://50tu.com/bizhi/.{0,30}/\d+-\d+-\d+/\d+.html',
        'fenyePattern': ['.html', '_%d.html'],
        'imgUrlPattern': u'http.*\.(jpg|jpeg|gif|JPG|png)',
        'detailFenyePattern': ['.html', '_%d.html'],
        'titleXpath': '//h1/text()',
        'imgXpath': '//div[@class="wrap"]/img/@src',
        'contentXpath': '',
        'timeXpath': '',
        'myposXpath': '//div[@class="palce"]/a/text()',
        'detailFyXpath': '//h1/text()',
        'isAlbum': 2
    },
     'tooopen.com':{
         'category':'动物',
         'domain':'tooopen.com',
         'sourceUrl':{
                 'http://www.tooopen.com/img/89_0_1_1.aspx':333,  
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
         'category':'动物',
         'domain':'taopic.com',
         'sourceUrl':{
                 'http://www.taopic.com/tuku/dongwutupian/list_1.html':470,
             },
         'urlPattern':'http://www.taopic.com/tuku/\d+/\d+.html',
         'fenyePattern':['1.html', '%d.html'],
         'bodyPattern':{"tag":"div", "class":["viewBoxPad"]},
         'myposPattern': {"tag":"div", "class":["crumbs"]},
         'imgPattern':ur'(?is)(<img.*?>)',
         'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
         #'textXpath':'//div[@class="viewBoxPad"]/div/div[2]/p/text()',
         'isAlbum':1
        },

    'zhuoku.com':{
        'category':'动物',
        'domain':'zhuoku.com',
        'sourceUrl':{
                'http://www.zhuoku.com/zhuomianbizhi/dong-dongwu/index-1.htm':12,
            },
        'urlPattern':'http://www.zhuoku.com/zhuomianbizhi/dong-dongwu/\d+.htm',
        'fenyePattern':['1.htm', '%d.htm'],
        'bodyPattern':{"tag":"div", "id":["liebiao"]},
        'myposPattern': {"tag":"div", "class":["nav"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|JPG|png)',
        'imgReplace':[['img.zhuoku.com','bizhi.zhuoku.com'],['thumbs/tn_',''],['zhuoku_','']],
        'textXpath':'//div[@id="liebiaom"]/h1/text()',
	    'detailFenyePattern':['.htm', '_%d.htm'],
        'isAlbum':1
    },

    'bizhi.knowsky.com':{ 
        'category':'动物', 
        'domain':'bizhi.knowsky.com',
        'sourceUrl':{
                'http://bizhi.knowsky.com/bizhi_more.asp?page=1&id=1':8,
            },
        'urlPattern':'http://bizhi.knowsky.com/bizhi_list.asp\?id=\d+',
        'fenyePattern':['page=1', 'page=%d'],
        'bodyPattern':{"tag":"div", "id":["fontindexlist"]},
        'myposXpath': '//div[@class="pt z mt10"]/text()',
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'imgReplace':[['/s/','/l/']],
        'detailFenyePattern':['asp?', 'asp?page=%d&'],
        'isAlbum':1
    },

    'sc115.com':{
        'category':'动物',
        'domain':'sc115.com',
        'sourceUrl':{
                'http://www.sc115.com/photo/dongwutupian/index.html':17,
            },
        'urlPattern':'http://www.sc115.com/photo/\d+.html',
        'fenyePattern':['.html', '_%d.html'],
        'bodyPattern':{"tag":"div", "class":["preview"]},
        'myposPattern': {"tag":"div", "class":["path"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*?\.(jpg|jpeg|gif|JPG|png)',
        #'textXpath':'//p[@class="f14 cGray lh24"]/text()',      
        'isAlbum':1
    },

    'm1ok.com':{
        'category':'动物',
        'domain':'m1ok.com',
        'sourceUrl':{
                'http://www.m1ok.com/scgqtp/scgqtpdw1.shtm':49,
                'http://www.m1ok.com/desk/deskdw1.shtm':21,
            },
        'urlPattern':'http://www.m1ok.com/Article/\d+/\d+/index.htm',
        'bodyPattern':{"tag":"div", "class":["scMainLC", "piclistshow"]},
        'fenyePattern':['1.shtm','%d.shtm'],
        'imgPattern':ur'src=.*',
        'imgUrlPattern':'http.*upload.*\.(jpg|jpeg|gif|JPG|png)',
        'textXpath':'//div[@class="scMainLT link07"]/h1/text()',
        'myposXpath':'//div[@class="scMainLT link07"]/span/text()',
        'imgReplace':[['s.jpeg','.jpeg'],],
        'isAlbum':1
    },

    'm.bz55.com':{
        'category':'动物',
        'domain':'m.bz55.com',
        'sourceUrl':{
                'http://m.bz55.com/sjdongwusjbz/':14,
            },
        'urlPattern':'http://m.bz55.com/\d+.html',
        'fenyePattern':['', '%d.html'],
        'bodyPattern':{"tag":"div", "id":["im"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },
    
    'jituwang.com':{
        'category':'动物',
        'domain':'jituwang.com',
        'sourceUrl':{
                'http://www.jituwang.com/tuku/ludidongwu/list_1.html':148,
                'http://www.jituwang.com/tuku/shuizhongdongwu/list_1.html':619,
                'http://www.jituwang.com/tuku/kongzhongdongwu/list_1.html':21,
            },
        'urlPattern':'http://www.jituwang.com/.{0,30}/\d+/\d+.html',
        'fenyePattern':['list_1.html', 'list_%d.html'],
        'bodyPattern':{"tag":"div", "class":["bg_img"]},
        'myposPattern': {"tag":"div", "class":["breakcrumb"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',        
        'textPattern':{"tag":"div", "class":["img_title"]},
        'isAlbum':1,
    },

    'chinaz.com':{
        'category':'动物',
        'domain':'chinaz.com',
        'sourceUrl':{
                'http://sc.chinaz.com/tupian/dongwutupian.html':168,
                'http://desk.chinaz.com/dongwu/index.html':2,
            },
        'urlPattern':'((http://desk.chinaz.com/dongwu/\d+.html)|(http://sc.chinaz.com/tupian/\d+.htm))',
        'fenyePattern':['.html', '_%d.html'],
        'bodyPattern':{"tag":"div", "class":["imga","picBox"]},
        'myposPattern': {"tag":"div", "class":["dangqianweizh", "dangqian"]},
        'textPatter':{"tag":"div", "class":["title", "text_wrap"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1,
    },


    'jj20.com':{
        'category':'动物',
        'domain':'jj20.com',
        'sourceUrl':{
                'http://www.jj20.com/bz/dwxz/list_2_1.html':30,
            },
        'urlPattern':'http://www.jj20.com/bz/dwxz/.*/\d+.html',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"div", "class":["tu-st"]},
        'myposPattern':{"tag":"div", "class":["fl"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*?\.(jpg|jpeg|gif|JPG|png)',
        'detailFenyePattern':['.html', '_%d.html'],
        'imgReplace':[['-lpp.jpg','.jpg']],
        'textXpath':'//div[@class="wzfz tu-tit fix"]/h1/text()', 
        'isAlbum':1
    },

    'bz55.com':{
        'category':'动物',
        'domain':'bz55.com',
        'sourceUrl':{
                'http://www.bz55.com/dongwubizhi/':63,
            },
        'urlPattern':'http://www.bz55.com/dongwubizhi/\d+/\d+/\d+.html',
        'fenyePattern':['', 'list_49_%d.html'],
        'bodyPattern':{"tag":"div", "class":["imglist"]},
        'myposPattern':{"tag":"div", "class":["article_position"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'detailFenyePattern':['.html', '_%d.html'],
        'textXpath':'//div[@class="article_title"]/h1/text()',
        'isAlbum':1
    },

    'mxmop.com':{
        'category':'动物',
        'domain':'mxmop.com',
        'sourceUrl':{
                'http://www.mxmop.com/dongwu/page/1/':445,
            },
        'urlPattern':'http://www.mxmop.com/dongwu/\d+.html',
        'fenyePattern':['1/', '%d/'],
        'bodyPattern':{"tag":"div", "id":["itemContainer"]},
        'myposPattern': {"tag":"div", "class":["center"]},
        #'myposXpath': '//table[@id="middle"]/tbody/tr/td[1]/div[1]/table/tbody/tr/td[2]/a/text()',
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'detailFenyePattern':['.html', '_%d.html'],
        'textXpath':'//div[@class="content-box"]/p/text()',
        'isAlbum':1
    },

    'zol.com.cn':{
        'category':'动物',
        'domain':'zol.com.cn',
        'sourceUrl':{
                'http://desk.zol.com.cn/dongwu/1.html':12,
                'http://sj.zol.com.cn/bizhi/dongwu/1.html':5,
            },
        'urlPattern':'((http://desk.zol.com.cn/bizhi/\d+_\d+_\d+.html)|(http://sj.zol.com.cn/bizhi/detail_\d+_\d+.html))',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"div", "class":["photo-list-box"]},
        'myposPattern': {"tag":"div", "class":["location"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        #'detailFenyePattern':['.html', '_%d.html'],
        'textXpath':'//*[@id="titleName"]/text()',
        'imgReplace':[['s144x90','s960x600']],
        'isAlbum':1
    },

    'pp.163.com':{
        'category':'动物',
        'domain':'pp.163.com',
        'sourceUrl':{
                'http://pp.163.com/pp/#p=20&c=-1&m=3&page=1':500,
            },
        'urlPattern':'http://pp.163.com/.*?/pp/\d+.html',
        'fenyePattern':['page=1', 'page=%d'],
        'bodyPattern':{"tag":"div", "id":["J-picsContainer"]},
        'myposPattern': {"tag":"p", "class":["m-crumb"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'textPattern':{"tag":"h2", "class":["picset-title"]},
        'imgUrlPattern':'http.*?\.(jpg|jpeg|gif|JPG|png)',
        'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },
    
    'photo.pclady.com.cn':{
        'category':'动物',
        'domain':'photo.pclady.com.cn',
        'sourceUrl':{
                'http://photo.pclady.com.cn/cate/1327/1.html':92,
            },
        'urlPattern':'http://photo.pclady.com.cn/pic/\d+.html',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"div", "class":["pic-scroll"]},
        'myposPattern': {"tag":"div", "class":["guide"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'textPattern':{"tag":"span", "class":["pic-txt"]},
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'detailFenyePattern':['.html', '_%d.html'],
        'imgReplace':[['_small','']],
        'isAlbum':1
    },


    'win4000.com':{
        'category':'动物',
        'domain':'win4000.com',
        'sourceUrl':{
                'http://www.win4000.com/wallpaper_206_0_0_1.html':148,
                'http://www.win4000.com/mobile_2355_0_0_1.html':5,
            },
        'urlPattern':'http://www.win4000.com/wallpaper_detail_\d+.html',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"div", "class":["Bigimg","paper-down"]},
        'myposPattern': {"tag":"div", "class":["mei-location"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        #'textPattern':{"tag":"dd", "class":["clearfix"]},
        'textXpath':'//div[@class="ptitle"]/h1/text()',
        'imgUrlPattern':ur'http://pic1.*\.(jpg|jpeg|gif|JPG|png)',
        #'imgReplace':[['','']],
        'isAlbum':1
    },
    
   'meinvtag.win4000.com':{
        'category':'动物',
        'domain':'meinvtag.win4000.com',
        'sourceUrl':{
                'http://www.win4000.com/meinvtag54_1.html':7,
            },
        'urlPattern':'http://www.win4000.com/meinv\d+.html',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"ul", "class":["scroll-img"]},
        'myposPattern': {"tag":"div", "class":["mei-location"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'textXpath':'//div[@class="where clearfix"]/h1/text()',
        'imgUrlPattern':ur'http://pic1.*\.(jpg|jpeg|gif|JPG|png)',
        'imgReplace':[['_100.jpg','']],
        'isAlbum':1
    },     


    'b5.hellowallpaper.com':{
        'category':'动物',
        'domain':'b5.hellowallpaper.com',
        'sourceUrl':{
                'http://b5.hellowallpaper.com/animal_001.html':14,
            },
        'urlPattern':'http://b5.hellowallpaper.com/animal_.*?--.*?-\d+x\d+.html',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"div", "id":["imgsmallnormal"]},
        'myposPattern': {"tag":"div", "id":["mainrightlink"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'textPattern':{"tag":"div", "id":["mainrighttitle"]},
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'detailFenyePattern':['.html', '_%d.html'],
        'imgReplace':[['review-s-',''],['.jpg', '-1280x1024.jpg']],
        'isAlbum':1 
    },
    
     
    'sc.jb51.net':{
        'category':'动物',
        'domain':'sc.jb51.net',
        'sourceUrl':{
                'http://sc.jb51.net/picture/animal/list_37_1.html':110,
                'http://sc.jb51.net/picture/animal/dog/list_204_1.html':20,
                'http://sc.jb51.net/picture/animal/cat/list_209_1.html':8,
            },
        'urlPattern':'http://sc.jb51.net/picture/animal/.*?/\d+.htm',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"div", "class":["content-b"]},
        'myposPattern': {"tag":"div", "class":["pos"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        #'textPattern':{"tag":"dd", "class":["title"]},
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'detailFenyePattern':['.html', '_%d.html'],
        'textXpath':'//div[@class="title"]/h1/text()',
        #'imgReplace':[['92x92','']],
        'isAlbum':1
    },

    'sucaibar.com':{
        'category':'动物',
        'domain':'sucaibar.com',
        'sourceUrl':{
                'http://www.sucaibar.com/image/dongwu/index.html':8,
            },
        'urlPattern':'http://www.sucaibar.com/image/\d+.html',
        'fenyePattern':['.html', '_%d.html'],
        'detailFenyePattern':['.html', '_%d.html'],
        'titleXpath':'//h1/text()',
        'imgXpath':'//div[@class="l_effect_img_mid"]/a/img/@src',
        'timeXpath':'',
        'contentXpath':'//div[@class="tjms"]/text()',
        'myposXpath':'//p[@class="location"]/a/text()',
        'detailFyXpath':'//span[@class="num"]/text()',
        'isAlbum':2
    },

    'pic.jiachong.net':{
        'category':'动物',
        'domain':'pic.jiachong.net',
        'sourceUrl':{
                'http://pic.jiachong.net/dwtp/quan/list_98_1.html':31,
                'http://pic.jiachong.net/dwtp/maomi/list_99_1.html':18,
                'http://pic.jiachong.net/dwtp/yu/list_100_1.html':16,
                'http://pic.jiachong.net/dwtp/niao/list_104_1.html':23,
                'http://pic.jiachong.net/dwtp/houzi/list_101_1.html':10,
                'http://pic.jiachong.net/dwtp/konglong/list_102_1.html':4,
                'http://pic.jiachong.net/dwtp/she/list_103_1.html':16,
                'http://pic.jiachong.net/dwtp/ysdw/list_105_1.html':39,
            },
        'urlPattern':'http://pic.jiachong.net/dwtp/.*?/\d+.html',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"div", "class":["artbody"]},
        'myposPattern': {"tag":"div", "class":["position"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'textXpath':'//div[@class="art-top"]/h1/text()',
        'isAlbum':1,
    },

}
