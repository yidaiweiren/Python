#私有化

'''
class Test(object):
    def __init__(self):
        self.num = 100


t = Test()
print (t.num)   #结果位100
t.num = 200
print(t.num)    #结果位200
'''

class Test(object):
    def __init__(self):
        self.__num = 100    #加“__”问私有属性

t = Test()
print(t.__num)
'''
程序报错
Traceback (most recent call last):
  File "D:/PycharmProjects/Python/study2/day1/09私有化/01pdb调试--pdb.set().py", line 20, in <module>
    print(t.__num)
AttributeError: 'Test' object has no attribute '__num'
'''