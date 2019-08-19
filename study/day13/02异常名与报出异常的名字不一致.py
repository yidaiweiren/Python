#异常名与报出异常的名字不一致

try:
    open("123.txt")
    print ("-----1-----")
except NameError:   #此处异常名不一致
    print ("如果捕获到异常后做的处理，")

except FileNotFoundError:
    print ("如果捕获到异常后做的处理，")

except (FileNotFoundError,NameError):   #如果有多个可能结果，外面用括号括起来，里面用逗号隔开
    print("如果捕获到异常后做的处理，")
print ("-----2-----")
'''
结果
Traceback (most recent call last):
  File "D:/PycharmProjects/Python/study/day13/02异常名与报出异常的名字不一致.py", line 4, in <module>
    open("123.txt")
FileNotFoundError: [Errno 2] No such file or directory: '123.txt'   此处的异常名是：FileNotFoundError

解决方案：再在底下写一个except
结果
如果捕获到异常后做的处理，
-----2-----
'''
