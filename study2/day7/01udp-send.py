from socket import *

#创建一个套接字
udpSocket = socket(AF_INET,SOCK_DGRAM)

#发送给谁
udpSocket.sendto(b"haha",("10.217.11.92",8080))