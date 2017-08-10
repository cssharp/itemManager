#!/usr/bin/python
#coding:utf-8

import sqlite3
import json
import os
import sys
import logging
reload(sys)
sys.setdefaultencoding('utf-8')


def test():
    conn = sqlite3.connect('db.sqlite3')
    print "Opened database successfully";
    c = conn.cursor()
    cursor = c.execute('delete from app_item')
    print "Table created successfully";
    conn.commit()
    conn.close()


def insert(filePath='C:\\Users\\XIA\\Desktop\\gs\\goodsSpider\\archive\\a2-by-aerosoles_Cool Cat.txt'):
    strx = open(filePath, 'r').read()
    j = json.loads(strx)

    sql = 'insert into app_item(brand, iid, name, imgUrls, category, weight, sizes, gender, itemUrl, price, feature) values (?,?,?,?,?,?,?,?,?,?,?)'
    
    conn = sqlite3.connect('db.sqlite3')
    print "Opened database successfully";
    c = conn.cursor()
    c.executemany(sql, [( j['brand'], j['id'], j['name'], "\n".join(j['imgUrls']), j['category'], j['weight'], "\n".join(j['sizes']), j['gender'], j['itemUrl'], j['price'], j.get('feature', ''))])
    print "Table created successfully";
    conn.commit()
    conn.close()


def getFiles(pathStart, path='C:\\Users\\XIA\\Desktop\\gs\\goodsSpider\\archive'):
    dirs = os.listdir(path)
    result = []
    for x in dirs:
        if not os.path.isdir(x):
            if pathStart == 'all':
                result.append('{0}/{1}'.format(path, x))
            elif x.startswith(pathStart):
                result.append('{0}/{1}'.format(path, x))
    return result



def getAllFiles(path='C:\\Users\\XIA\\Desktop\\gs\\goodsSpider\\archive'):
    dirs = os.listdir(path)
    result = []
    for x in dirs:
        if not os.path.isdir(x):
            result.append('{0}/{1}'.format(path, x))
    return result


if __name__ == '__main__':
    test()
    #files = getFiles('adidas')
    files = getAllFiles()
    total = len(files)
    for i, filePath in enumerate(files):
        logging.warning('[{0}/{1}] {2}'.format(i+1, total, filePath))
        insert(filePath)


