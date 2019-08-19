#私有化


class Test(object):
    def __init__(self):
        self.__num = 100    #加“__”问私有属性

    #获取值方法
    def getNum(self):
        return self.__num

    #设定值方法
    def setNum(self,newNum):
        self.__num = newNum

t = Test()
print(t.getNum())   #结果为100

t.setNum(500)
print(t.getNum())   #此处结果为500