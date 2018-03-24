#encoding:utf-8
webInfo = {
    'warting.com':{
        'category':'素材', 
        'domain':'warting.com', 
        'sourceUrl':{'http://www.warting.com/gallery/list_1.html':771, 'http://www.warting.com/works/list_1.html':3},
        'urlPattern':'http://www.warting.com/gallery/\d+/\d+.html',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"ul", "class":["picshow_first"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'myposPattern': {"tag":"div", "class":["location"]}, 
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'textPattern':{"tag":"div", "class":["article_bd"]},
        'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },

    'jb51.net':{
        'category':'素材', 
        'domain':'jb51.net', 
        'sourceUrl':{
                'http://sc.jb51.net/design/list_2_1.html':1270,
                'http://sc.jb51.net/web/vector/list_70_1.html':760,
                'http://sc.jb51.net/picture/list_3_1.html':1410,
                'http://sc.jb51.net/web/gif/list_5_1.html':59,
                'http://sc.jb51.net/ppt/list_20_1.html':158,
                'http://sc.jb51.net/aemoban/list_1.html':24,
                'http://sc.jb51.net/ziti/list_1.html':58,
                'http://sc.jb51.net/web/list_1_1.html':47,
            },
        'urlPattern':'http://sc.jb51.net/.*/\d+.htm',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"div", "class":["content-b"]},
        'myposPattern': {"tag":"div", "class":["pos"]}, 
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'isAlbum':1
    },

    'm1ok.com':{
        'category':'素材', 
        'domain':'m1ok.com', 
        'sourceUrl':{
                'http://www.m1ok.com/scsl/scsl1.shtm':236,
                'http://www.m1ok.com/sczt/sczt1.shtm':126,
                'http://www.m1ok.com/scppt/scppt1.shtm':77,
                'http://www.m1ok.com/scpsd/scpsd1.shtm':239,
                'http://www.m1ok.com/scwymb/scwymb1.shtm':232,
                'http://www.m1ok.com/scflash/scflash1.shtm':99,
                'http://www.m1ok.com/sc3d/sc3d1.shtm':63,
                'http://www.m1ok.com/sctb/sctb1.shtm':233,
            },
        'urlPattern':'http://www.m1ok.com/Article/\d+/\d+/index.htm',
        'bodyPattern':{"tag":"div", "class":["scMainL"]},
        'fenyePattern':['1.shtm','%d.shtm'],
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*upload.*\.(jpg|jpeg|gif|JPG|png)',
        'textXpath':'//div[@class="scMainLBqL link03"]/a/text()',
        'myposXpath':'//div[@class="scMainL"]/div[1]/span[1]/a/text()',
        'isAlbum':1
    },

    'tuku.cn':{
        'category':'素材', 
        'domain':'tuku.cn', 
        'sourceUrl':{
                'http://www.tuku.cn/aclass.aspx?id=11&Page=1':13,
                'http://www.tuku.cn/photoshop.aspx':1,
                'http://www.tuku.cn/vector.aspx':1,
            },
        'urlPattern':'http://www.tuku.cn/.*\?typeid=\d+',
        'bodyPattern':{"tag":"from", "id":["DataList1", "class_DataList1"]},
        'textPattern':{"tag":"from", "id":["DataList1", "class_DataList1"]},
        'titlePattern':{"tag":"span", "id":["Label1"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'fenyePattern':['Page=1','Page=%d'],
        'imgUrlPattern':ur'http://image5.tuku.cn/pic/.*/s\d+.(jpg|jpeg)',
        'imgReplace': [['/s0', '/0'], ['/s1', '/1'], ['/s2', '/2'], ['/s3', '/3'], ['/s4', '/4'], ['/s5', '/5']],
        'detailFenyePattern':['', '&Page=%d'],
        'isAlbum':1
        },

    'ivsky.com':{
        'category':'素材', 
        'domain':'ivsky.com', 
        'sourceUrl':{
                'http://www.ivsky.com/tupian/guanggaosheji/index_1.html':11,
                'http://www.ivsky.com/tupian/shejisucai/index_1.html':38,
            },
        'urlPattern':'http://www.ivsky.com/.{0,30}/.{0,60}/',
        'bodyPattern':{"tag":"ul", "class":["pli", "il", "ali"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'fenyePattern':['_1.html','_%d.html'],
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'textPattern': {"tag":"div", "class":["al_info"]}, 
        'imgReplace':[['/t/','/pre/']],
        'isAlbum':1
        },

    'ffpic.com':{
        'category':'素材', 
        'domain':'ffpic.com', 
        'sourceUrl':{
                'http://www.ffpic.com/psd/index.html':457,
            },
        'fenyePattern':['.html','_%d.html'],
        'urlPattern':'http://www.ffpic.com/psd/\d+.html',
        'titleXpath':'//div[@class="title"]/div[@class="lefts"]/span/a/text()',
        'imgXpath':'//div[@class="down_pic"]/a/@href',
        'contentXpath':'//span[@id="miaosu"]//text()',
        'timeXpath':'//ul/li[9]/span/text()',
        'myposXpath':'//p[@class="path"]/a/text()',
        'isAlbum':0
        }, 

    'tupianzj.com':{
        'category':'素材', 
        'domain':'tupianzj.com', 
        'sourceUrl':{
                'http://www.tupianzj.com/chuangyi/list_2_1.html':117,
            },
        'fenyePattern':['1.html','%d.html'],
        'urlPattern':'http://www.tupianzj.com/.*/\d+/\d+.html',
        'titleXpath':'//div[@class="title"]/h2/text()',
        'imgXpath':'//img[@id="bigpicimg"]/@src',
        'contentXpath':'//div[@class="tishi"]/a/text()',
        'timeXpath':'//div[@class="vi2_b"]/text()',
        'myposPattern':'//div[@class="weizhi"]/a/text()',
        'detailFenyePattern':['.html', '_%d.html'],
        'detailFyXpath':'//div[@class="pages"]/ul/li[1]/a/text()',
        'isAlbum':2
        }, 


    'niutuku.com':{
        'category':'素材', 
        'domain':'niutuku.com', 
        'sourceUrl':{
                'http://niutuku.com/psd/index.shtml':300,
                'http://niutuku.com/web/index.shtml':300,
                'http://niutuku.com/ppt/index.shtml':133
            },
        'urlPattern':'http://niutuku.com/(psd|web|ppt)/\d+.shtml',
        'fenyePattern':['.shtml', '_%d.shtml'],
        'bodyPattern':{"tag":"div", "class":["sucai"]},
        'myposPattern': {"tag":"div", "class":["place"]}, 
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },

    'niutuku.com':{
        'category':'素材', 
        'domain':'niutuku.com', 
        'sourceUrl':{
                'http://niutuku.com/psd/index.shtml':300,
                'http://niutuku.com/web/index.shtml':300,
                'http://niutuku.com/ppt/index.shtml':133,
                'http://niutuku.com/hd/15/index.shtml':300,
            },
        'urlPattern':'http://niutuku.com/(psd|web|ppt|hd)/\d+.shtml',
        'fenyePattern':['.shtml', '_%d.shtml'],
        'bodyPattern':{"tag":"div", "class":["sucai"]},
        'myposPattern': {"tag":"div", "class":["place"]}, 
        'textPattern': {"tag":"div", "class":["arc_title"]}, 
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },

    'lanrentuku.com':{
        'category':'素材', 
        'domain':'lanrentuku.com', 
        'sourceUrl':{
                'http://www.lanrentuku.com/vector/p1.html':1642,
                'http://www.lanrentuku.com/png/p1.html':84,
                'http://www.lanrentuku.com/psd/p1.html':54,
                'http://www.lanrentuku.com/tupian/beijingtupian/p1.html':5,
                'http://www.lanrentuku.com/gif/p1.html':2,
                'http://www.lanrentuku.com/show/pingmian/p1.html':5,
            },
        'urlPattern':'http://www.lanrentuku.com/(vector|png|psd|tupian|gif|show)/(\d+|(.*/.*)).html',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"div", "class":["content-a", "content-b"]},
        'myposPattern': {"tag":"div", "class":["place"]}, 
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },

    'gtn9.com':{
        'category':'素材', 
        'domain':'gtn9.com', 
        'sourceUrl':{
                'http://www.gtn9.com/brand_list.aspx?ID=1&category_id=0&page=1':827,
            },
        'urlPattern':'http://www.gtn9.com/work_show.aspx\?ID=[a-zA-Z0-9]+',
        'fenyePattern':['page=1', 'page=%d'],
        'bodyPattern':{"tag":"div", "class":["image-box"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*"',
        'imgReplace':[['"','']],
        'textXpath': '//a[@class="c-tx2"]/text()',
        'isAlbum':1
    },
    'poluoluo.com':{
        'category':'素材', 
        'domain':'poluoluo.com', 
        'sourceUrl':{
                'http://www.poluoluo.com/xinshang/Index.asp?page=1':439,
                'http://www.poluoluo.com/sucai/ShowClass.asp?ClassID=167&page=1':4,
                'http://www.poluoluo.com/sc/xk/?page=1':78,
                'http://www.poluoluo.com/sc/bgpic/?page=1':65,
                'http://www.poluoluo.com/sc/gaoguang/?page=1':7,
                'http://www.poluoluo.com/sc/ShowClass.asp?ClassID=174&page=1':217
            },
        'urlPattern':'http://www.poluoluo.com/.*/\d+.html',
        'fenyePattern':['page=1', 'page=%d'],
        'bodyPattern':{"tag":"div", "class":["box", "xstart", "scstart"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'myposPattern': {"tag":"div", "id":["mmmmm"]}, 
        'textPattern': {"tag":"div", "id":["noText"]}, 
        'isAlbum':1
    },
    'sucaitianxia.com':{
        'category':'素材', 
        'domain':'sucaitianxia.com', 
        'sourceUrl':{
                'http://www.sucaitianxia.com/psd/index.html':2894,
                'http://www.sucaitianxia.com/ai/index.html':1789,
                'http://www.sucaitianxia.com/png/index.html':18,
                'http://www.sucaitianxia.com/fonts/index.html':18,
                'http://www.sucaitianxia.com/photoshop/index.html':189,
            },
        'urlPattern':'http://www.sucaitianxia.com/.*/\d+.html',
        'fenyePattern':['.html', '_%d.html'],
        'bodyPattern':{"tag":"div", "class":["nr03"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'myposXpath': '//div[@class="nav_con"]/ul/li/a/text()', 
        'isAlbum':1
    },

    'aiimg.com':{
        'category':'素材', 
        'domain':'aiimg.com', 
        'sourceUrl':{
                'http://www.aiimg.com/vector/vector_material_1.html':548,
                'http://www.aiimg.com/psd/psd_material_1.html':839,
                'http://www.aiimg.com/taobao/taobao_162_1.html':123,
                'http://www.aiimg.com/photoshop/brush_1.html':86,
                'http://www.aiimg.com/png/png_material_1.html':136,
                'http://www.aiimg.com/web/personal_1.html':33,
            },
        'urlPattern':'http://www.aiimg.com/.*/\d+/\d+.html',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"div", "class":["imgbox"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'textXpath':ur'//div[@class="desc"]/dl[1]/dd/span/text()',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'myposXpath': '//div[@class="place"]/a/text()', 
        'isAlbum':1
    },

    '588ku.com':{
        'category':'素材', 
        'domain':'588ku.com', 
        'sourceUrl':{
                'http://588ku.com/sucai/page1/':1067,
                'http://588ku.com/moban/0-default-0-0-0-0-0-0-1/':500
            },
        'urlPattern':'http://588ku.com/.*/\d+.html',
        'fenyePattern':['1/', '%d/'],
        'bodyPattern':{"tag":"div", "class":["img-l-box"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'textXpath':ur'//div[@class="desc"]/dl[1]/dd/span/text()',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'myposXpath': '//div[@class="bread-nav"]/a/text()', 
        'isAlbum':1
    },
    'chinaz.com':{
        'category':'素材', 
        'domain':'chinaz.com', 
        'sourceUrl':{
                'http://font.chinaz.com/zhongwenziti.html':130,
                'http://font.chinaz.com/yingwenziti.html':708
            },
        'urlPattern':'http://font.chinaz.com/\d+.htm',
        'fenyePattern':['.html', '_%d.html'],
        'titleXpath':'//div[@class="text_wrap"]/h2/a/text()',
        'imgXpath':'//div[@class="imga"]/a/@href',
        'contentXpath':'//div[@class="gjz_tag"]/div[@class="ta_block"]/div[@class="smr"]/text()',
        'timeXpath':'//div[@class="lefts"]/span/em/text()',
        'myposXpath':'//div[@class="dangqian"]/a/text()',
        'isAlbum':0
    },
    '7kk.com':{
        'category':'素材', 
        'domain':'7kk.com', 
        'sourceUrl':{
                'http://www.7kk.com/sucai/beijingtu/new----1.html':8,
                'http://www.7kk.com/sucai/guanggaohaibao/new----1.html':8,
                'http://www.7kk.com/sucai/wangyesheji/new----1.html':1,
                'http://www.7kk.com/sucai/tupiansheji/new----1.html':6,
                'http://www.7kk.com/sucai/appsheji/new----1.html':1,
                'http://www.7kk.com/sucai/tubiao/new----1.html':4,
                'http://www.7kk.com/sucai/qitasucai/new----1.html':13,
            },
        'urlPattern':'http://www.7kk.com/.*/\d+.html',
        'bodyPattern':{"tag":"div", "id":["container", "focus"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'myposPattern': {"tag":"div", "class":["filterbar"]}, 
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'fenyePattern':['----1','----%d'],
        'isAlbum':1
    },

    'abc.2008php.com':{
        'category':'素材', 
        'domain':'abc.2008php.com', 
        'sourceUrl':{
                'https://abc.2008php.com/?PageNo=1&dz=1&topy=1':150,
                'https://abc.2008php.com/?PageNo=1&topy=3&dz=1':54,
                'https://abc.2008php.com/?PageNo=1&topy=5&dz=1':18,
                'https://abc.2008php.com/?PageNo=1&topy=7&dz=1':90,
                'https://abc.2008php.com/?PageNo=1&topy=12&dz=1':211,
                'https://abc.2008php.com/?PageNo=1&topy=10&dz=1':88,
            },
        'urlPattern':'https://abc.2008php.com/.*/\d+/\d+/\d+.html',
        'bodyPattern':{"tag":"p", "class":["pap"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'myposXpath': '//div[@id="new_da"]/div[2]/a/text()',
        'textXpath': '//div[@id="new_da"]/div[4]/a/text()',
        'fenyePattern':['PageNo=1','PageNo=%d'],
        'isAlbum':1
    },

    'ibaotu.com':{
        'category':'素材', 
        'domain':'ibaotu.com', 
        'sourceUrl':{
                'http://ibaotu.com/taobao/2-0-0-0-0-1.html':369,
                'http://ibaotu.com/shejiyuansu/5-0-0-0-0-1.html':344,
            },
        'urlPattern':'http://ibaotu.com/sucai/\d+.html',
        'bodyPattern':{"tag":"div", "class":["big-pic"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'myposXpath': '//div[@id="main"]/div[1]/a/text()',
        'fenyePattern':['1.html','%d.html'],
        'isAlbum':1
    },

    '3lian.com':{
        'category':'素材', 
        'domain':'3lian.com', 
        'sourceUrl':{'http://www.3lian.com/gif/more/03/index.html':217},
        'bodyPattern':{"tag":"div", "class":["article", "arc_pag"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'urlPattern':'http://www.3lian.com/gif/\d+/\d+-\d+/\d+.html',
        'myposXpath': '//div[@class="gg_cnt_left"]/a/text()',
        'textXpath': '//div[@class="tips"]/p/text()',
        'detailFenyePattern':['03/', '03/index_%d.html'],
        'fenyePattern':['.html','_%d.html'],
        'isAlbum':1
    },

    'ico.58pic.com':{
        'category':'素材', 
        'domain':'ico.58pic.com', 
        'sourceUrl':{
            'http://ico.58pic.com/tubiaodaquan/index/1.html':60,
            'http://ico.58pic.com/tubiaowenjian/index/1.html':135,
            },
        'bodyPattern':{"tag":"div", "class":["demoimg"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':ur'http.*\.(jpg|jpeg|gif|JPG|png)',
        'urlPattern':'http://ico.58pic.com/.{0,10}/\d+.html',
        'textXpath': '//div[@class="box_rightlast"]/p/a/span/text()',
        'titleXpath': '//div[@class="box_rightul"]/span/a/text()',
        'fenyePattern':['1.html','%d.html'],
        'isAlbum':1
    },

    'sc115.com':{
        'category':'素材', 
        'domain':'sc115.com', 
        'sourceUrl':{
            'http://www.sc115.com/vector/index.html' : 209,
            'http://www.sc115.com/psd/index.html' : 209,
            'http://www.sc115.com/Templates/index.html' : 40,
            'http://www.sc115.com/ppt/index.html' : 209,
            'http://www.sc115.com/png/index.html' : 209,
            'http://www.sc115.com/pattern/index.html' : 144,
            'http://www.sc115.com/3d/index.html' : 58,
            'http://www.sc115.com/psys/index.html' : 71,
            'http://www.sc115.com/tupian/beijing/index.html' : 105,
            'http://www.sc115.com/shows/poster/index.html' : 105,
            'http://www.sc115.com/shows/web/index.html' : 7,
            'http://www.sc115.com/shows/album/index.html' : 84,
            'http://www.sc115.com/shows/card/index.html' : 25,
            'http://www.sc115.com/shows/VI/index.html' : 105,
            'http://www.sc115.com/shows/logo/index.html' : 105,
            'http://www.sc115.com/shows/bz/index.html' : 105,
            'http://www.sc115.com/shows/pm/index.html' : 105,
            'http://www.sc115.com/shows/other/index.html' : 59,
            'http://www.sc115.com/tu/guanggao/index.html' : 13,
            'http://www.sc115.com/tu/jieri/index.html' : 10,
            'http://www.sc115.com/tu/mingpian/index.html' : 10,
            'http://www.sc115.com/tu/huace/index.html' : 26,
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

    'glzy8.com':{
        'category':'素材', 
        'domain':'glzy8.com', 
        'sourceUrl':{
                'http://www.glzy8.com/dl/1.html':19529,
            },
        'urlPattern':'http://www.glzy8.com/show/\d+.html',
        'fenyePattern':['1.html', '%d.html'],
        'titleXpath':'//div[@class="title"]/h1/text()',
        'imgXpath':'//div[@class="zoom"]/img/@src',
        'contentXpath':'//div[@class="soft"]/text()[1]',
        'timeXpath':'//div[@class="soft"]/text()',
        'myposXpath':'//div[@class="nav"]/a/text()',
        'isAlbum':0
    },

    '13cg.com':{
        'category':'素材', 
        'domain':'13cg.com', 
        'sourceUrl':{
                'http://www.13cg.com/album/hot/1':166,
            },
        'sourcePattern':'http://www.13cg.com/album/show/.*',
        'urlPattern':'http://www.13cg.com/note/\d+',
        'fenyePattern':['/1', '/%d'],
        'titleXpath':'//div[@class="picdis"]/p/text()',
        'imgXpath':'//a[@class="show_big"]/img/@src',
        'contentXpath':'//div[@class="nc_ut"]/span[1]/a/text()',
        'sourceFenyePattern':['', '/%d'],
        'timeXpath':'//div[@class="nc_ut"]/span[2]/text()',
        'myposXpath':'',
        'isAlbum':0
    },

    'shejiye.com':{
        'category':'素材', 
        'domain':'shejiye.com', 
        'sourceUrl':{
                'http://www.shejiye.com/index.php?m=content&c=index&a=lists&catid=17&page=1':151,
                'http://www.shejiye.com/index.php?m=content&c=index&a=lists&catid=15&page=1':55,
                'http://www.shejiye.com/index.php?m=content&c=index&a=lists&catid=13&page=1':79,
                'http://www.shejiye.com/index.php?m=content&c=index&a=lists&catid=12&page=1':74,
                'http://www.shejiye.com/index.php?m=content&c=index&a=lists&catid=1&page=1':5108,
                'http://www.shejiye.com/index.php?m=content&c=index&a=lists&catid=22&page=1':4159,
            },
        'urlPattern':'http://www.shejiye.com/index.php\?m=content&c=index&a=show&catid=\d+&id=\d+',
        'fenyePattern':['page=1', 'page=%d'],
        'bodyPattern':{"tag":"div", "class":["mainbox"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'myposPattern': {"tag":"div", "class":["location"]}, 
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },

    'zcool.com.cn':{
        'category':'素材', 
        'domain':'zcool.com.cn', 
        'sourceUrl':{
            'http://www.zcool.com.cn/discover/8!0!0!0!0!!!!2!0!1':100,
            'http://www.zcool.com.cn/discover/613!0!0!0!0!!!!2!0!1':35,
            'http://www.zcool.com.cn/discover/24!0!0!0!0!!!!-1!0!1':100,
            'http://www.zcool.com.cn/discover/499!0!0!0!0!!!!-1!0!1':100,
            'http://www.zcool.com.cn/discover/609!0!0!0!0!!!!-1!0!1':100,
            'http://www.zcool.com.cn/discover/1!0!0!0!0!!!!-1!0!1':100,
            'http://www.zcool.com.cn/discover/17!0!0!0!0!!!!-1!0!1':100,
            'http://www.zcool.com.cn/discover/8!0!0!0!0!!!!-1!0!1':100,
            'http://www.zcool.com.cn/discover/44!0!0!0!0!!!!-1!0!1':100,
            },
        'urlPattern':'http://www.zcool.com.cn/work/.*html',
        'fenyePattern':['!1', '!%d'],
        'bodyPattern':{"tag":"div", "class":["work-content-wrap"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'myposPattern': {"tag":"span", "class":["head-index"]}, 
        'imgUrlPattern':ur'http://img.zcool.cn/community/.{0,100}(jpg|jpeg|gif|JPG|png)',
        'detailFenyePattern':['.html', '/%d.html'],
        'isAlbum':1
    },

    '51pptmoban.com':{
        'category':'素材', 
        'domain':'51pptmoban.com', 
        'sourceUrl':{
                'http://www.51pptmoban.com/ppt/index.html':280,
                'http://www.51pptmoban.com/pic/index.html':61,
                'http://www.51pptmoban.com/tubiao/index.html':25,
                'http://www.51pptmoban.com/sucai/index.html':24,
                'http://www.51pptmoban.com/texiao/index.html':20,
            },
        'urlPattern':'http://www.51pptmoban.com/.*/\d+.html',
        'fenyePattern':['.html', '_%d.html'],
        'bodyPattern':{"tag":"div", "class":["ppt_pic"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'myposPattern': {"tag":"span", "class":["head-index"]}, 
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'detailFenyePattern':['.html', '_%d.html'],
        'textXpath':'//div[@class="ppt_js"]/text()',
        'myposXpath':'//div[@class="wz"]/a/text()',
        'isAlbum':1
    },

    '1ppt.com':{
        'category':'素材', 
        'domain':'1ppt.com', 
        'sourceUrl':{
                'http://www.1ppt.com/xiazai/ppt_xiazai_1.html':49,
                'http://www.1ppt.com/beijing/ppt_beijing_1.html':45,
                'http://www.1ppt.com/jieri/ppt_jieri_1.html':23,
                'http://www.1ppt.com/hangye/ppt_hangye_1.html':23,
                'http://www.1ppt.com/moban/ppt_moban_1.html':72,
            },
        'urlPattern':'http://www.1ppt.com/article/\d+.htm',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"div", "class":["content"]},
        'myposPattern': {"tag":"span", "class":["place"]}, 
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'isAlbum':1
    },

    '86ps.com':{
        'category':'素材', 
        'domain':'86ps.com', 
        'sourceUrl':{
                'http://www.86ps.com/psd/sheji/341_Index.html':314,
                'http://www.86ps.com/psd/haibao/377_Index.html':278,
                'http://www.86ps.com/psd/print/398_Index.html':174,
                'http://www.86ps.com/psd/yinglou/327_Index.html':1740,
                'http://www.86ps.com/psd/zhanban/317_Index.html':202,
                'http://www.86ps.com/psd/jieri/294_Index.html':152,
                'http://www.86ps.com/psd/2011tl/333_Index.html':337,
                'http://www.86ps.com/psd/zhaopian/332_Index.html':102,
                'http://www.86ps.com/psd/xiezhen/340_Index.html':237,
                'http://www.86ps.com/psd/ertong/329_Index.html':382,
                'http://www.86ps.com/PSSC/bjdw/141_Index.html':36,
                'http://www.86ps.com/PSSC/sc/261_Index.html':190,
            },
        'urlPattern':'http://www.86ps.com/psd/.*/\d+.htm',
        'fenyePattern':['Index.html', 'List_%d.html'],
        'titleXpath':'//div[@class="detail"]/h2/text()',
        'imgXpath':'//body/div[@class="box1000  clearfix"]/div[4]/div[4]/p/img/@src',
        'contentXpath':'//div[@class="detail"]/p[3]/text()',
        'timeXpath':'//div[@class="detail"]/font/text()',
        'myposXpath':'//div[@class="topPos"]/a/text()',
        'isAlbum':0
    },

    'sucaibar.com':{
        'category':'素材', 
        'domain':'sucaibar.com', 
        'sourceUrl':{
                'http://www.sucaibar.com/psd/index.html':231,
                'http://www.sucaibar.com/vector/index.html':248,
                'http://www.sucaibar.com/ppt/index.html':174,
                'http://www.sucaibar.com/icon/index.html':256,
            },
        'urlPattern':'http://www.sucaibar.com/.*/\d+.htm',
        'fenyePattern':['.html', '_%d.html'],
        'titleXpath':'//div[@class="detai-title"]/h1/text()',
        'imgXpath':'//img[@class="suo-img"]/@src',
        'contentXpath':'//div[@class="detai-sucai-img"]/p[2]/text()',
        'timeXpath':'//div[@class="detai-title"]/p/text()',
        'myposXpath':'//p[@class="location"]/a/text()',
        'isAlbum':0
    },

    'jituwang.com':{
        'category':'素材', 
        'domain':'jituwang.com', 
        'sourceUrl':{
                'http://www.jituwang.com/psd/guanggaosheji/list_1.html':687,
                'http://www.jituwang.com/psd/festival/list_1.html':82,
                'http://www.jituwang.com/psd/psdfencengsucai/list_1.html':390,
                'http://www.jituwang.com/psd/culture/list_1.html':25,
                'http://www.jituwang.com/psd/business/list_1.html':62,
                'http://www.jituwang.com/psd/huanjingsheji/list_1.html':90,
                'http://www.jituwang.com/psd/wangyemoban/list_1.html':120,
                'http://www.jituwang.com/vector/guanggaosheji/list_1.html':976,
                'http://www.jituwang.com/vector/festival/list_1.html':423,
                'http://www.jituwang.com/vector/diwenbiankuang/list_1.html':1394,
                'http://www.jituwang.com/vector/people/list_1.html':450,
                'http://www.jituwang.com/vector/culture/list_1.html':142,
                'http://www.jituwang.com/vector/shenghuobaike/list_1.html':722,
                'http://www.jituwang.com/vector/shengwushijie/list_1.html':178,
                'http://www.jituwang.com/vector/business/list_1.html':177,
                'http://www.jituwang.com/vector/kongjianhuanjing/list_1.html':105,
                'http://www.jituwang.com/vector/xiandaikeji/list_1.html':111,
                'http://www.jituwang.com/vector/logo/list_1.html':925,
                'http://www.jituwang.com/ps/brushes/list_1.html':17,
                'http://www.jituwang.com/tuku/background/list_1.html':338,
            },
        'urlPattern':'http://www.jituwang.com/.{0,30}/\d+/\d+.html',
        'fenyePattern':['list_1.html', 'list_%d.html'],
        'titleXpath':'//div[@class="img_title"]/h1/text()',
        'imgXpath':'//div[@class="bg_img"]/a/img/@src',
        'contentXpath':'//div[@class="img_msg"]/text()',
        'timeXpath':'//div[@class="img_submenu"]/dl/dd[9]/text()',
        'myposXpath':'//div[@class="breakcrumb"]/a/text()',
        'isAlbum':0

    },

}
