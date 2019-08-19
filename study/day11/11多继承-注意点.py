#多继承
#带有（object）这样的类称为“新式类”，object为默认参数，最底层的大类。
#不带（object）的类称为经典类
'''
举例：驴和马生下的是骡子
骡子继承了一部分驴的属性，也继承了一部分马的属性
'''

class Base(object):
    def test(self):
        print ("-----Base-----")

#A相当于驴
class A(Base):
    def test(self):
        print ("-----A-----")

#B相当于马
class B(Base):
    def test(self):
        print ("-----B-----")

#C相当与骡子
class C(A,B):   #同时继承多个类，每个父类用逗号隔开
    pass
    #def test(self):
        #print("-----C-----")

c = C()
c.test()    #结果：-----C-----。直接参考day11/08调用被重写的方法/注释

print (C.__mro__)   #类名__mro__:调用一个方法时搜索的顺序，如果在某个类中找到方法，那么停止搜索
'''
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>)
'''