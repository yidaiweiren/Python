#__new__方法
'''
对象都是由__new__方法创建的，
定义一个对象时，父类没有写__new__方法，会默认继承父类；如果有__new__方法，会使用__new__方法

'''
class Dog(object):
    def __init__(self):
        print ("-----__init__方法-----")

    def __del__(self):
        print ("-----__del__方法-----")

    def __str__(self):
        print ("-----__str__方法-----")

    def __new__(cls):   #看清楚，此处是cls。cls此时时Dog指向的那个“类对象”，因为cls和Dog的id相同
        print (id(cls))
        print ("-----__new__方法-----")
        return object.__new__(cls)  #return返回创建对象的引用

print (id(Dog))
xtq = Dog()
