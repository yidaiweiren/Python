#一个函数中有多个return
#封装函数中只要有一个renturn，执行至此，这个函数就执行完毕
#return后面可以跟列表，元组，字符串，字典等
#一个函数要想返回多个值，不能用多个return实现
#return可以用来结束函数

def test():
    a=11
    b=22
    c=33
    #第1中，可以使用列表来封装3个变量
    #d=[a,b,c]  #也可直接写成return [a,b,c]
    #return d
    #return [a,b,c]
    return (a,b,c)
print (test())
'''
第1种：使用列表封装 [11, 22, 33]
第2种：使用元组封装 (11, 22, 33)
'''