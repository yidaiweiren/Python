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
    '''定义了一个Cat类'''
    #属性
    #方法
    def __init__(self,new_name,new_age):     #初始化对象的方法,
        '''
        对象刚在内存中创建完成，就执行__init__方法，接收来自Cat（“汤姆”，40）的两个属性传递给形参，创建完成后，引用指向tom
        '''
        print ("----------haha----------")
        self.name=new_name
        self.age=new_age

    def __str__(self):
        #自动调用。print(tom)。获取tom对象的描述信息时自动调用
        return "%s的年龄是:%d"%(self.name,self.age)

    def eat(self):
        print ("猫正在吃东西···")

    def drink(self):
        print ("猫正在喝水···")

    def introduce(self):    #introduce:释义为介绍
        # #introduce(self)中的self相当于形参，接收tom.introduce()传入的参数，这就是self指向调用者的原因

        #print ("%s的年龄是：%d岁"%(tom.name,tom.age))    lanmao调用时出错位置
        print("%s的年龄是：%d岁" %(self.name, self.age))
        '''
        self到底是谁？
        通过哪个对象调用，self就是那个对象。类似于js中的this，谁点击就是谁。这里时谁调用就是谁
        '''
#类的调用
#Cat()  #类似于函数调用。此处为创建一个对象

#创建一个对象
tom=Cat("汤姆",40)       #先执行=右边，在内存中生成了一个对象，然后tom也指向了这个对象（引用）
print (tom)
############################################################################################
#创建第二个对象

lanmao=Cat("蓝猫",20)
print (lanmao)