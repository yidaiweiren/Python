#装饰器
'''
需求
实现一个模拟调用验证功能
'''

def w1(func):
    def inner():
        print("-----正在验证权限-----")
        func()      #此处相当于闭包，只是在此处扩展为：“传入另一个函数的引用”
    return inner

def f1():
    print("-----f1-----")

def f2():
    print("-----f2-----")

innerFunc = w1(f1)  #详情可以查阅上节“闭包”
innerFunc()

innerFunc = w1(f2)
innerFunc()


'''
老方法
def w1():
    print ("-----正在验证权限-----")
    
def f1():
    w1()
    print("-----f1-----")
f1()
结果
-----正在验证权限-----
-----f1-----
'''
