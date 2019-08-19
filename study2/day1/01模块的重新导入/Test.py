#reload重新导入修改后的模块
#此操作在交互模式中运行
#先写原版，交互模式中导入，然后在修改，交互模式打不出修改后的值，必须才去reload方法
#交互模式只能打开导入时的版本
def test():
    print ("-----原版-----")
    print ("-----修改后-----")


'''
过程结果：先打印未修改的
In [2]: import Test

In [3]: Test.test()
-----原版-----

'''

'''
过程结果：现在修改模块，再打印。发现结果未打印修改后的
In [5]: import Test

In [6]: Test.test()
-----原版-----

In [7]:
'''

'''
过程结果：使用reload（）方法打印修改后的
In [1]: import Test

In [2]: Test.test()
-----原版-----

In [3]: from imp import *
D:\python\Anaconda3\Scripts\ipython:1: DeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses

In [4]: reload(Test)
Out[4]: <module 'Test' from 'D:\\PycharmProjects\\Python\\study2\\day1\\Test.py'>

In [5]: Test.test()
-----原版-----
-----修改后-----

In [6]:
'''