#type继承类

class Animal:
    def eat(self):
        print("-----eat-----")

class Dog(Animal):
    pass

wangcai = Dog()
wangcai.eat()
#打印是谁创建出来的
print(wangcai.__class__)


Cat = type("Cat",(Animal,),{})

xiaohuamao = Cat()
xiaohuamao.eat()
#打印是谁创建出来的
print(xiaohuamao.__class__)