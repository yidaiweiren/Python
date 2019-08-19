#多态
'''
没执行时不确定调用父类还是子类，当执行的那一瞬间，introduce（）中是谁，才知道最后掉的时父类还是子类

'''

class Dog(object):
    def print_self(self):
        print ("大家好，我是xxx，希望以后大家多多关照···")

class Xiaotq(Dog):
    def print_self(self):
        print ("hello,everybody,我是你们的老大，我是xxx")


def introduce(temp):     #看清楚，这是函数，不是方法
    temp.print_self()

dog1 = Dog()
dog2 = Xiaotq()

introduce(dog1) #大家好，我是xxx，希望以后大家多多关照···
introduce(dog2) #hello,everybody,我是你们的老大，我是xxx