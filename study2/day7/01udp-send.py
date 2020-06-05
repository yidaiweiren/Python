from socket import *

#创建一个套接字
udpSocket = socket(AF_INET,SOCK_DGRAM)

#发送给谁
udpSocket.sendto(b"haha",("127.0.0.1",8080))