#-*-coding:utf-8-*-
#匿名函数扩展-1

#这种写法不灵活，只能计算加法
def test(a,b):
    result=a+b
    return result

nums=test(11,22)
print (nums)
'''
33
'''

#使用匿名函数当作实参
def test2(a,b,func):
    result=func(a,b)
    return result

nums2=test2(11,22,lambda x,y:x+y)
print (nums2)
'''
33
'''

'''
函数执行过程
    1.将实参11,22,lambda x,y:x+y传给a,b,func
    2.执行func(a,b),发现func为函数（x+y），也就是说把接收到的a的值“作为实参”给x，把接收到的b的值“作为实参”给y
    3.执行x+y
    4.return将计算结果返回给test2（）函数
    5.打印这个返回值
'''
