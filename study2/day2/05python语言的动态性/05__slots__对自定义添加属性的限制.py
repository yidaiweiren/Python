class Person(object):
    __slots__ = ("name","age")


p1 = Person()
p1.name = "p1"
print (p1.name)

p1.age = 18
print(p1.age)

p1.addr = "beijing"
print(p1.addr)

'''
slots可以限定用户可自定义添加的属性，其中没有addr所以执行结果，添加addr属性时报错
p1
18
    p1.addr = "beijing"
AttributeError: 'Person' object has no attribute 'addr'
'''