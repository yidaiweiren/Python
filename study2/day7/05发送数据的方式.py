from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)

destIP = input("请输入目标IP:")
destPort = int(input("请输入目标端口："))
sendData = input("请输入要发送的数据:")

udpSocket.sendto(sendData.encode("GB2312"),(destIP,destPort))