'''
为了防止别人使用“from msgnew import *”导入所有功能，这里可以使用__all__=[]方法来限定别人使用的功能。
列表中写哪个，可以使用哪个；不写的不能用，会直接报错
仅限于“from msgnew import *”调用方法
'''
__all__ = ["test1","Test"]

def test1():
    print ("-----msgnew/test1-----")

def test2():
    print ("-----msgnew/test2-----")

class Test(object):
    pass