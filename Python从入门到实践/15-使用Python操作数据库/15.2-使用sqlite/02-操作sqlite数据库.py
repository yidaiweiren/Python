# -*- coding:utf-8 -*-
'''
@author:cuiyb
@Wechat Contact:******
@project:Python
@file:02-操作sqlite数据库.py
@time:2019/7/27 13:59
'''

import sqlite3

conn = sqlite3.connect('soft.db')

cursor = conn.cursor()


cursor.execute('insert into user(id,name) values ("5","cuiyb")')

conn.commit()




cursor.close()

conn.close()