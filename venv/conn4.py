#数据库修改操作
import pymysql
db=pymysql.connect("localhost","root","Cc151602","testdb")
cursor=db.cursor()
sql="update employee set age=age+1 where sex='%s'" %('M')
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()