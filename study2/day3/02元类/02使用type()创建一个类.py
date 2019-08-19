#使用type（）创建一个类
'''
type(类名，由父类名称组成的元组（如果没有可为空），包含属性的字典（没有可为空）)

元类：最原始创建类的东西称为元类
'''

#创建一个类
Test2 = type ("Test2",(),{})
t2 = Test2()
print(type(t2))
'''
结果
<class '__main__.Test2'>
'''

#创建一个有属性的类
Person = type("Person",(),{"num":0})
p1 = Person()
print(p1.num)
'''
结果
0
'''

#创建一个带有方法的类
def printNum(self):
    print("-----num-%d-----"%self.num)

Test3 = type("Test3",(),{"printNum":printNum})

t3 = Test3()
t3.num = 100
t3.printNum()
'''
结果
-----num-100-----
'''

#相当于
class printNum2:
    def printNum2(self):
        print("-----num-%d-----"%self.num)

t2 = printNum2()
t2.num = 300
t2.printNum2()
'''
结果
-----num-300-----
'''