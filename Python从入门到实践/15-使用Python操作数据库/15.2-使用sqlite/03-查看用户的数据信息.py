# -*- coding:utf-8 -*-
'''
@author:cuiyb
@Wechat Contact:******
@project:Python
@file:03-查看用户的数据信息.py
@time:2019/7/27 14:04
'''

import sqlite3

conn = sqlite3.connect('soft.db')

if conn :
    print("ok")

cursor = conn.cursor()

cursor.execute('select * from user')

#获取返回结果
#使用fetchone方法查询一条结果
result1 = cursor.fetchone()
print(result1)

#使用fetchmany方法查询多条数据
result2 = cursor.fetchmany(2)
print(result2)

#使用fetchall方法查询多条数据
result3 = cursor.fetchall()
print(result3)

cursor.close()

conn.close()