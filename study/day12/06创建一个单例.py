#创建一个单例
'''
原来每创建一个对象，会指向一个内存空间。
而单例不管创建多少个对象，都会指向同一块内存空间
'''

class Dog(object):
    __instance = None   #常见一个私有属性（可以理解为变量）

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)    #将创建对象的引用赋值给__instance
            return cls.__instance
        else:
            #return上一次创建的对象的引用
            return cls.__instance


a = Dog()
print (id(a))

b = Dog()
print (id(b))

'''
结果：两个对象的引用指向同一块内存
2779683430976
2779683430976
'''

