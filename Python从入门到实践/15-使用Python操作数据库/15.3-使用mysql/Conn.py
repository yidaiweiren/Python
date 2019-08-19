# -*- coding:utf-8 -*-
'''
@author:cuiyb
@Wechat Contact:******
@project:Python
@file:Conn.py
@time:2019/7/27 14:37
'''

import pymysql
import time

class Link_db(object):
    def __init__(self):
        print("这是连接数据库的类(Link_db)")
        #pass

    def Connect(self):
        '''创建链接数据库的方法'''
        host = "localhost"
        user = "root"
        password = "Cc151602"
        DB = "books"

        try:
            self.db = pymysql.connect(host, user, password, DB, charset="utf8")
            print("---Connect--%s---"%self.db)
            print("链接数据库--is ok")
        except:
            print("链接数据库--or die")

    def Cursor(self,sql):
        '''创建游标方法'''
        self.sql = sql
        cursor = self.db.cursor()
        print("---Cursor--%s---" % self.db)
        print("---Cursor--%s---"%self.sql)
        cursor.execute(self.sql)
        self.db.commit()
        date = cursor.fetchall()
        print(date)

        #关闭游标
        cursor.close()


class Select(Link_db):
    '''创建查询类--继承链接数据库类'''
    def __init__(self):
        print("这是select类")

    def select(self):
        pass


if __name__ == "__main__":
    a = Link_db()
    a.Connect()
    a.Cursor("insert into users (uname,upass) values ('pythonaq','123456')")
    #time.sleep(3)
    a.Cursor("select * from users")

    #time.sleep(3)
    s = Link_db()
    s.Connect()
    s.Cursor("update users set upass='test1haha' where uname='test1'")

    b = Link_db()
    b.Connect()
    b.Cursor("delete from users where uname='python'")
    b.Cursor("select * from users")
    b.Cursor("select * from bookinfo")
    b.Cursor("select version()")