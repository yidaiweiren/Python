#连接数据库 并测试打印数据库版本
import pymysql
db=pymysql.connect("localhost","root","Cc151602","testdb")
cursor=db.cursor()
cursor.execute("SELECT VERSION()")
data=cursor.fetchone()
print ("Databases version:%s" % data)
db.close()