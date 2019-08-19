#三个数字求和

#1.获取3个数字
num1=int(input("请输入第1个数字："))
num2=int(input("请输入第2个数字："))
num3=int(input("请输入第3个数字："))

#需要使用一个函数来接收并处理
def num_3_sum(a,b,c):
    result=a+b+c
    print ("%d+%d+%d=%d"%(a,b,c,result))

num_3_sum(num1,num2,num3)

'''
请输入第1个数字：123
请输入第2个数字：234
请输入第3个数字：233
123+234+233=590
'''