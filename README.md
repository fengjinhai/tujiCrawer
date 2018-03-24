# tujiCrawer
通用的图集抓取程序，采用配置模板对大部分站点进行图集抓取。

数据库表结构
 CREATE TABLE `tbl_content` (
  `urlSign` char(32) NOT NULL DEFAULT '0' COMMENT '来源url的sign',
  `title` varchar(256) NOT NULL DEFAULT '' COMMENT '标题',
  `text` text NOT NULL COMMENT 'text',
  `images` text NOT NULL COMMENT 'å›¾ç‰‡',
  `tags` varchar(1024) NOT NULL DEFAULT '' COMMENT '内容 tag',
  `url` varchar(1024) NOT NULL DEFAULT '' COMMENT '新增URL',
  `isAlbum` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否图集',
  `picUrl` varchar(1024) NOT NULL DEFAULT '' COMMENT 'picUrl',
  `mypos` varchar(1024) NOT NULL DEFAULT '' COMMENT 'mypos',
  `sourceUrl` varchar(1024) NOT NULL DEFAULT '' COMMENT '抓取URL',
  `status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '状态',
  `category` varchar(64) NOT NULL DEFAULT '' COMMENT '类目',
  `domain` varchar(1024) NOT NULL DEFAULT '' COMMENT 'domain',
  `publishTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '发布时间',
  `crawlTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '创建时间',
  PRIMARY KEY (`urlSign`),
  KEY `status_idx` (`status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
