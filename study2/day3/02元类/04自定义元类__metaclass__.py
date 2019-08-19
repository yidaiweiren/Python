'''
自定义元类__metaclass__
'''

def upper_attr(future_class_name,future_class_parents,future_class_attr):

    #遍历属性字典，把不是以__开头的属性名字变为大写
    newAttr = {}
    for name,value in future_class_attr.items():
        if not name.startswith("__"):
            newAttr[name.upper()] = value

    #调用type来创建一个类
    return type(future_class_name,future_class_parents,newAttr)

class Foo(object,metaclass=upper_attr):
    #__metaclass__ = upper_attr  #python2写在这
    bar = "bip"

print(hasattr(Foo,"bar"))
print(hasattr(Foo,"BAR"))
t = Foo()
print(t.BAR)
print(t.bar)
