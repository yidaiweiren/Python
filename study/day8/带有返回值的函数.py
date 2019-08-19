#带有返回值的函数
#每个函数中自己定义的变量只能在这个函数中使用，不能在其他函数中使用
#函数中return哪个变量，结果就是哪个变量

def get_wendu():
    wendu=22
    print ("当前的温度是%d摄氏度"%wendu)
    return wendu       #使用return返回温度变量的结果，这里也就是22


def get_wendu_huashi(wendu_huashi):     #使用“wendu_huashi”来接受result传递的参数（第一个函数的返回值）
    wendu_huashi=wendu_huashi+3
    print ("当前的温度是%d华氏度"%wendu_huashi)
#get_wendu()

result=get_wendu()     #定义一个变量来接收return返回来的结果
#print (result)      #打印这个返回值

print ("="*20)
get_wendu_huashi(result)      #将这个接收返回值的变量做为参数再传递给函数get_wendu_huashi
