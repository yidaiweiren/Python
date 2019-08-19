#使用装饰器对无参函数进行装饰
def func(functionName):
    print ("-----func-1-----")
    def func_in(*args,**kwargs):
        print("-----记录日志-----")
        print ("-----func_in-1-----")
        Ret = functionName(*args,**kwargs)
        print ("-----func_in_2-----")
        return Ret

    print ("-----func-2-----")
    return func_in

@func
def test():
    print ("-----test-----")
    return "haha"

@func   #无返回值
def test2():
    print ("-----test2-----")

@func   #有参数
def test3(a):
    print ("-----test3-a=%d-----"%a)

ret = test()
print ("test return values is %s"%ret)

a = test2()
print ("test2 return values is %s"%a)


test3(11)