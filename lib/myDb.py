# -*- coding:utf-8 -*
import MySQLdb
import sys
import time
import json
reload(sys)
sys.setdefaultencoding('utf-8')

wlcdb = {'user':'', 'passwd':'', 'dhost':'127.0.0.1', 'dport':3306}
rlcdb = {'user':'', 'passwd':'', 'dhost':'127.0.0.1', 'dport':3306}

def build_insert_sql(conn, talbe_name, k_v):
    names=[]
    values=[]
    for key in k_v.keys():
        names.append(key)
        value = k_v[key]
        if isinstance(value, basestring) or isinstance(value, str):
            values.append("'%s'"% conn.escape_string(value))
        elif isinstance(value, int):
            values.append("%d"%value)
        else:
            values.append("%d"%value)
    return "insert ignore into %s (%s) values (%s);" % (talbe_name, ",".join(names), ",".join(values))

def writeDB(talbe_name, k_v, dbase='chuilei'):
    try:
        conn=MySQLdb.connect(host = wlcdb['dhost'], user = wlcdb['user'], passwd = wlcdb['passwd'], db = dbase, port = wlcdb['dport'])
        executeSql = build_insert_sql(conn, talbe_name, k_v)
        cur=conn.cursor()
        cur.execute("SET NAMES utf8mb4")
        try:
            #print executeSql
            cur.execute(executeSql)
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        cur.close()
        conn.commit()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error insertList"


def getDB(executeSql, dbase):
    try:
        conn=MySQLdb.connect(host = rlcdb['dhost'], user = rlcdb['user'], passwd = rlcdb['passwd'], db = dbase, port = rlcdb['dport'])
        cur=conn.cursor()
        cur.execute("SET NAMES utf8mb4")
        try:
            cur.execute(executeSql)
            results=cur.fetchall()
            return results
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        cur.close()
        conn.commit()
        conn.close()
    except MySQLdb.Error,e:
        print e
        print "Mysql Error selectList"

def doDB(executeSql, dbase='chuilei'):
    ret = 0
    try:
        conn=MySQLdb.connect(host = wlcdb['dhost'], user = wlcdb['user'], passwd = wlcdb['passwd'], db = dbase, port = wlcdb['dport'])
        cur=conn.cursor()
        try:
            ret = cur.execute(executeSql)
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        cur.close()
        conn.commit()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error insertList"
    return ret

'''
def writePicMany(talbe_name, picList, dbase='chuilei'):
    rukuList = []
    x = time.localtime(time.time())
    nowTime = time.strftime('%Y-%m-%d %H:%M:%S',x)
    try:
        conn=MySQLdb.connect(host = lcdb['dhost'], user = lcdb['user'], passwd = lcdb['passwd'], db = dbase, port = lcdb['dport'])
        sql = "insert into "+tbl+"(set_sign, pic_seq, objurl, from_url, pic_title, pic_desc, picture_id, width, height, content_sign1, content_sign2, create_time, update_time) values(%d, %d, %s, %s, %s, %s, %d, %d, %d, %d, %d, %s, %s)"
        for picDic in picList:
            picTuple = (picDic['set_sign'], picDic['pic_seq'], picDic['objurl'], picDic['from_url'], picDic['pic_title'], \
                    picDic['pic_desc'],picDic['picture_id'],picDic['width'], picDic['height'],picDic['content_sign1'], \
                    picDic['content_sign2'], nowTime, nowTime)
            rukuList.append(picTuple)
        cur=conn.cursor()
        cur.execute("SET NAMES utf8mb4")
        try:
            cur.executemany(sql, rukuList)
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        cur.close()
        conn.commit()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error insertList"
'''

