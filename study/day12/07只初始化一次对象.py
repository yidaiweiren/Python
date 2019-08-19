#创建一个单例
'''
需求
原来每创建一个对象，会指向一个内存空间。
而单例不管创建多少个对象，都会指向同一块内存空间
只让__init__方法初始化一次对象（也就是以后一直就是初始化的那个对象）
'''

class Dog(object):
    __instance = None   #常见一个私有属性（可以理解为变量）
    __init_flag = False

    def __new__(cls,name):  #name在这里暂时用不上，主要是防止创建时传参报错
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)    #将创建对象的引用赋值给__instance
            return cls.__instance
        else:
            #return上一次创建的对象的引用
            return cls.__instance

    def __init__(self,name):
        if Dog.__init_flag == False:
            self.name = name
            Dog.__init_flag = True


a = Dog("旺财")
print (id(a))
print (a.name)

b = Dog("哮天犬")
print (id(b))
print (b.name)

'''
结果：两个对象的name都是旺财
2019567346240
旺财
2019567346240
旺财
'''

