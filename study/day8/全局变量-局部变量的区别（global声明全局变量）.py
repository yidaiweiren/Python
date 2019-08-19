#全局变量-局部变量的区别
#显示当前温度

#传统方法做，局部变量传给局部变量
'''
#模块1，获取温度
def get_wendu():
    wendu=33
    return wendu

#模块2，显示温度
def print_wendu(Wendu):
    print ("温度是%d"%Wendu)

result=get_wendu()

print_wendu(result)

#结果为：温度是33
'''

#定义一个全局变量wendu
wendu=0
'''
思路
定义全局变量wendu
执行get_wendu()函数，将温度值修改为33
结束get_wendu()函数，程序继续执行
执行print_wendu()函数，获取修改过后的wendu
结束print_wendu()函数
'''

#模块1，获取温度
def get_wendu():
    #如果wendu这个变量已经在全局进行定义了，此时想在函数中对这个全局变量做修改，wendu=33显然是不行的
    #在wendu=33前面添加global wendu即可直接修改全局变量wendu
    #使用global来声明一个全局变量，而声明过后，这个变量将不再是一个局部变量，而是对全局变量的修改
    global wendu
    wendu=33


#模块2，显示温度
def print_wendu():
    print ("温度是%d"%wendu)

get_wendu()

print_wendu()
