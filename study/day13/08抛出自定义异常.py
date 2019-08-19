#抛出自定义异常

#创建一个自定义异常类
class ShortInputException(Exception):   #Exception作为所有异常的父类，这里我们的自定义异常可以继承Exception
    def __init__(self,length,atlease):  #atlease：释义为“至少”
        self.length = length
        self.atlease = atlease

def main():
    try:
        s = input("请输入-->")
        if len(s)<3:
            #raise引发一个你定义的异常
            raise ShortInputException(len(s),3)

    except ShortInputException as result:
        print ("ShortInputException:输入的长度是：%d，规定的长度至少应该是%d。result的结果是：%s"%(result.length,result.atlease,result))

    else:
        print ("-----没有异常-----")

main()

'''
请输入-->1
ShortInputException:输入的长度是：1，规定的长度至少应该是3。result的结果是：(1, 3)
'''