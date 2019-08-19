class Person(object):
    def __init__(self,newName,newAge):
        self.name = newName
        self.age = newAge

laowang = Person("老王",18)
print(laowang.name)
print(laowang.age)

laowang.addr = "上海······"
print(laowang.addr)

laozhao = Person("老赵",20)

#给类动态添加属性
Person.num = 100

print(laowang.num)
print(laozhao.num)