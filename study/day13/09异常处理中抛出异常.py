#异常处理中抛出异常

class  Test(object):
    def __init__(self,switch):
        self.switch = switch
    def calc(self,a,b):  #calc:释义为“计算”
        try:
            return a/b
        except Exception as result:
            if self.switch:
                print ("捕获开启，已捕获到异常，异常信息为：%s"%result)
            else:
                raise   #在这个异常处理中，再抛出异常给python解释器

a = Test(True)
a.calc(11,0)
'''
捕获开启，已捕获到异常，异常信息为：division by zero
'''

print ("#####################################################")

a.switch = False
a.calc(11,0)
'''
Traceback (most recent call last):
  File "D:/PycharmProjects/Python/study/day13/09异常处理中抛出异常.py", line 22, in <module>
    a.switch = False
NameError: name 'a' is not defined
'''