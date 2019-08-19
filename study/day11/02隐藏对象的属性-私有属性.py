#-*-coding_utf-8-*-
#对比直接获取值和使用get方法获取的差别
#隐藏对象的属性-私有属性

class Dog:
    def __init__(self,new_name):
        self.name = new_name
        self.__age = 0      #定义一个私有属性，属性的名字是"__age"

    def set_age(self,new_age):
        if new_age>0 and new_age<100:
            self.__age = new_age
        else:
            self.__age = 0

    #定义一个get方法
    def get_age(self):
        return self.__age


dog = Dog("小白")
dog.set_age(-10)
age = dog.get_age()
print (age)
#print (dog.__age)   #私有属性，不能调用

