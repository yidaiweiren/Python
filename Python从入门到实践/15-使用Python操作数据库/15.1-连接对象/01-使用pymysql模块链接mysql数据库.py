# -*- coding:utf-8 -*-
'''
@author:cuiyb
@Wechat Contact:******
@project:Python
@file:01-使用pymysql模块链接mysql数据库.py
@time:2019/7/27 13:36
'''

import pymysql
conn = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "Cc151602",
    db = "books",
    charset = "utf8",
    cursorclass = pymysql.cursors.DictCursor
)

if conn:
    print("ok")
else:
    print("die")

cursor = conn.cursor()
cursor.execute("insert into users (uname,upass) values ('laowang','laowang')")

conn.commit()

cursor.close()

conn.close()