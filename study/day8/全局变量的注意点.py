#全局变量的注意点
#把一个变量放到函数的前面，函数可以获取到这个变量
#把一个变量放到函数的后面，函数可以获取到这个变量
#把一个变量放到“调用函数”的后面，函数不能获取到这个变量

a=100
def test():
    print ("a=%d"%a)
    print ("b=%d"%b)
    print ("c=%d"%c)
b=200

test()

c=300

'''
a=100
b=200
#提示c未定义
Traceback (most recent call last):
  File "D:/PycharmProjects/Python/study/day8/全局变量的注意点.py", line 13, in <module>
    test()
  File "D:/PycharmProjects/Python/study/day8/全局变量的注意点.py", line 10, in test
    print ("c=%d"%c)
NameError: name 'c' is not defined
'''