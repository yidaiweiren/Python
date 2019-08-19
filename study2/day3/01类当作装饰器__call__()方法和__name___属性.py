#类当作装饰器

#使用类的调用引入
'''
class Test(object):
    def __call__(self):
        print("-----test-----")

t = Test()
t()
'''

'''
__call__()方法：让一个对象直接可以调用其中的方法
__name__方法：获取函数的名字
'''

class Test(object):
    def __init__(self,func):
        print("-----初始化-----")
        print("func name is %s"%func.__name__)
        self.__func = func
    def __call__(self):
        print("-----装饰器中的功能-----")
        self.__func()


@Test   #相当于创建一个类的对象，把test当作参数扔进去Test(test)
def test():
    print("-----test-----")


#test()