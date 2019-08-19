'''
生成器的第一种创建方式:将生成式的列表中括号改为元组的圆括号
当使用next（）方法调用到最后一个值的洗一个值，程序就会崩掉
'''

a = [x*2 for x in range(10)]
print(a)

#生成器
b = (x*2 for x in range(10))
print(b)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
