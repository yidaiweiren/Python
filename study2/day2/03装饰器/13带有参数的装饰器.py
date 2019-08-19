#使用装饰器对无参函数进行装饰
def func_arg(arg):
    print ("-----func_arg-1-----")
    def func(functionName):
        print ("-----func-1-----")
        def func_in():
            print ("-----记录日志-arg=%s-----"%arg)
            print ("-----func_in-1-----")
            if arg=="heihei":
                functionName()
                functionName()
            else:
                functionName()
            print ("-----func_in_2-----")
            print ("*#"*25)
        print ("-----func-2-----")
        print ("$&"*25)
        return func_in
    print ("-----func_arg-2-----")
    print ("-="*25)
    return func

'''
1.先执行func_agrs("heihei")函数，这个函数return的结果就是func这个函数的引用
2.相当于返回了@func
3.使用@func对test进行装饰
'''
@func_arg("heihei")
def test():
    print ("-----test-----")

#带有参数的装饰器，能够起到在运行时，有不同的功能
@func_arg("haha")
def test2():
    print ("-----test2-----")

test()
test2()