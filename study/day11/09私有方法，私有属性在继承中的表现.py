#私有方法，私有属性在继承中的表现
#私有方法，私有属性：相当于人的一下小秘密不能继承给子类
'''
如果调用的是 继承的父类中的公有方法，可以在这个方法种访问父类中的私有方法和私有属性。
但是 如果子类中实现了一个公有方法，那么这个方法是不能调用继承的父类中的私有方法和私有属性。
'''
class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def test1(self):
        print ("-----test1-----")

    def __test2(self):
        print ("-----test2-----")

    def test3(self):
        self.__test2()  #调用私有方法
        print (self.__num2)     #调用私用属性

class B(A):
    def test4(self):
        self.__test2()  # 调用私有方法
        print(self.__num2)  # 调用私用属性

b = B()
#继承方法
#b.test1()      #公有方法正常继承。结果：-----test1-----
#b.__test2()     #不能继承私有方法

#继承属性
#print (b.num1)      #共有属性正常继承。结果：100
#print (b.__num2)    #私有属性不能继承


b.test3()
'''
-----test2-----
200
'''

b.test4()   #结果：报错