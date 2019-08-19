#coding=utf-8
#必须写编码集

from socket import *
import os
#定义广播ip，以及接收端端口
dest = ('<broadcast>',8080)

#创建套接字
udpSocket=socket(AF_INET,SOCK_DGRAM)

#绑定端口
udpSocket.bind(("",7890))

#对需要广播的套接字进行进一步修改，否则不能使用广播
udpSocket.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

#以广播形式发送数据到本网络中的所有电脑
udpSocket.sendto(b"Hi,nihao",dest)



print("等待对方回复，(按Ctrl+C可以退出)：")


while True:
	content,address = udpSocket.recvfrom(1024)
	print(content)
	print(address)
