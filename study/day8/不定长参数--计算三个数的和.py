#-*-coding:utf-8-*-
#函数的缺省参数--计算三个数的和
#“*”代表传入的值没有多余变量接收的时候全部传递给“*”的变量，这个变量会生成一个元组


def sum_nums(a,b,c,*args):  #传递的实参的个数大于形参的个数，将多余的值全部扔给args。放在形参的最后一个位置
    print ("a=%d"%a)
    print ("b=%d"%b)
    print ("c=%d"%c)
    print (args)

    result=a+b+c
    for num in args:
        result+=num
    print ("result=%d"%result)      #计算的结果：result=495

sum_nums(11,22,33,44,55,66,77,88,99)
'''
a=11
b=22
c=33
(44, 55, 66, 77, 88, 99)    以元组形式展现
'''