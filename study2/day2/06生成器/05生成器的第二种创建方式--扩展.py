'''
生成器的第二种创建方式
只要出现yield就是代表生成器
当程序执行到yield，就会停止，会把yield后面的值返回。如果再次执行next，那么就会继续从“原来停止的地方”继续执行
'''
'''
斐波那契数列：第三个数等于前两个数之和
1，2，3，5，8···
'''

def createNum():
    print("-----start-----")
    a,b = 0,1
    for i in range(5):
        print("-----yield-1-----")
        yield b
        print("-----yield-2-----")
        a,b = b,a+b
        print("-----yield-3-----")
    print("-----stop-----")

createNum() #交互模式下调用，返回的时一个对象

#创建一个生成器对象
a = createNum()

for num in a:
    print(num)


