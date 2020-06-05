#多个装饰器

def makeBlod(fn):
    def wrapped():
        print ("-----1-----")
        return "<b>"+fn()+"</b>"
    return wrapped

def makeItalic(fn):
    def wrapped():
        print ("-----2-----")
        return "<i>"+fn()+"</i>"
    return wrapped

@makeBlod
def test1():
    return "hello test1"
#相当于test1 = makeBlod（test1）
#test1（）

@makeItalic
def test2():
    return "hello test2"

@makeBlod
@makeItalic     #这里makeBlod下面没有函数，makeItalic下面紧靠函数，所以就近原则，先让makeItalic装饰函数，装饰完以后，再让makeBlod“接着”装饰所以结果就是下面最后的<b>包着<i>
def test3():
    print ("-----3-----")
    return "hello test3"


#test1()
#test2()
ret = test3()
print (ret)
'''
-----1-----
-----2-----
-----3-----
<b><i>hello test3</i></b>
'''