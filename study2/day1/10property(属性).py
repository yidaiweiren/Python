#property（属性）

'''
t.num到底是调用getNum()还是setNum(),要根据实际的场景来判断
    1.如果给t.num赋值，那么一定时调用setNum()
    2.如果是获取t.num的值，那么久一定调用getNum()

property的作用：相当于把方法进行了封装，开发者在对属性设置数据时更方便

'''

class Test(object):
    def __init__(self):
        self.__num = 100    #加“__”问私有属性


    #获取值方法
    def getNum(self):
        print("-----getNum-----")
        return self.__num

    #设定值方法
    def setNum(self,newNum):
        print("-----setNum-----")
        self.__num = newNum

    num = property(getNum,setNum)   #num中同时放入get和set方法，当调用是系统会先判断时赋值还是取值，然后分发到不同的方法

t = Test()
#print(t.getNum())   #结果为100

#t.setNum(500)
#print(t.getNum())   #此处结果为500

print ("-="*25)

t.num = 200
print(t.num)
'''
结果
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
-----setNum-----
-----getNum-----
200
'''