'''
动态的添加一个静态方法
'''
class P(object):
    def __init__(self,newName):
        self.name = newName

def run(self):
        print ("-----%s正在吃-----"%self.name)

@classmethod
def printNum(cls):
    print ("-----classmethos-----")

p1 = P("p1")
p2 = P("p2")

import types
p1.run = types.MethodType(run,p1)
p1.run()

P.printnum = printNum   #静态方法跟类走，实例方法跟对象走
P.printnum()
P.printnum = printNum
P.printnum()
