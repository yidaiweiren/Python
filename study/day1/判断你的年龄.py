#判断你的年龄
#使用到调用时间模块
#使用到算数运算符
#使用到IF语句
import datetime #调用datetime模块
imyear=int(input('请输入出生年份：'))   #获取用户输入的出生年份，使用int()函数判断取整
nowyear=datetime.datetime.now().year    #获取当前年份
#print (nowyear) #输出获取的年份
age=nowyear-imyear  #使用算数运算，来计算现在的年龄
print ("您的年龄为："+str(age)+"岁")
#####根据年龄判断现在的年龄阶段
print ("##########################")
if age<18:   #如果年龄小于18  #切记IF写完要加":"
    print ("您现在为未成年人：~@_@~")
if age>=18 and age<30:
    print ("您现在为青年人：-_-")
if age>=30 and age<60:
    print("您现在为中年人：~@<>@~")
if age>60:
    print ("您现在为老年人：*-_-*")