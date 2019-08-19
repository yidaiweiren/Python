from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)

udpSocket.bind(("",7788))

recvData = udpSocket.recvfrom(1024)

content,destInfo = recvData

#对ip，端口解包
ip,port = destInfo
'''
解包
a=(11,22)
c,d = a
c=11
d=22
'''

print("来自于%s的%s端口的消息："%(ip,port)+"\n"+content.decode("GB2312"))
