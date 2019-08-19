#使用装饰器对无参函数进行装饰
def func(functionName):
    print ("-----func-1-----")
    def func_in():
        print ("-----func_in-1-----")
        functionName()
        print ("-----func_in_2-----")
    print ("-----func-2-----")
    return func_in

def test():
    print ("-----test-----")

test = func(test)
test()