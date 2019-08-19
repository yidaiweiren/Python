#-*-coding:utf-8-*-

a=100   #不可变类型  详见day8/3种不可变类型和2种可变类型

def test(num):
    num+=num
    print (num)
    print ("*"*10)
test(a)

print (a)
'''
200
**********
100
'''

b=[100]     #可变类型
def test1(num1):
    num1+=num1      #相当于列表+列表，相当于列表合并，列表是可以修改的，此处就相当于修改了全局变量
    print (num1)
    print ("*"*10)
test1(b)

print (b)
'''
[100, 100]
**********
[100, 100]
'''

#观察num2+=num2和num2=num2+num2的区别

c=[100]
def test2(num2):
    num2=num2+num2  #先计算等号右边的值，在把值给左边，左边相当于在内存中重新开了一块地方，与全局变量无关了，所以结果全局变量不变
    print (num2)
    print ("*"*10)
test2(c)

print (c)
'''
[100, 100]
**********
[100]
'''