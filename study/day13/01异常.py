#异常

try:
    print (num)
    print ("-----1-----")
except NameError:   #except 异常名（异常的定性）
    print ("如果捕获到异常后做的处理，")
print ("-----2-----")
'''
结果
如果捕获到异常后做的处理，
-----2-----     后面的程序会正常执行，不会崩
'''
print (num)
print ("-----1-----")
'''
结果
Traceback (most recent call last):
  File "D:/PycharmProjects/Python/study/day13/01异常.py", line 9, in <module>
    print (num)
NameError: name 'num' is not defined    NameError叫做异常名
'''