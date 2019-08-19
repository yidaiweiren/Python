#垃圾回收--gc

import gc
class ClassA():
    def __init__(self):
        print("object born,id:%s"%str(hex(id(self))))

def f2():
    while True:
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1
        del c1
        del c2
        gc.collect()    #手动垃圾回收
        print(gc.garbage)   #清理的垃圾列表
#把python的gc功能关闭
gc.disable()
f2()