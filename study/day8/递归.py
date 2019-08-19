#-*-coding:utf-8-*-
#递归:函数在自己的函数中调用自己
#计算一个数字的阶乘

#老方法求阶乘
'''
i=1
result=1
while i<=5:
    result*=i
    i+=1
print (result)
'''

def getNums(num):
    if num>1:
        return num * getNums(num-1)
    else:
        return num
result=getNums(5)
print (result)