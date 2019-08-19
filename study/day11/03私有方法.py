#-*-coding:utf-8-*-
#私有方法
#私有方法：不能直接调用
#共有方法：可以在外面直接调用
'''
使用短信网关发短息（调用这个发信方法）
    1.不能直接发送短信（所以发信方式为私有方法）
    2.判断余额是否够用，够用在调用发信方法，不够不调用

'''
class Dog:
    def __send_msg(self):  #"__send_msg"为私有方法
        print ("-----正在发送短信-----")

    def send_msg(self,new_money):     #send_msg为公有方法
        if new_money>10000:
            self.__send_msg()
        else:
            print ("余额不足，请先充值")


dog = Dog()
dog.send_msg(100000)