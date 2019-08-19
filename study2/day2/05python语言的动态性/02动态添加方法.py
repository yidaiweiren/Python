'''
动态添加方法
'''

class Person(object):
    def __init__(self,newName,newAge):
        self.name = newName
        self.age = newAge

    def eat(self):
        print ("-----%s正在吃-----"%self.name)

def run(self):
    print ("-----%s正在跑-----"%self.name)

p1 = Person("p1",18)
p1.eat()



#错误的添加方式
#p1.run = run
#p1.run()
'''
#虽然p1对象中，run属性已经指向定义的run函数，但是这句代码还是不正确
因为run属性指向的函数，是后来添加的，即p1.run（）的时候，并没有把p1当作第1个参数，导致run函数调用的时候，出现缺少参数的问题
'''

#正确调用方法
'''
导入一个types的模块
调用MethodType方法进行函数与对象绑定
MethodType(函数名，对象)
'''
import types

p1.run = types.MethodType(run,p1)
p1.run()
'''
-----p1正在吃-----
-----p1正在跑-----
'''