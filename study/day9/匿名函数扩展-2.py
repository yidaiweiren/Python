#coding=utf-8
#匿名函数扩展-2

#使用匿名函数当作实参
def test2(a,b,func):
    result=func(a,b)
    return result
#动态的实现一些功能
#python2中实现
#new_func=input("请输入一个匿名函数：")

#python3中的实现，加eval()方法
new_func=eval(input("请输入一个匿名函数："))      #eval()类似于int()取整一样。eval将带有双引号的“str”，转换为不带双引号的str
nums2=test2(11,22,new_func)
print (nums2)
'''
请输入一个匿名函数：lambda x,y:x+y
33

请输入一个匿名函数：lambda x,y:x*y+100+200    还可以自己添加一些值
542

'''
