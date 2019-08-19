#使用装饰器对无参函数进行装饰
def func(functionName):
    print ("-----func-1-----")
    def func_in():
        print ("-----func_in-1-----")
        Ret = functionName()    #保存返回来的haha
        print ("-----func_in_2-----")
        return Ret  #把haha返回到17行的调用

    print ("-----func-2-----")
    return func_in

@func
def test():
    print ("-----test-----")
    return "haha"
ret = test()
print ("test ruturn values is %s"%ret)