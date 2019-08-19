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

#类的调用
#Cat()  #类似于函数调用

#创建一个对象
tom=Cat()       #先执行=右边，在内存中生成了一个对象，然后tom也指向了这个对象
