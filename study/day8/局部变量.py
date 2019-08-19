#局部变量
#只对当前函数生效的变量称为局部变量
def test1():
    a=100
    print (a)

def test2():
    print("a=%d"%a)


test1()
test2()

'''
100    #test1正常执行

#test2执行报错，显示a为定义
Traceback (most recent call last):
  File "D:/PycharmProjects/Python/study/day8/局部变量.py", line 12, in <module>
    test2()
  File "D:/PycharmProjects/Python/study/day8/局部变量.py", line 8, in test2
    print("a=%d"%a)
NameError: name 'a' is not defined

'''