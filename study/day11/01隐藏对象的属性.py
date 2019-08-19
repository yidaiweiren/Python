#-*-coding_utf-8-*-
#对比直接获取值和使用get方法获取的差别
#隐藏对象的属性

class Dog:
    #
    def set_age(self,new_age):
        #使用传统方法
        #self.age = new_age

        #使用get方法+判断值得的合法性
        if new_age>0 and new_age<100:
            self.age = new_age
        else:
            self.age = 0

    #定义一个get方法
    def get_age(self):
        return self.age

#使用传统方式直接获取值，遇到负值就会有bug
dog = Dog()
#dog.age = -10   #结果为“-10”，不符合逻辑规范，年龄没有负值
#print (dog.age)


#使用get方法来获取
#dog.set_age(10)    #传入age的值。若值为负值，可以在set_age方法中做一个判断
#age = dog.get_age()     #使用get方法获取值
#print (age)     #打印获取的值


#使用get方法+判断
dog.set_age(-10)
age = dog.get_age()
print (age)
'''
0       结果为0，因为-10不合法，利用方法对传入的值做一个处理
'''
