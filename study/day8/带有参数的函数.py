#带有参数的函数

#引入
'''
此程序太过死板，智能计算固定
def sum_2_num():
    a=10
    b=20
    result=a+b
    print ("%d+%d=%d"%(a,b,result))

#输出函数结果
sum_2_num()

10+20=30
'''
def sum_2_num(a,b):     #封装函数，使用a,b两个变量来存储input传进来的值
    #a=10
    #b=20
    result=a+b
    print ("%d+%d=%d"%(a,b,result))
num1=int(input ("请输入第一个数字:"))
num2=int(input ("请输入第二个数字:"))
#输出函数结果
sum_2_num(num1,num2)     #调用的时候可以直接将num1和num2“作为参数”传入函数中，但必须保持一一对应，也就是说num1-->a,num2-->b
'''
请输入第一个数字:999
请输入第二个数字:123
999+123=1122
'''