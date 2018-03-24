#encoding:utf-8

webInfo = {
    'photo.pchouse.com.cn':{
	    'category':'家装',
	    'domain':'photo.pchouse.com.cn',
	    'sourceUrl':{
		    'http://photo.pchouse.com.cn/p1.html':1413,
		},
	    'sourcePattern':'http://photo.pchouse.com.cn/photo/\d+.html',
	    'urlPattern':'http://photo.pchouse.com.cn/groupList/\d+.html',
	    'fenyePattern':['1.html', '%d.html'],
	    'bodyPattern':{"tag":"div", "class":["galCon"]},
	    'myposPattern': {"tag":"div", "class":["gray1"]},
	    'imgPattern':ur'(?is)(<img.*?>)',
	    'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
	    'isAlbum':1
	},

    'tugou.com':{
	    'category':'家装',
	    'domain':'tugou.com',
	    'sourceUrl':{
		    'http://www.tugou.com/jy/yq/p_1/':34,
                    'http://www.tugou.com/jy/ys/p_1/':36,
                    'http://www.tugou.com/jy/yf/p_1/':43,
		},
	    'urlPattern':'http://www.tugou.com/.*/\d+.html',
	    'fenyePattern':['p_1', 'p_%d'],
	    'bodyPattern':{"tag":"div", "class":["content"]},
	    'myposPattern': {"tag":"div", "class":["crumbs"]},
	    'textPattern': {"tag":"div", "class":["content"]},
	    'imgPattern':ur'(?is)(<img.*?>)',
	    'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
	    'isAlbum':1
	},

    'tu.tugou.com':{
	    'category':'家装',
	    'domain':'tu.tugou.com',
	    'sourceUrl':{
                    'http://meitu.tugou.com/case/p_1/':57,
                    'http://meitu.tugou.com/pic/p_1/':1583,
                    'http://www.tugou.com/realcase/p_1/':4,
		},
	    'urlPattern':'.*tugou.com/.*\d+.html',
	    'fenyePattern':['p_1', 'p_%d'],
	    'bodyPattern':{"tag":"figure", "class":["pd-c-item", "bigpic-img"]},
	    'myposPattern': {"tag":"div", "class":["crumbs"]},
	    'textPattern': {"tag":"div", "class":["infotxt"]},
	    'imgPattern':ur'(?is)(<img.*?>)',
	    'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
	    'isAlbum':1
	},


    '3lian.com':{
        'category':'家装', 
        'domain':'3lian.com', 
        'sourceUrl':{
                'http://www.3lian.com/gif/more/22/':26,
                'http://www.3lian.com/show/s113/':78,
                'http://www.3lian.com/gif/more/10/':26,
            },
        'bodyPattern':{"tag":"div", "class":["article", "arc_pag"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'urlPattern':'http://www.3lian.com/(gif|show)/.*\d+.html',
	'myposPattern': {"tag":"div", "class":["adress"]},
	'textXpath': "//h1/text()",
        'fenyePattern':['', 'index_%d.html'],
        'detailFenyePattern':['.html','_%d.html'],
        'isAlbum':1
    },

    'tuku.cn':{
        'category':'家装', 
        'domain':'tuku.cn', 
        'sourceUrl':{
                'http://www.tuku.cn/aclass.aspx?id=5&Page=1':5,
            },
        'urlPattern':'http://www.tuku.cn/class.aspx\?typeid=\d+',
        'bodyPattern':{"tag":"from", "id":["form1"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'fenyePattern':['Page=1','Page=%d'],
        'imgUrlPattern':ur'http://image5.tuku.cn/pic/.*/s\d+.(jpg|jpeg)',
        'detailFenyePattern':['','&Page=%d'],
        'imgReplace': [['/s0', '/0'], ['/s1', '/1'], ['/s2', '/2'], ['/s3', '/3'], ['/s4', '/4'], ['/s5', '/5']],
        'isAlbum':1
        },

    'sc115.com':{
        'category':'家装', 
        'domain':'sc115.com', 
        'sourceUrl':{
            'http://www.sc115.com/tupian/jianzhu/index.html':105,
        },
        'bodyPattern':{"tag":"div", "class":["content","preview"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'urlPattern':'http://www.sc115.com/.{0,30}/\d+.html',
        'textXpath': '//h2[@class="arc_tag"]/a/text()',
        'myposXpath': '//div[@class="path"]/a/text()',
        'fenyePattern':['.html','_%d.html'],
        'isAlbum':1
    },
    'sj33.cn':{
        'category':'家装', 
        'domain':'sj33.cn', 
        'sourceUrl':{
            'http://www.sj33.cn/architecture/slsj/P1.html':119,
        },
        'bodyPattern':{"tag":"div", "class":["artcon"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'urlPattern':'http://www.sj33.cn/.*/\d+/\d+.html',
        'textXpath': '//h1/text()',
        'myposXpath': '//div[@id="loat6"]/a/text()',
        'fenyePattern':['P1','P%d'],
        'isAlbum':1
    },

    'pic.10huan.com':{
        'category':'家装', 
        'domain':'pic.10huan.com', 
        'sourceUrl':{
            'http://pic.10huan.com/listinfo-3-0.html':161,
            'http://pic.10huan.com/listinfo-1-0.html':3135,
            'http://pic.10huan.com/listinfo-2-0.html':600,
        },
        'urlPattern':'http://pic.10huan.com/.*/\d+_\d+/\d+.html',
        'fenyePattern':['0.html','%d.html'],
        'titleXpath':'//h1/font/text()',
        'imgXpath':'//td[@id="text"]/img/@src',
        'contentXpath':'//div[@class="soft"]/text()[1]',
        'timeXpath':'//td[@class="info_text"]/text()',
        'myposXpath':'',
        'isAlbum':0
    },

    'zxzhijia.com':{
        'category':'家装', 
        'domain':'zxzhijia.com', 
        'sourceUrl':{
            'http://www.zxzhijia.com/CaseOne/photolist.html?&p=1':2473,
        },
        'bodyPattern':{"tag":"div", "class":["small_img_list"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.{0,100}(jpg|jpeg|png)',
        'urlPattern':'http://www.zxzhijia.com/CaseOne/meitu/\d+.html',
        'textXpath': '//h1/text()',
        'myposXpath': '//p[@class="xgt_dh"]/a/text()',
        'fenyePattern':['p=1','p=%d'],
        'isAlbum':1
    },

    'shejibao.com':{
        'category':'家装', 
        'domain':'shejibao.com', 
        'sourceUrl':{
            'http://www.shejibao.com/list/28_0_0_0_0.html':1113
        },
        'urlPattern':'http://www.shejibao.com/content/\d+.html',
        'fenyePattern':['0.html','%d.html'],
        'titleXpath':'//h1/text()',
        'imgXpath':'//p[@class="imgzoom"]/img/@src',
        'contentXpath':'//div[@class="content"]/figure/figcaption/a/text()',
        'timeXpath':'//section[@id="bread"]/p/a/text()',
        'myposXpath':'',
        'isAlbum':0
    },

    'ddove.com':{
        'category':'家装', 
        'domain':'ddove.com', 
        'sourceUrl':{
            'http://www.ddove.com/data/?clsid=128&k=&sort=0&ori=0&sale=0&ps=&pa=&page=1':528
        },
        'bodyPattern':{"tag":"div", "class":["thumbmaxbox"]},
        'urlPattern':'http://www.ddove.com/htmldatanew/\d+/.*.html',
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'textXpath': '//div[@class="content"]/text()',
        'fenyePattern':['page=1','page=%d'],
        'isAlbum':1
    },

    'zixun.jia.com':{
	'category':'家装',
	'domain':'zixun.jia.com',
	'sourceUrl':{
		'http://zixun.jia.com/alist/38/p1/':171,
		'http://zixun.jia.com/alist/34/p1/':145,
		'http://zixun.jia.com/alist/36/p1/':48,
	    },
	'urlPattern':'http://zixun.jia.com/article/\d+.html',
	'fenyePattern':['p1', 'p%d'],
	'bodyPattern':{"tag":"div", "class":["ind_details"]},
	'myposPattern': {"tag":"div", "class":["crumbs"]},
	'imgPattern':ur'(?is)(<img.*?>)',
	'imgUrlPattern':'http.*?\.(jpg|jpeg|gif|JPG|png)',
        'urlReplace':[['.html','_all.html']],
	'detailFenyePattern':['.html', '_%d.html'],
	'textPattern':{"tag":"p", "class":["ind_txt"]},
	'isAlbum':1
    },

}

