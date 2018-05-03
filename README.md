# tujiCrawer
### 通用的图集抓取和字段解析程序，采用配置模板对大部分站点进行图集抓取。
### 配置程序在conf中按照现有格式进行配置
  - clientSource.py 和 clientPage.py 为两个主要的程序
  - clientSource.py 用来发现链接
  - clientPage.py 用来抓取具体页面的图片

### 数据库表结构
> CREATE TABLE `tbl_content` (<br>
>>  `urlSign` char(32) NOT NULL DEFAULT '0' COMMENT '来源url的sign',<br>
>>  `title` varchar(256) NOT NULL DEFAULT '' COMMENT '标题',<br>
>> `text` text NOT NULL COMMENT 'text',<br>
>>  `images` text NOT NULL COMMENT '图片json',<br>
>>  `tags` varchar(1024) NOT NULL DEFAULT '' COMMENT '内容 tag',<br>
>>  `url` varchar(1024) NOT NULL DEFAULT '' COMMENT '新增URL',<br>
>>  `isAlbum` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否图集',<br>
>>  `picUrl` varchar(1024) NOT NULL DEFAULT '' COMMENT 'picUrl',<br>
>>  `mypos` varchar(1024) NOT NULL DEFAULT '' COMMENT 'mypos',<br>
>>  `sourceUrl` varchar(1024) NOT NULL DEFAULT '' COMMENT '抓取URL',<br>
>>  `status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '状态',<br>
>>  `category` varchar(64) NOT NULL DEFAULT '' COMMENT '类目',<br>
>>  `domain` varchar(1024) NOT NULL DEFAULT '' COMMENT 'domain',<br>
>>  `publishTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '发布时间',<br>
>>  `crawlTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '创建时间',<br>
>>  PRIMARY KEY (`urlSign`),<br>
>>  KEY `status_idx` (`status`)<br>
> )  ENGINE=InnoDB DEFAULT CHARSET=utf8;<br>
  
