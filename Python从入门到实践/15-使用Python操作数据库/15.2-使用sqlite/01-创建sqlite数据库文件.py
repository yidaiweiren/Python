# -*- coding:utf-8 -*-
'''
@author:cuiyb
@Wechat Contact:******
@project:Python
@file:01-创建sqlite数据库文件.py
@time:2019/7/27 13:51
'''

import sqlite3

#连接到sqlite数据库
#数据文件时soft.db,如果文件不存在，会自动在当前目录创建

conn = sqlite3.connect('soft.db')

#创建一个游标（cursor）
cursor = conn.cursor()

#执行一条sql语句，创建一个user表
cursor.execute('create table user (id int(10) primary key, name varchar(20))')

#关闭游标
cursor.close()

#关闭数据库链接
conn.close()