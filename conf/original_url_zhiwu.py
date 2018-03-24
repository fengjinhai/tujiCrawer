#encoding:utf-8
webInfo = {
    'chinaz.com':{
        'category':'植物', 
        'domain':'chinaz.com', 
        'sourceUrl':{'http://sc.chinaz.com/tag_tupian/ZhiWu.html':237},
        'urlPattern':'sc.chinaz.com/tupian/\d+.htm',
        'fenyePattern':['.html', '_%d.html'],
        'titleXpath':'//div[@class="text_wrap"]/h2/a/text()',
        'imgXpath':'//div[@class="imga"]/a/@href',
        'contentXpath':'//div[@class="gjz_tag"]/div[@class="ta_block"]/div[@class="smr"]/text()',
        'timeXpath':'//div[@class="lefts"]/span/em/text()',
        'myposXpath':'//div[@class="dangqian"]/a/text()',
        'isAlbum':0
    },
    'kuoo8.com':{
        'category':'植物', 
        'domain':'kuoo8.com', 
        'sourceUrl':{'http://kuoo8.com/pic/bizhi_flower.html':9},
        'urlPattern':'kuoo8.com/pic/\d+.htm',
        'fenyePattern':['.html', '_%d.html'],
        'titleXpath':'//h1[@class="workTitle"]/span/text()',
        'imgXpath':'//div[@class="imglist"]/a/@href',
        'contentXpath':'',
        'timeXpath':'//div[@class="workLeftTop"]/p[2]/span/text()',
        'myposXpath':'//div[@class="longTop"]/a/text()',
        'isAlbum':0
    },
    'maxitas.com':{
        'category':'植物', 
        'domain':'maxitas.com', 
        'sourceUrl':{'http://www.maxitas.com/huamu/':1},
        'bodyPattern':{"tag":"div", "id":["article"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'urlPattern':'http://www.maxitas.com/huamu/show/\d+/',
        'fenyePattern':'',
        'isAlbum':1
    },
    'wmtp.net':{
        'category':'植物', 
        'domain':'wmtp.net', 
        'sourceUrl':{'http://wmtp.net/?s=%E6%A4%8D%E7%89%A9':2},
        'bodyPattern':{"tag":"div", "id":["content"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'urlPattern':'http://wmtp.net/\d+',
        'fenyePattern':['net/', 'net/page/%d'],
        'isAlbum':1
    },
    '3lian.com':{
        'category':'植物', 
        'domain':'3lian.com', 
        'sourceUrl':{'http://www.3lian.com/gif/more/15/':80},
        'bodyPattern':{"tag":"div", "class":["article", "arc_pag"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'urlPattern':'http://www.3lian.com/gif/\d+/\d+-\d+/.*.html',
        'fenyePattern':['15/', '15/index_%d.html'],
        'detailFenyePattern':['.html','_%d.html'],
        'isAlbum':1
    },
    'yanghua.baike.com':{
        'category':'植物', 
        'domain':'yanghua.baike.com', 
        'sourceUrl':{'http://yanghua.baike.com/category-0.html':35},
        'bodyPattern':{"tag":"div", "class":["nwdiv"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'urlPattern':'http://yanghua.baike.com/article-\d+.html',
        'fenyePattern':['category-0', 'category-0-%d'],
        'isAlbum':1
    },
    'win4000.com':{
        'category':'植物', 
        'domain':'win4000.com', 
        'sourceUrl':{'http://www.win4000.com/wallpaper_209_0_0_1.html':177},
        'urlPattern':'http://www.win4000.com/wallpaper_detail_\d+.html',
        'bodyPattern':{"tag":"ul", "class":["ulBigPic", 'pic-large']},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'fenyePattern':['1.html','%d.html'],
        'isAlbum':1
    },
    'wed114.cn':{
        'category':'植物', 
        'domain':'wed114.cn', 
        'sourceUrl':{'http://www.wed114.cn/jiehun/zhiwu/list_779_1.html':241},
        'urlPattern':'http://www.wed114.cn/jiehun/zhiwu/\d+.html',
        'bodyPattern':{"tag":"div", "class":["substance"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'detailFenyePattern':['.html','_%d.html'],
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'fenyePattern':['1.html','%d.html'],
        'isAlbum':1
    },
    'jb51.net':{
        'category':'植物', 
        'domain':'jb51.net', 
        'sourceUrl':{'http://sc.jb51.net/picture/flower/list_189_1.html':195},
        'urlPattern':'http://sc.jb51.net/picture/flower/.{1,30}/\d+.htm',
        'bodyPattern':{"tag":"div", "class":["content-b"]},
        'myposPattern': {"tag":"div", "class":["pos"]}, 
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'fenyePattern':['1.html','%d.html'],
        'isAlbum':1
    },
    'jj20.com':{
        'category':'植物', 
        'domain':'jj20.com', 
        'sourceUrl':{'http://www.jj20.com/bz/hhzw/list_3_1.html':41},
        'urlPattern':'http://www.jj20.com/bz/hhzw/.{1,20}/\d+.html',
        'bodyPattern':{"tag":"div", "class":["photo"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'fenyePattern':['1.html','%d.html'],
        'detailFenyePattern':['.html','_%d.html'],
        'isAlbum':1
    },
    'bzw315.com':{
        'category':'植物', 
        'domain':'bzw315.com', 
        'sourceUrl':{'http://www.bzw315.com/zx/zhiwu/3/1/':244},
        'urlPattern':'http://www.bzw315.com/zx/.{1,20}/\d+.html',
        'bodyPattern':{"tag":"div", "class":["words"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|JPG|png)',
        'fenyePattern':['/1/','/%d/'],
        'isAlbum':1
    },
    'warting.com':{
        'category':'植物', 
        'domain':'warting.com', 
        'sourceUrl':{'http://www.warting.com/pic/plant/list_1.html':21},
        'urlPattern':'http://www.warting.com/pic/\d+/\d+/\d+.html',
        'bodyPattern':{"tag":"div", "class":["picshow_second"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'fenyePattern':['_1.html','_%d.html'],
        'detailFenyePattern':['.html','_%d.html'],
        'isAlbum':1
    },
    'zhongyixueyuan.com':{
        'category':'植物', 
        'domain':'zhongyixueyuan.com', 
        'sourceUrl':{'http://www.zhongyixueyuan.com/about/zhiwuyao/':1},
        'urlPattern':'http://www.zhongyixueyuan.com/.{1,15}/',
        'bodyPattern':{"tag":"div", "class":["content"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'isAlbum':1
    },
    '7kk.com':{
        'category':'植物', 
        'domain':'7kk.com', 
        'sourceUrl':{
                'http://www.7kk.com/shengwu/shuiguo/new----1':4,
                'http://www.7kk.com/shengwu/shucai/new----1':2,
                'http://www.7kk.com/shengwu/huacaoshumu/new----1':25,
                'http://www.7kk.com/bizhi/zhiwu/new----1':155
            },
        'urlPattern':'http://www.7kk.com/album/photos/\d+.html|http://www.7kk.com/picture/\d+.html',
        'bodyPattern':{"tag":"div", "id":["container", "focus"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'myposPattern': {"tag":"div", "class":["filterbar"]}, 
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'fenyePattern':['----1','----%d'],
        'isAlbum':1
    },
    'qnong.com.cn':{
        'category':'植物', 
        'domain':'qnong.com.cn', 
        'sourceUrl':{
                'http://www.qnong.com.cn/zhongzhi/liangshi/index.html':4,
                'http://www.qnong.com.cn/zhongzhi/shucai/index.html':11,
                'http://www.qnong.com.cn/zhongzhi/shuiguo/index.html':11,
                'http://www.qnong.com.cn/zhongzhi/huahui/index.html':39,
                'http://www.qnong.com.cn/zhongzhi/yaocai/index.html':9,
                'http://www.qnong.com.cn/zhongzhi/chaye/index.html':3
            },
        'urlPattern':'http://www.qnong.com.cn/zhongzhi/.{0,20}/\d+.html',
        'bodyPattern':{"tag":"div", "class":["article"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'fenyePattern':['.html','_%d.html'],
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'isAlbum':1
    },
    'pchome.net':{
        'category':'植物', 
        'domain':'pchome.net', 
        'sourceUrl':{
                'http://download.pchome.net/wallpaper/zhiwu/otherplants/p1/':31,
                'http://download.pchome.net/wallpaper/zhiwu/tulip/p1/':14,
                'http://download.pchome.net/wallpaper/zhiwu/nongye/p1/':3
            },
        'urlPattern':'http://download.pchome.net/wallpaper/info-.*.html',
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'fenyePattern':['p1/', 'p%d/'],
        'detailFenyePattern':['-1-','-%d-'],
        'titleXpath':'//h3/a/text()',
        'imgXpath':'//img[@id="bigImg"]/@src',
        'contentXpath':'',
        'timeXpath':'',
        'myposXpath':'//div[@class="location-nav"]/div/a/text()',
        'detailFyXpath':'//h3/span/text()',
        'isAlbum':2
        },
    '50tu.com':{
        'category':'植物', 
        'domain':'50tu.com', 
        'sourceUrl':{
                'http://50tu.com/bizhi/zhiwu/':11, 
                'http://50tu.com/bizhi/huahui/index.html':9
            },
        'urlPattern':'http://50tu.com/bizhi/.{0,30}/\d+-\d+-\d+/\d+.html',
        'fenyePattern':['.html','_%d.html'],
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'detailFenyePattern':['.html', '_%d.html'],
        'titleXpath':'//h1/text()',
        'imgXpath':'//div[@class="wrap"]/img/@src',
        'contentXpath':'',
        'timeXpath':'',
        'myposXpath':'//div[@class="palce"]/a/text()',
        'detailFyXpath':'//h1/text()',
        'isAlbum':2
        },

    'imagewa.com':{
        'category':'植物', 
        'domain':'imagewa.com', 
        'sourceUrl':{
                'http://imagewa.com/Photo/231/Index.html':16, 
                'http://imagewa.com/Photo/232/Index.html':25
            },
        'urlPattern':'http://imagewa.com/Photo/\d+/\d+.html',
        'fenyePattern':['Index.html','List_%d.html'],
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'titleXpath':'//title/text()',
        'imgXpath':'//div[@id="ImgSize"]/a/img/@src',
        'contentXpath':'//td[@class="Showinfo_tags"]/text()',
        'timeXpath':'',
        'myposXpath':'',
        'isAlbum':0
        },
        'baihuaji.cn':{
            'category':'植物', 
            'domain':'baihuaji.cn', 
            'sourceUrl':{
                    'http://www.baihuaji.cn/news/list?total=106&cid=1&fypage=1':11,
                    'http://www.baihuaji.cn/news/list?total=48&cid=6&fypage=1':5,
                    'http://www.baihuaji.cn/news/list?total=96&cid=3&fypage=1':10,
                    'http://www.baihuaji.cn/news/list?total=142&cid=12&fypage=15':15
                },
            'urlPattern':'http://www.baihuaji.cn/article_\d+.html',
            'bodyPattern':{"tag":"div", "class":["content_main"]},
            'imgPattern':ur'(?is)(<img.*?>)',
            'fenyePattern':['fypage=1','fypage=%d'],
            'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
            'isAlbum':1
            },
        'huaxianer.com':{
            'category':'植物', 
            'domain':'huaxianer.com', 
            'sourceUrl':{
                    'http://www.huaxianer.com/image/list_1_1.html':26,
                    'http://www.huaxianer.com/wiki/list_11_1.html':26,
                    'http://www.huaxianer.com/jishu/list_20_1.html':25,
                    'http://www.huaxianer.com/zhishi/list_46_1.html':13,
                },
            'urlPattern':'http://www.huaxianer.com/.{0,30}/\d+.html',
            'bodyPattern':{"tag":"article", "class":["article-content"]},
            'imgPattern':ur'(?is)(<img.*?>)',
            'fenyePattern':['_1.html','_%d.html'],
            'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
            'isAlbum':1
            },

        'fsbus.com':{
            'category':'植物', 
            'domain':'fsbus.com', 
            'sourceUrl':{
                    'http://tu.fsbus.com/zhiwu/page/1/':14,
                },
            'urlPattern':'http://tu.fsbus.com/zhiwu/\d+.html',
            'bodyPattern':{"tag":"div", "class":["post-content"]},
            'imgPattern':ur'(?is)(<img.*?>)',
            'fenyePattern':['/1/','/%d/'],
            'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
            'isAlbum':1
            },

        'ivsky.com':{
            'category':'植物', 
            'domain':'ivsky.com', 
            'sourceUrl':{
                    'http://www.ivsky.com/bizhi/huahui/index_1.html':15,
                    'http://www.ivsky.com/bizhi/zhiwu/index_1.html':7,
                    'http://www.ivsky.com/tupian/zhiwuhuahui/index_1.html':191,
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

        'zol.com.cn':{
            'category':'植物', 
            'domain':'zol.com.cn', 
            'sourceUrl':{
                    'http://sj.zol.com.cn/bizhi/zhiwu/1.html':14,
                    'http://desk.zol.com.cn/zhiwu/1.html':15,
                    'http://desk.zol.com.cn/zhiwu/p4/1.html':15,
                    'http://desk.zol.com.cn/zhiwu/p3/1.html':2,
                },
            'urlPattern':'http://desk.zol.com.cn/bizhi/\d+_\d+_\d+.html',
            'bodyPattern':{"tag":"div", "class":["photo-set-list"]},
            'imgPattern':ur'(?is)(<img.*?>)',
            'fenyePattern':['1.html','%d.html'],
            'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
            'imgReplace':[['/t_s144x90','/t_s960x600']],
            'isAlbum':1
            },

        'pp.163.com':{
            'category':'植物', 
            'domain':'pp.163.com', 
            'sourceUrl':{
                    'http://shenyang74-126.pp.163.com/pp#p=18&c=-1&m=3&page=1':500,
                },
            'urlPattern':'http://pp.163.com/.*/pp/\d+.html',
            'bodyPattern':{"tag":"div", "id":["J-picsContainer"]},
            'myposPattern': {"tag":"p", "class":["m-crumb"]}, 
            'imgPattern':ur'(?is)(<img.*?>)',
            'fenyePattern':['page=1','page=%d'],
            'imgUrlPattern':ur'http.*\.(jpg|jpeg)',
            'isAlbum':1
            },
        'tuku.cn':{
            'category':'植物', 
        'domain':'tuku.cn', 
        'sourceUrl':{
                'http://www.tuku.cn/wallpapers.aspx?id2=38&Page=1':7,
            },
        'urlPattern':'http://www.tuku.cn/wallpaper_class.aspx\?typeid=\d+',
        'bodyPattern':{"tag":"from", "id":["form1"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'fenyePattern':['Page=1','Page=%d'],
        'imgUrlPattern':ur'http://image5.tuku.cn/pic/wallpaper/zhiwu.*/s\d+.(jpg|jpeg)',
        'imgReplace':[['/s0','/0']],
        'isAlbum':1
        },
    'pp3.cn':{
        'category':'植物', 
        'domain':'pp3.cn', 
        'sourceUrl':{
                'http://www.pp3.cn/html/ptc/cat/zhiwu/list_208_1.html':55,
                'http://www.pp3.cn/html/ptc/cat/huahui/list_226_1.html':11,
            },
        'urlPattern':'http://www.pp3.cn/html/ptc/cat/zhiwu/\d+.html',
        'titleXpath':'//h1[@class="yh"]/text()',
        'imgXpath':'//div[@class="picbox"]/a[1]/@href',
        'contentXpath':'',
        'timeXpath':'//p[@class="dgrey tc"]/i[2]/text()',
        'myposXpath':'//div[@class="crumb grey"]/a/text()',
        'fenyePattern':['1.html','%d.html'],
        'isAlbum':0
        },
    'zw3e.com':{
        'category':'植物', 
        'domain':'zw3e.com', 
        'sourceUrl':{
                'http://www.zw3e.com/641/index_1.html':7,
                'http://www.zw3e.com/636/index_1.html':4,
                'http://www.zw3e.com/105/index_1.html':80,
                'http://www.zw3e.com/961/index_1.html':30,
                'http://www.zw3e.com/101/index_1.html':2,
                'http://www.zw3e.com/102/index_1.html':2,
                'http://www.zw3e.com/103/index_1.html':2,
            },
        'urlPattern':'http://www.zw3e.com/\d+/e\d+.html',
        'bodyPattern':{"tag":"div", "id":["con_body"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'fenyePattern':['index_1.html','index_%d.html'],
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|png)',
        'isAlbum':1
        },
    '52yhua.com':{
        'category':'植物', 
        'domain':'52yhua.com', 
        'sourceUrl':{
                 'http://www.52yhua.com/tupian/list_4_1.html':87,
                 'http://www.52yhua.com/':1,
                 'http://www.52yhua.com/fenlei/':1,
                 'http://www.52yhua.com/huayu/list_5_1.html':11,
                 'http://www.52yhua.com/zhuanti/list_8_1.html':14,
                 'http://www.52yhua.com/jishu/list_9_1.html':114,
                 'http://www.52yhua.com/fanzhi/list_11_1.html':35,
                 'http://www.52yhua.com/binghai/list_10_1.html':16,
                 'http://www.52yhua.com/jiating/list_13_1.html':56,
            },
        'urlPattern':'http://www.52yhua.com/.{0,20}/\d+.html',
        'bodyPattern':{"tag":"div", "class":["content"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'fenyePattern':['1.html','%d.html'],
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|png)',
        'isAlbum':1
        },

    'huabaike.com':{
        'category':'植物', 
        'domain':'huabaike.com', 
        'sourceUrl':{
                'https://www.huabaike.com/jtyh/p1.html':123,
                'https://www.huabaike.com/yhjq/p1.html':162,
                'https://www.huabaike.com/hyjk/p1.html':77,
                'https://www.huabaike.com/sphh/p1.html':9,
                'https://www.huabaike.com/pjzz/p1.html':7,
                'https://www.huabaike.com/cbzw':1,
                'https://www.huabaike.com/mbzw':1,
                'https://www.huabaike.com/tbzw':1,
                'https://www.huabaike.com/lkzw':1,
                'https://www.huabaike.com/sszw':1,
                'https://www.huabaike.com/qgzw':1,
                'https://www.huabaike.com/sgzw':1,
            },
        'urlPattern':'https://www.huabaike.com/.{0,20}/\d+.html',
        'myposPattern': {"tag":"div", "class":["BreadNav"]}, 
        'bodyPattern':{"tag":"div", "class":["contentDiv"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'fenyePattern':['p1','p%d'],
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|png)',
        'isAlbum':1
        },

    'plant.cila.cn':{
        'category':'植物', 
        'domain':'plant.cila.cn', 
        'sourceUrl':{
                'http://plant.cila.cn/zhiwulist1.html':1,
                'http://plant.cila.cn/zhuanti/yuanlinqiaomu200/1.html':17,
                'http://plant.cila.cn/zhiwuzhishi1.html':2117,
                'http://plant.cila.cn/zhiwulist1.html':127,
                'http://plant.cila.cn/tujian1.html':504,
                'http://plant.cila.cn/guanshang/duorou1.html':4,
            },
        'myposPattern': {"tag":"div", "class":["path"]}, 
        'urlPattern':'plant.cila.cn/.*/.*',
        'bodyPattern':{"tag":"div", "class":["cont"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'fenyePattern':['1.html','%d.html'],
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|png)',
        'isAlbum':1
        },

    'tuchong.com':{
        'post':1,
        'category':'植物', 
        'domain':'tuchong.com', 
        'sourceUrl':{
                        'https://tuchong.com/rest/tags/%E6%A4%8D%E7%89%A9/posts?page=1&count=100&order=new':100, 
                        'https://tuchong.com/rest/tags/%E5%A4%9A%E8%82%89%E6%A4%8D%E7%89%A9/posts?page=1&count=20&order=new':20
                    },
        'urlPattern':'tuchong.com/.*',
        'fenyePattern':['page=1', 'page=%d'],
        'bodyPattern':{"tag":"img", "class":["multi-photo-image"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'fenyePattern':['1.html','%d.html'],
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|png)',
        'titlePattern':  {"tag":"div", "class":["common-tag"]},
        'isAlbum':1

    },

    'jituwang.com':{
        'category':'植物', 
        'domain':'jituwang.com', 
        'sourceUrl':{
                        'http://www.jituwang.com/tuku/shuiguoshucai/list_1.html':164
                    },
        'urlPattern':'http://www.jituwang.com/tuku/\d+/\d+.html',
        'fenyePattern':['list_1.html', 'list_%d.html'],
        'titleXpath':'//div[@class="img_title"]/h1/text()',
        'imgXpath':'//div[@class="bg_img"]/a/@href',
        'contentXpath':'//div[@class="img_msg"]/text()',
        'timeXpath':'',
        'myposXpath':'//div[@class="breakcrumb"]/a/text()',
        'isAlbum':0
    },
    '99bz.net':{
        'category':'植物', 
        'domain':'99bz.net', 
        'sourceUrl':{
                        'http://www.99bz.net/bz/zhiwubizhi_1.html':13,
                        'http://www.99bz.net/bz/huahuibizhi_1.html':22,
                    },
        'urlPattern':'http://www.99bz.net/bz/\d+.html',
        'fenyePattern':['_1.html', '_%d.html'],
        'bodyPattern':{"tag":"div", "class":["pp","hh"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'fenyePattern':['1.html','%d.html'],
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|png)',
        'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },
    'bz55.com':{
        'category':'植物', 
        'domain':'bz55.com', 
        'sourceUrl':{
                        'http://www.bz55.com/zhiwubizhi/list_50_1.html':44,
                    },
        'urlPattern':'http://www.bz55.com/zhiwubizhi/\d+/\d+/\d+.html',
        'fenyePattern':['_1.html', '_%d.html'],
        'bodyPattern':{"tag":"div", "class":["imglist"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'fenyePattern':['1.html','%d.html'],
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|png)',
        'isAlbum':1
    },
    'jiachong.net':{
        'category':'植物', 
        'domain':'jiachong.net', 
        'sourceUrl':{
                        'http://pic.jiachong.net/zw/sctp/list_88_1.html':23,
                        'http://pic.jiachong.net/zw/gstp/list_89_1.html':12,
                        'http://pic.jiachong.net/zw/smtp/list_90_1.html':21,
                        'http://pic.jiachong.net/zw/hctp/list_91_1.html':15,
                        'http://pic.jiachong.net/zw/drzw/list_92_1.html':18,
                        'http://pic.jiachong.net/zw/snzw/list_93_1.html':12,
                    },
        'urlPattern':'http://pic.jiachong.net/zw/.{0,20}/\d+.html',
        'fenyePattern':['_1.html', '_%d.html'],
        'titleXpath':'//h1/text()',
        'imgXpath':'//div[@class="artbody"]/p/a/img/@src',
        'contentXpath':'//div[@class="gjz_tag"]/div[@class="ta_block"]/div[@class="smr"]/text()',
        'timeXpath':'//span[@class="icon-timer"]/text()',
        'myposXpath':'//div[@class="position"]/a/text()',
        'isAlbum':0
    },
   'm1ok.com':{
        'category':'植物', 
        'domain':'m1ok.com', 
        'sourceUrl':{
                        'http://www.m1ok.com/desk/deskzw1.shtm':28,
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
        'category':'植物', 
        'domain':'zhuoku.com', 
        'sourceUrl':{
                        'http://www.zhuoku.com/zhuomianbizhi/dong-zhiwu/index-1.htm':13,
                    },
        'urlPattern':'http://www.zhuoku.com/.*/.*/\d+.htm',
        'fenyePattern':['1.htm', '%d.htm'],
        'bodyPattern':{"tag":"div", "class":["bizhiin"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.*.(jpg|jpeg|png)',
        'imgReplace':[['thumbs/tn_', '']],
        'isAlbum':1
    },

   'deskbz.com':{
        'category':'植物', 
        'domain':'deskbz.com', 
        'sourceUrl':{
                        'http://www.deskbz.com/zhiwu/':1,
                    },
        'urlPattern':'http://www.deskbz.com/zhiwu/\d+.html',
        'bodyPattern':{"tag":"div", "class":["picturebox"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.*.(jpg|jpeg|png)',
        'isAlbum':1
    },
}
