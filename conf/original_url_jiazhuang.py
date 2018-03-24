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

}

