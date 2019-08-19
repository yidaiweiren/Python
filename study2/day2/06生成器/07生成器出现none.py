'''
send和next的相同点：都可以执行一次，让程序向下走一步
不同点时send可以传一个值，而这个值可以给“yield i”这个表达式，相当与“yield i” = send("value")
send不能第一次执行，如果第一次执行程序直接崩
'''

def test():
    i = 0
    while i<5:
        temp = yield i
        print(temp)
        i+=1

t = test()
print(t.__next__())
print(t.__next__())

'''
结果中出现了none
0
None
1
None
2
'''

#使用send方法
t.send("haha")

'''
0
None
1
haha
'''