#查询大于2000的数据
import pymysql
db=pymysql.connect("localhost","root","Cc151602","testdb")
cursor=db.cursor()
sql="select * from employee where INCOME<%s" %(20000)
try:
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        fname=row[0]
        lname=row[1]
        age=row[2]
        sex=row[3]
        income=row[4]
        print ("fname=%s,lname-%s,age=%s,sex=%s,income=%s" % (fname,lname,age,sex,income))
except:
    print("Error:unable to fetch data")
db.close()
