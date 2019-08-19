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
    def test1(self):
        print ("-----test1-----")

#B相当于马
class B(Base):
    def test2(self):
        print ("-----test2-----")

#C相当与骡子
class C(A,B):   #同时继承多个类，每个父类用逗号隔开
    pass

c = C()
c.test()
c.test1()
c.test2()
'''
c同时继承了多个类
-----Base-----
-----test1-----
-----test2-----
'''