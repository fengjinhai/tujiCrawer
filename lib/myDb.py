# -*- coding:utf-8 -*
import pymysql
import traceback
import sys
import time
import json

wlcdb = {'user':'root', 'passwd':'', 'dhost':'127.0.0.1', 'dport':3306}

def build_insert_sql(conn, talbe_name, k_v):
    names=[]
    values=[]
    for key in k_v.keys():
        names.append(key)
        value = k_v[key]
        if isinstance(value, str):
            values.append("'%s'"% conn.escape_string(value))
        elif isinstance(value, int):
            values.append("%d"%value)
        else:
            values.append("%d"%value)
    return "insert ignore into %s (%s) values (%s);" % (talbe_name, ",".join(names), ",".join(values))

def writeDB(talbe_name, k_v, dbase='tuji'):
    try:
        conn = pymysql.connect(host = wlcdb['dhost'], user = wlcdb['user'], passwd = wlcdb['passwd'], db = dbase, port = wlcdb['dport'])
        executeSql = build_insert_sql(conn, talbe_name, k_v)
        cur = conn.cursor()
        cur.execute(executeSql)
        cur.close()
        conn.commit()
        conn.close()
        return True
    except:
        traceback.print_exc()
        return False

def getDB(executeSql, dbase):
    try:
        conn=pymysql.connect(host = wlcdb['dhost'], user = wlcdb['user'], passwd = wlcdb['passwd'], db = dbase, port = wlcdb['dport'])
        cur=conn.cursor()
        cur.execute(executeSql)
        results=cur.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return results
    except:
        traceback.print_exc()
        return False

def doDB(executeSql, dbase='tuji'):
    try:
        conn=pymysql.connect(host = wlcdb['dhost'], user = wlcdb['user'], passwd = wlcdb['passwd'], db = dbase, port = wlcdb['dport'])
        cur=conn.cursor()
        ret = cur.execute(executeSql)
        cur.close()
        conn.commit()
        conn.close()
        return ret
    except:
        traceback.print_exc()
        return False
