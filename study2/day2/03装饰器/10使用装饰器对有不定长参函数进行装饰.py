#使用装饰器对无参函数进行装饰
def func(functionName):
    print ("-----func-1-----")
    def func_in(*args,**kwargs):   #如果a和b没有定义，那么会导致19,20行调用失败
        print ("-----func_in-1-----")
        functionName(*args,**kwargs)   #如果a和b当作实参进行传递，呢么会导致12,16行无法调用
        print ("-----func_in_2-----")
    print ("-----func-2-----")
    return func_in

@func
def test(a,b,c):
    print ("-----test,a=%d,b=%d,c=%d-----"%(a,b,c))

@func
def test2(a,b,c,d):
    print ("-----test,a=%d,b=%d,c=%d,d=%d-----"%(a,b,c,d))

test(11,22,33)
test2(11,22,33,44)