#继承

#定义动物类，设定为父类，所有动物都具备吃喝拉撒的功能
class Animal:   #Animal：释义为“动物”
    def eat(self):
        print ("-----吃-----")

    def drink(self):
        print ("-----喝-----")

    def sleep(self):
        print ("-----睡觉-----")

    def run(self):
        print ("-----跑-----")

class Dog(Animal):  #dog类后面加（），括号中写入，父类的名字，即可继承父类
    #定义一个狗特有的方法：汪汪叫，同时也可以调用继承到父类的方法
    def bark(self):     #bark:释义为“叫”
        print ("-----汪汪叫-----")

class Cat(Animal):
    def catch(self):    #catch:释义为“抓住”
        print ("-----抓老鼠-----")

#a = Animal()
#a.eat()        #结果：-----吃-----。

#创建一个狗对象
wangcai = Dog()
wangcai.eat()   #结果：-----吃-----。表示已经继承到父类了。


#创建一个猫对象
tom = Cat()
tom.eat()   #结果：-----吃-----。表示已经继承到父类了。