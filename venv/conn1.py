#使用sql语句创建数据库，检查若存在该数据库，删除再创建，若不存在，直接创建
import pymysql
db=pymysql.connect("localhost","root","Cc151602","testdb")
cursor=db.cursor()
#使用execute方法执行删除
cursor.execute("DROP TABLE IF EXISTS employee")
sql="""CREATE TABLE employee(
    first_name  char(20)    not null,
    last_name   char(20),
    age int,
    sex char(5),
    INCOME FLOAT
)"""
cursor.execute(sql)
db.close()