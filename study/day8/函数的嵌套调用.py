#函数的嵌套调用
def test1():
    pass
def test2():
    print ("---2-1---")
    print ("php")
    print ("---2-2---")
def test3():
    print ("---3-1---")
    #print ("hello python")
    test2()     #可以直接嵌套并且调用test2（）函数
    print ("---3-2---")

test3()

'''
---3-1---
---2-1---
php
---2-2---
---3-2---
'''

