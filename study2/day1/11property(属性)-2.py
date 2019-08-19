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
    @property   #使用property
    def num(self):  #定义什么名字，24行就使用"名字.setter"
        print("-----getNum-----")
        return self.__num

    #设定值方法
    @num.setter     #使用“名字.setter”
    def num(self,newNum):
        print("-----setNum-----")
        self.__num = newNum


t = Test()

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