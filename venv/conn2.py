#使用sql语句向数据库插入一条记录
import pymysql
db=pymysql.connect("localhost","root","Cc151602","testdb")
cursor=db.cursor()
sql="""INSERT INTO employee(first_name,last_name,age,sex,INCOME) values('cuiyb2','yidaiweiren','23','M','1200')"""
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()