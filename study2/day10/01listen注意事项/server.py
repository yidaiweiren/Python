#coding=utf-8
from socket import *
from time import sleep


##创建socket套接字
tcpSerSocket = socket(AF_INET,SOCK_STREAM)

#绑定本地信息
address = ("",37788)
tcpSerSocket.bind(address)

#定义最大连接数
connNum = int(input("请输入需要最大的连接数："))


#使用socket创建的套接字默认属性是主动的，使用listen将其变为被动，这样就可以接受别人的连接了
tcpSerSocket.listen(connNum)

#如果有新的客户端链接，那么就产生一个新的套接字来为这个客户端服务
for i in range(10):
	print(i)
	sleep(1)

print("延时结束。。。")

while True:
	newSocket,clientAddr = tcpSerSocket.accept()
	print(tcpSerSocket.accept())
	print("+"*40)

	print(newSocket)
	print("="*40)
	print(clientAddr)
	sleep(1)