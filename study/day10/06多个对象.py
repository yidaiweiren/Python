#定义一个类
'''
class 类名：
      属性：
      方法：
        函数（def）也可做为类的方法，但必须写在class中
        def eat(self):  #定义方法过程中需要写上self
            pass
'''
class Cat:
    #属性
    #方法
    def eat(self):
        print ("猫正在吃东西···")
    def drink(self):
        print ("猫正在喝水···")
    def introduce(self):    #introduce:释义为介绍
        print ("%s的年龄是：%d岁"%(tom.name,tom.age))
#类的调用
#Cat()  #类似于函数调用

#创建一个对象
tom=Cat()       #先执行=右边，在内存中生成了一个对象，然后tom也指向了这个对象


#调用这个类
#对象.方法
tom.eat()
tom.drink()
'''
猫正在吃东西···
猫正在喝水···
'''

#添加属性（目前把属性可以理解为变量）
#对象.变量
tom.name="汤姆"
tom.age=40

#查看添加的属性
#获取属性的第一种方式
print ("%s的年龄是%d"%(tom.name,tom.age))

#获取属性的第二种方式（将第一种写成方法）
#调用方法
tom.introduce()

############################################################################################
#创建第二个对象
lanmao=Cat()
lanmao.eat()
lanmao.drink()
lanmao.name="蓝猫"
lanmao.age=20
lanmao.introduce()  #结果不对
