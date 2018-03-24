#encoding:utf-8
webInfo = {
    '7kk.com':{
        'category':'娱乐', 
        'domain':'7kk.com', 
        'sourceUrl':{
                'http://www.7kk.com/renwu/nvmingxing/new----1.html':0,
                'http://www.7kk.com/renwu/nanmingxing/new----1.html':0,
                'http://www.7kk.com/renwu/tushuobagua/new----1.html':0,
            },
        'urlPattern':'http://www.7kk.com/album/photos/\d+.html|http://www.7kk.com/picture/\d+.html',
        'bodyPattern':{"tag":"div", "id":["container", "focus"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'myposPattern': {"tag":"div", "class":["filterbar"]}, 
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'fenyePattern':['----1','----%d'],
        'isAlbum':1
    },

    'bz55.com':{
        'category':'娱乐', 
        'domain':'bz55.com', 
        'sourceUrl':{
                        'http://www.bz55.com/shoujibizhi/mingxingsjbz/list_30_1.html':207,
                        'http://www.bz55.com/shoujibizhi/movesjbz/list_31_1.html':69,
                        'http://www.bz55.com/yingshibizhi/list_45_1.html':272,
                        'http://www.bz55.com/mingxingbizhi/list_5_1.html':410,
                    },
        'urlPattern':'http://www.bz55.com/zhiwubizhi/\d+/\d+/\d+.html',
        'fenyePattern':['_1.html', '_%d.html'],
        'bodyPattern':{"tag":"div", "class":["imglist"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'myposXpath':'//div[@class="article_position"]/a/text()',
        'textXpath':'//div[@class="bizhic"]/a/text()',
        'fenyePattern':['1.html','%d.html'],
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|png)',
        'isAlbum':1
    },



    '50tu.com':{
        'category':'娱乐', 
        'domain':'50tu.com', 
        'sourceUrl':{
                'http://50tu.com/nvxing/dalu/index.html':62,
                'http://50tu.com/nvxing/oumei/index.html':30,
                'http://50tu.com/nvxing/rihan/index.html':41,
                'http://50tu.com/nvxing/xiezhen/index.html':236,
                'http://50tu.com/nvxing/nenmo/index.html':70,
                'http://50tu.com/feizhuliu/mingxing/index.html':444,
            },
        'urlPattern':'http://50tu.com/.*/.{0,30}/\d+-\d+-\d+/\d+.html',
        'fenyePattern':['.html','_%d.html'],
        'imgReplace':[['small','']],
        'imgPattern':ur'(?is)(<img.*?>)',
        'bodyPattern':{"tag":"div", "class":["album_wrap"]},
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'titleXpath':'//h1/text()',
        'imgXpath':'//div[@class="wrap"]/img/@src',
        'myposXpath':'//div[@class="palce"]/a/text()',
        'detailFyXpath':'//h1/text()',
        'isAlbum':1
        },

    'ivsky.com':{
        'category':'娱乐', 
        'domain':'ivsky.com', 
        'sourceUrl':{
                'http://www.ivsky.com/bizhi/nvxing/index_1.html':100,
                'http://www.ivsky.com/bizhi/nanxing/index_1.html':51,
            },
        'urlPattern':'http://www.ivsky.com/.{0,30}/.{0,60}/',
        'bodyPattern':{"tag":"ul", "class":["pli", "il", "ali"]},
        'imgPattern':ur'(?is)(<img.*?>)',
         'myposPattern': {"tag":"div", "class":["pos"]}, 
        'fenyePattern':['_1.html','_%d.html'],
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'textPattern': {"tag":"div", "class":["al_info"]}, 
        'imgReplace':[['/t/','/pre/']],
        'isAlbum':1
        },

   'm1ok.com':{
        'category':'娱乐', 
        'domain':'m1ok.com', 
        'sourceUrl':{
                        'http://www.m1ok.com/desk/deskmx1.shtm':52,
                        'http://www.m1ok.com/desk/deskys1.shtm':27,
                    },
        'urlPattern':'http://www.m1ok.com/Article/\d+/\d+/index.htm',
        'fenyePattern':['1.shtm', '%d.shtm'],
        'bodyPattern':{"tag":"div", "class":["tpjPicshowListCC"]},
        'imgPattern':ur'src=.*',
        'imgUrlPattern':ur'http.*.(jpg|jpeg|png)',
        'imgReplace':[['m1.jpg','.jpg'], ['m.jpg','.jpg']],
        'isAlbum':1
    },

   'zhuoku.com':{
        'category':'娱乐', 
        'domain':'zhuoku.com', 
        'sourceUrl':{
                        'http://www.zhuoku.com/zhuomianbizhi/star/index-1.htm':108,
                        'http://www.zhuoku.com/zhuomianbizhi/movie/index-1.htm':35,
                    },
        'urlPattern':'http://www.zhuoku.com/.*/.*/\d+.htm',
        'myposXpath':'//div[@class="nav"]/a/text()',
        'textXpath':'//div[@class="bizhic"]/a/text()',
        'fenyePattern':['1.htm', '%d.htm'],
        'bodyPattern':{"tag":"div", "class":["bizhiin"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.*.(jpg|jpeg|png)',
        'imgReplace':[['thumbs/tn_', '']],
        'isAlbum':1
    },



    '99bz.net':{
        'category':'娱乐', 
        'domain':'99bz.net', 
        'sourceUrl':{
                        'http://www.99bz.net/bz/mingxingbizhi_1.html':50,
                        'http://www.99bz.net/bz/dianshijubizhi_1.html':33,
                        'http://www.99bz.net/bz/dianyingbizhi_1.html':15,
                    },
        'urlPattern':'http://www.99bz.net/bz/\d+.html',
        'fenyePattern':['_1.html', '_%d.html'],
        'bodyPattern':{"tag":"div", "class":["pp","hh"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'fenyePattern':['1.html','%d.html'],
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|png)',
        'detailFenyePattern':['.html', '_%d.html'],
        'myposPattern': {"tag":"div", "class":["category-nav"]}, 
        'isAlbum':1
    },

    'warting.com':{
        'category':'娱乐', 
        'domain':'warting.com', 
        'sourceUrl':{
                'http://www.warting.com/wallpaper/movie/list_1.html':13,
                'http://www.warting.com/wallpaper/star/list_1.html':32,
            },
        'urlPattern':'http://www.warting.com/(wallpaper|gallery)/\d+/\d+.html',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"ul", "class":["picshow_first", "picshow_third"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'myposPattern': {"tag":"div", "class":["location"]}, 
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'textPattern':{"tag":"div", "class":["article_bd"]},
        'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },


    'zol.com.cn':{
        'category':'娱乐', 
        'domain':'zol.com.cn', 
        'sourceUrl':{
                'http://desk.zol.com.cn/mingxing/1.html':40,
                'http://desk.zol.com.cn/yingshi/1.html':22,
                'http://sj.zol.com.cn/bizhi/mingxing/1.html':30,
                'http://sj.zol.com.cn/bizhi/yingshi/1.html':9,
            },
        'urlPattern':'zol.com.cn/.*_\d+_\d+.html',
        'myposPattern': {"tag":"div", "class":["location"]}, 
        'bodyPattern':{"tag":"div", "class":["photo-set-list"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'fenyePattern':['1.html','%d.html'],
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'imgReplace':[['/t_s144x90','/t_s960x600']],
        'isAlbum':1
        },

    'wed114.cn':{
        'category':'娱乐', 
        'domain':'wed114.cn', 
        'sourceUrl':{
                'http://www.wed114.cn/jiehun/tuku/mingxingxiezhen/list_106_1.html':63,
                'http://www.wed114.cn/jiehun/yule/list_118_1.html':611,
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

    'niutuku.com':{
        'category':'娱乐', 
        'domain':'niutuku.com', 
        'sourceUrl':{
                'http://niutuku.com/bizhi/4/index.shtml':126,
            },
        'urlPattern':'http://niutuku.com/bizhi/\d+.shtml',
        'bodyPattern':{"tag":"dl", "id":["container"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'myposPattern': {"tag":"div", "class":["place"]}, 
        'fenyePattern':['.shtml','_%d.shtml'],
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'imgReplace':[['190','960']],
        'isAlbum':1
    },

    'news.shangqiuw.com':{
        'category':'娱乐', 
        'domain':'news.shangqiuw.com', 
        'sourceUrl':{
                'http://news.shangqiuw.com/newslist-0-10-aa-p1.html':2451,
            },
        'urlPattern':'http://news.shangqiuw.com/newsshow-\d+.html',
        'bodyPattern':{"tag":"div", "class":["nr"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'myposPattern': {"tag":"div", "class":["break"]}, 
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'fenyePattern':['p1.html','p%d.html'],
        'isAlbum':1
    },

    'meixiuwang.com':{
        'category':'娱乐', 
        'domain':'meixiuwang.com', 
        'sourceUrl':{
                'http://www.meixiuwang.com/mingxing/list_12_1.html':254,
            },
        'urlPattern':'http://www.meixiuwang.com/mingxing/\d+/\d+/\d+.html',
        'bodyPattern':{"tag":"div", "class":["content"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'myposPattern': {"tag":"div", "class":["postion"]}, 
        'detailFenyePattern':['.html','_%d.html'],
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'fenyePattern':['1.html','%d.html'],

        'isAlbum':1
    },

    'ciligod.com':{
        'category':'娱乐', 
        'domain':'ciligod.com', 
        'sourceUrl':{
                'http://www.ciligod.com/mx/index.html':428,
            },
        'urlPattern':'http://www.ciligod.com/mx/\d+.html',
        'bodyPattern':{"tag":"div", "class":["poster"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'myposPattern': {"tag":"div", "class":["place"]}, 
        'textPattern': {"tag":"div", "class":["intro"]}, 
        'detailFenyePattern':['.html','_%d.html'],
        'publishTimeXpath':'',
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'fenyePattern':['.html','_%d.html'],
        'isAlbum':1
    },

    '5857.com':{
        'category':'娱乐', 
        'domain':'5857.com', 
        'sourceUrl':{
                'http://www.5857.com/list-9-0-3374-0-0-0-1.html':97,
                'http://www.5857.com/list-9-0-3366-0-0-0-1.html':127,
            },
        'urlPattern':'http://www.5857.com/.*/\d+.html',
        'bodyPattern':{"tag":"a", "class":["photo-a"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'detailFenyePattern':['.html','_%d.html'],
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'myposPattern': {"tag":"div", "class":["position"]}, 
        'textPattern': {"tag":"div", "class":["con-tags"]}, 
        'fenyePattern':['1.html','%d.html'],
        'isAlbum':1
    },

    'xiazaizhijia.com':{
        'category':'娱乐', 
        'domain':'xiazaizhijia.com', 
        'sourceUrl':{
                'http://www.xiazaizhijia.com/bizhi/ys/':883,
            },
        'urlPattern':'http://www.xiazaizhijia.com/bizhi/\d+.html',
        'titleXpath':'//div[@class="main-title"]/h1/text()',
        'imgXpath':'//div[@class="pic"]/img/@src',
        'contentXpath':'//div[@class="key-list"]/a/text()',
        'fenyePattern':['', '226_%d.html'],
        'timeXpath':'',
        'myposXpath':'//div[@class="bread-nav"]/a/text()',
        'isAlbum':0
    },
    '4j4j.cn':{
        'category':'娱乐', 
        'domain':'4j4j.cn', 
        'sourceUrl':{
                'http://www.4j4j.cn/sjbz/f-cate75_1.html':59,
                'http://www.4j4j.cn/zmbz/f-cate55_1.html':18,
                'http://www.4j4j.cn/zmbz/f-cate54_1.html':6,
                'http://www.4j4j.cn/zmbz/f-cate53_1.html':4,
                'http://www.4j4j.cn/zmbz/f-cate51_1.html':26,
                'http://www.4j4j.cn/mxtp/index_1.html':24,
            },
        'urlPattern':'http://www.4j4j.cn/.*/\d+.html',
        'bodyPattern':{"tag":"ul", "id":["clearfix"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http://pic.4j4j.cn/upload/star/\d+_\d+/\d+.(jpg|jpeg|gif|JPG|png)|http://pic.4j4j.cn/upload/pic/\d+/[A-Za-z0-9]+.(jpg|jpeg|gif|JPG|png)',
        'myposPattern': {"tag":"div", "class":["main_nav"]}, 
        'fenyePattern':['1.html','%d.html'],
        'isAlbum':1
    },

    'mingxing.com':{
        'category':'娱乐', 
        'domain':'mingxing.com', 
        'sourceUrl':{
                'http://tuku.mingxing.com/mxxz/':100,
                'http://www.mingxing.com/tuku/ysjz/':100,
                'http://www.mingxing.com/tuku/shz/':100,
                'http://www.mingxing.com/tuku/hdxz/':100,
            },
        'urlPattern':'http://www.mingxing.com/tuku/\d+/\d+/',
        'bodyPattern':{"div":"ul", "class":["img_box"]},
        'detailFenyePattern':['','%d.html'],
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'myposPattern': {"tag":"div", "class":["pictop"]}, 
        'fenyePattern':['','list_%d.html'],
        'isAlbum':1
    },

    'enterdesk.com':{
        'category':'娱乐', 
        'domain':'enterdesk.com', 
        'sourceUrl':{
                'http://www.enterdesk.com/zhuomianbizhi/mingxingbizhi/':39,
            },
        'urlPattern':'http://www.enterdesk.com/bizhi/\d+.html',
        'bodyPattern':{"div":"ul", "class":["arc_sximgs"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.{0,60}.(jpg|jpeg|gif|JPG|png)',
        'myposPattern': {"tag":"div", "class":["thislocation"]}, 
        'fenyePattern':['','%d.html'],
        'imgReplace':[['.200.150.jpg','']],
        'isAlbum':1
    },
    'zybus.com':{
        'category':'娱乐', 
        'domain':'zybus.com', 
        'sourceUrl':{
                'http://www.zybus.com/yirentuku/list_213_1.html':18,
            },
        'urlPattern':'http://www.zybus.com/yirentuku/\d+.html',
        'bodyPattern':{"tag":"div", "class":["imgList"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'myposPattern': {"tag":"div", "class":["position"]}, 
        'fenyePattern':['1.html','%d.html'],
        'isAlbum':1
    },

    'photo.pclady.com.cn':{
        'category':'娱乐', 
        'domain':'photo.pclady.com.cn', 
        'sourceUrl':{
                'http://photo.pclady.com.cn/cate/801/1.html':46,
                'http://photo.pclady.com.cn/cate/1323/1.html':15,
                'http://photo.pclady.com.cn/cate/1321/1.html':30,
            },
        'urlPattern':'http://photo.pclady.com.cn/pic/\d+.html',
        'bodyPattern':{"div":"div", "class":["pic-scroll"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'myposPattern': {"tag":"div", "class":["guide"]}, 
        'fenyePattern':['1.html','%d.html'],
        'imgReplace':[['_small','']],
        'isAlbum':1
    },


    'bzdao.com':{
        'category':'娱乐', 
        'domain':'bzdao.com', 
        'sourceUrl':{
                'http://www.bzdao.com/class/mxxz/Index-1.shtml':95,
                'http://www.bzdao.com/class/ysbz/Index-1.shtml':37,
            },
        'urlPattern':'http://www.bzdao.com/.*/Index\d+-\d+.shtml',
        'fenyePattern':['1.shtml', '%d.shtml'],
        'detailFenyePattern':['1.shtml', '%d.shtml'],
        'bodyPattern':{"tag":"div", "class":["rbox"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'myposPattern': {"tag":"div", "class":["place"]}, 
        'imgReplace':[['/s','/']],
        'isAlbum':1
    },

    'k123.com':{
            'category':'娱乐',
            'domain':'p.ik123.com',
            'sourceUrl':{
                    'http://p.ik123.com/mingxing/list_1.html':209,
                },
            'urlPattern':'http://p.ik123.com/bizhi/\d+.html',
            'fenyePattern':['1.html', '%d.html'],
            'bodyPattern':{"tag":"div", "id":["gui_left"]},
            'myposPattern': {"tag":"div", "class":["daohang"]},
            'imgPattern':ur'(?is)(<img.*?>)',
            'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
            'detailFenyePattern':['1.html', '%d.html'],
            'isAlbum':1
    },

    'bz.putaojiayuan.com':{
            'category':'娱乐',
            'domain':'bz.putaojiayuan.com',
            'sourceUrl':{
                    'http://bz.putaojiayuan.com/NvXingBiZhi/index_1.html':94,
                    'http://bz.putaojiayuan.com/NanXingBiZhi/index_1.html':22,
                    'http://bz.putaojiayuan.com/DianYingBiZhi/index_1.html':86,
                },
            'urlPattern':'http://bz.putaojiayuan.com/(NvXingBiZhi|NanXingBiZhi|DianYingBiZhi)/v\d+/',
            'fenyePattern':['1.html', '%d.html'],
            'bodyPattern':{"tag":"div", "class":["w992"]},
            'imgReplace':[['thumb','med']],
            'myposPattern': {"tag":"p", "class":["current"]},
            'imgPattern':ur'(?is)(<img.*?>)',
            'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
            'detailFenyePattern':['', 'index_%d.html'],
            'isAlbum':1
    },  
    
    'wmtp.net':{
            'category':'娱乐',
            'domain':'wmtp.net',
            'sourceUrl':{
                    'http://wmtp.net/tupian/mingxing/page/1':30,
             },
            'urlPattern':'http://wmtp.net/\d+',
            'fenyePattern':['/1', '/%d'],
            'bodyPattern':{"tag":"div", "class":["content-c"]},
            'myposPattern': {"tag":"span", "class":["post-tags"]},
            'imgPattern':ur'(?is)(<img.*?>)',
            'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
	        'detailFenyePattern':['.html', '_%d.html'],
            'isAlbum':1
    },
    
    'tupian.163jiankang.com':{
            'category':'娱乐',
            'domain':'tupian.163jiankang.com',
            'sourceUrl':{
                   'http://tupian.163jiankang.com/yule/1066-1.html':15,
                   'http://tupian.163jiankang.com/star/99-1.html':31,
            },
                'urlPattern':'http://tupian.163jiankang.com/(yule|star)/\d+.html',
            'fenyePattern':['1.html', '%d.html'],
            'bodyPattern':{"tag":"div", "id":["bigpic_all"]},
            'textPattern':{"tag":"div", "class":["intro"]},
            'myposPattern': {"tag":"div", "class":["header02"]},
            'imgPattern':ur'(?is)(<img.*?>)',
            'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
            'detailFenyePattern':['.html', '_%d.html'],
            'isAlbum':1
    },

    'haobizhi.com':{
            'category':'娱乐',
            'domain':'haobizhi.com',
            'sourceUrl':{
                    'http://www.haobizhi.com/yingshi/1.htm':134,
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
    
    'bizhi.tuku.com':{
            'category':'娱乐',
            'domain':'bizhi.tuku.com',
            'sourceUrl':{
                    'http://bizhi.tuku.com/': 15,
            },
            'urlPattern':'http://bizhi.tuku.com/((.*/\d+/\d+.html)|(/\d+/\d+.html))',
            'fenyePattern':['com/', 'com/index_%d.html'],
            'bodyPattern':{"tag":"div", "class":["photo"]},
            'myposPattern': {"tag":"div", "class":["location-nav"]},
            'imgReplace':[['smallbizhi/','']],
            'imgPattern':ur'(?is)(<img.*?>)',
            'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
            'detailFenyePattern':['1.html', '%d.html'],
            'isAlbum':1
    },    

    'bizhi.4493.com':{
            'category':'娱乐',
            'domain':'bizhi.4493.com',
            'sourceUrl':{
                    'http://bizhi.4493.com/mingxing/index-1.html':178,
             },
            'urlPattern':'http://bizhi.4493.com/image/\d+.html',
            'fenyePattern':['1.html', '%d.html'],
            'bodyPattern':{"tag":"div", "class":["picbox"]},
            'myposPattern': {"tag":"div", "class":["titinfo"]},
            'imgPattern':ur'(?is)(<img.*?>)',
            'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
	        'detailFenyePattern':['1.html', '%d.html'],
            'isAlbum':1
     },

    'deskcar.com':{
            'category':'娱乐',
            'domain':'deskcar.com',
            'sourceUrl':{
                    'http://www.deskcar.com/list/1/1.shtml':95,
                    'http://www.deskcar.com/list/3/1.shtml':31,
             },
            'urlPattern':'http://www.deskcar.com/html/\d+/list_\d+.shtml',
            'fenyePattern':['1.shtml', '%d.shtml'],
            'bodyPattern':{"tag":"div", "class":["bd_recommend"]},
            'imgReplace':[['TN_','']],
            'imgPattern':ur'(?is)(<img.*?>)',
            'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png|PNG)',
	        'detailFenyePattern':['1.shtml', '%d.shtml'],
            'isAlbum':1
     },

    
    'photo.ichang8.com':{
            'category':'娱乐',
            'domain':'photo.ichang8.com',
            'sourceUrl':{
                    'http://photo.ichang8.com/zhongguo-p-1.html':11,
                    'http://photo.ichang8.com/rihan-p-1.html':2,
                    'http://photo.ichang8.com/oumei-p-1.html':1,
                    'http://photo.ichang8.com/juzhao-p-1.html':1,
                    'http://photo.ichang8.com/diannao-p-1.html':12,
                    'http://photo.ichang8.com/shouji-p-1.html':3,
            },
            'urlPattern':'http://photo.ichang8.com/(zhongguo|rihan|zongyi|diannao|shouji)-\d+.html',
            'fenyePattern':['1.html', '%d.html'],
            'bodyPattern':{"tag":"div", "class":["img_box"]},
            'myposPattern': {"tag":"div", "class":["sub_nav"]},
            'imgPattern':ur'(?is)(<img.*?>)',
            'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
            'detailFenyePattern':['.html', '-p-%d.html'],
            'isAlbum':1
     },

     'mxmop.com':{
            'category':'娱乐',
            'domain':'mxmop.com',
            'sourceUrl':{
                    'http://www.mxmop.com/mingxing/page/1/':609,
                    'http://www.mxmop.com/dianying/page/1/':307,
            },
            'urlPattern':'http://www.mxmop.com/(dianying|mingxing)/\d+.html',
            'fenyePattern':['/1/', '/%d/'],
            'bodyPattern':{"tag":"div", "id":["itemContainer"]},
            'publishTimeXpath':'//span[@class="content-time"]/text()',
            'textXpath':'//div[@id="container"]/div[2]/p[2]/text()',
            'myposPattern': {"tag":"div", "id":["crumb"]},
            'imgPattern':ur'(?is)(<img.*?>)',
            'imgUrlPattern':'http.*\.(jpg|jpeg|JPG|png)',
            'isAlbum':1
     },

}
