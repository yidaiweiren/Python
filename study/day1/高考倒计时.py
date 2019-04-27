#高考倒计时
#日期运算有问题
#使用datetime模块
import datetime
year=int(input("请输入考试年份："))
month=int(input("请输入考试月份："))
day=int(input("请输入考试日期："))
Gyear=datetime.datetime.now().year
Gmonth=datetime.datetime.now().month
Gday=datetime.datetime.now().day
print ("::::::::::::::::::::::::::::::::")
Kyear=year-Gyear
Kmonth=month-Gmonth
Kday=day-Gday
print ("距离"+str(year)+"年高考，还有"+str(Kyear)+"年"+str(Kmonth)+"月"+str(Kday)+"日")