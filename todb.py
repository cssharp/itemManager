#!/usr/bin/python
#coding:utf-8

import sqlite3
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def test():
    conn = sqlite3.connect('db.sqlite3')
    print "Opened database successfully";
    c = conn.cursor()
    cursor = c.execute('SELECT * FROM app_item')
    for row in cursor:
       print "ID = ", row[0]
       print "NAME = ", row[1]
       print "ADDRESS = ", row[2]
       print "SALARY = ", row[3], "\n"

    print "Table created successfully";
    conn.commit()
    conn.close()


def insert(sql):
    conn = sqlite3.connect('db.sqlite3')
    print "Opened database successfully";
    c = conn.cursor()
    c.execute(sql)
    print "Table created successfully";
    conn.commit()
    conn.close()

def prepSql(filePath='C:\\Users\\XIA\\Desktop\\gs\\goodsSpider\\archive\\a2-by-aerosoles_Cool Cat.txt'):
    strx = open(filePath, 'r').read()
    j = json.loads(strx)
    strx = 'insert into app_item(brand, iid, name, imgUrls, category, weight, sizes, gender, itemUrl, price, feature) values ("{brand}","{iid}","{name}","{imgUrls}","{category}","{weight}","{sizes}","{gender}","{itemUrl}","{price}","{feature}")'
    strx = strx.format(brand = j['brand'],iid = j['id'],name = j['name'],imgUrls = "\n".join(j['imgUrls']),category = j['category'],weight = j['weight'],sizes = "\n".join(j['sizes']),gender = j['gender'],itemUrl = j['itemUrl'],price = j['price'],feature = j['feature'],featureTran = j['featureTrans'])
    return strx

if __name__ == '__main__':
    sql = prepSql()
    insert(sql)



