#coding=utf-8

from socket import *

#创建套接字
clientSocket = socket(AF_INET,SOCK_STREAM)

#创建链接
clientSocket.connect(("10.131.198.122",9991))

#向服务器发送数据
#tcp客户端已经连接好了服务器，所以直接发送就行，在以后的发送中，不需要填写对方ip和port--》打电话
#udp发送数据时，因为没有提前链接，每次都需要填写对方ip和port--》写信
clientSocket.send("你好".encode("GB2312"))

#接收服务器传回的数据
recvData = clientSocket.recv(1024)
print("[来自于服务器的消息]:%s"%recvData.decode("GB2312"))

clientSocket.close()
