#全局变量和局部变量的名字相同
#建议：全局变量尽量定义为：g_a=100。g为global，全局变量

a=100
def test():
    a=200
    print ("a=%d"%a)

def test2():
    print ("a=%d"%a)

test()

test2()

'''
a=200   test()输出的是局部变量

a=100   test2()输出的是全局变量
'''