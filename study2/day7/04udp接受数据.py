from socket import *

#创建一个套接字
udpSocket = socket(AF_INET,SOCK_DGRAM)

udpSocket.bind(("",7788))
'''
接收数据必须绑定端口

本机的7788端口，“”空字符中写本地ip，为避免本地多网卡，所以此处不写，若需要单独到指定网卡，那么就填写ip
如果指定发送端口，接收方会接受一坨连在一起的信息，不换行
一般情况下，发送方不需要绑定。
但是接收方必须绑定
'''

#接受信息
while True:
	recvData = udpSocket.recvfrom(1024)	#接受的最大数据为1024字节

	print(recvData)