#LEGB
'''
python解释器通过LFEGB顺序来找变量对应的值
locals-->enclosing function-->globals-->builtins
'''
num = 100
def test1():
    num = 200
    def test2():
        #num = 300
        print (num)
    return test2
ret = test1()
ret()