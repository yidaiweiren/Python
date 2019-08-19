#使用range()函数输出1-20的平方
#思路
#使用for循环出每个数字
#当循环一次去除的数字进行平方运算
#“**”表示乘方运算符
str=[]
for numm in range(1,21):
    value=numm**2
    str.append(value)
    print (str)     #没有正确缩进
print(str)      #有正确缩进

#结果
'''
[1]
[1, 4]
[1, 4, 9]
[1, 4, 9, 16]
[1, 4, 9, 16, 25]
[1, 4, 9, 16, 25, 36]
[1, 4, 9, 16, 25, 36, 49]
[1, 4, 9, 16, 25, 36, 49, 64]
[1, 4, 9, 16, 25, 36, 49, 64, 81]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
'''