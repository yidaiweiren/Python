'''
动态的添加一个静态方法
'''
class P(object):
    def __init__(self,newName):
        self.name = newName

def run(self):
        print ("-----%s正在吃-----"%self.name)

@staticmethod
def test():
    print ("-----staticmethos-----")

p1 = P("p1")
p2 = P("p2")

import types
p1.run = types.MethodType(run,p1)
p1.run()

P.test = test   #静态方法跟类走，实例方法跟对象走
P.test()
P.xx = test
P.xx()
