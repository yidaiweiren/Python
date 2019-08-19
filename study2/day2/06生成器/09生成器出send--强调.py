'''
send和next的相同点：都可以执行一次，让程序向下走一步
不同点时send可以传一个值，而这个值可以给“yield i”这个表达式，相当与“yield i” = send("value")
send不能第一次执行，如果第一次执行程序直接崩
    如果非得调用，第一次请写“send(None)”,第二次可以写“send("haha")”
'''

def test():
    i = 0
    while i<5:
        temp = yield i
        print(temp)
        i+=1

t = test()

print(t.send(None))

#使用send方法
print(t.send("haha"))

'''
0
haha
1
'''