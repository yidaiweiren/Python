#删除一条记录
import pymysql
db=pymysql.connect("localhost","root","Cc151602","testdb")
cursor=db.cursor()
sql="delete from employee where INCOME>%s" %(1200)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()