#三个数字求平均值
#修改求和的代码，迭代更新

#1.获取3个数字
num1=int(input("请输入第1个数字："))
num2=int(input("请输入第2个数字："))
num3=int(input("请输入第3个数字："))

#需要使用一个函数来接收并处理
def num_3_sum(a,b,c):
    result=a+b+c
    #print ("%d+%d+%d=%d"%(a,b,c,result))
    return result      #将计算结果返回给返回average_3_num函数


def average_3_num(a1,b1,c1):    #拿到用户输入的数字。也叫“形参”
    result=num_3_sum(a1,b1,c1)      #调用函数--将数值传递到num_3_sum函数，使用num_3_sum函数进行计算
    result=result/3     #可以写成result/=3，将拿到的num_3_sum的返回结果进行求平均值计算
    print ("平均值为：%d"%result)
average_3_num(num1,num2,num3)   #实参

'''
请输入第1个数字：1222
请输入第2个数字：2224
请输入第3个数字：4446
平均值为：2630
'''