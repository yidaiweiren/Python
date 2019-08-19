#使用装饰器对无参函数进行装饰
def func(functionName):
    print ("-----func-1-----")
    def func_in(a,b):   #如果a和b没有定义，那么会导致15行调用失败
        print ("-----func_in-1-----")
        functionName(a,b)   #如果a和b当作实参进行传递，呢么会导致12行无法调用
        print ("-----func_in_2-----")
    print ("-----func-2-----")
    return func_in

@func
def test(a,b):
    print ("-----test,a=%d,b=%d-----"%(a,b))

test(11,22)