from socket import *
from threading import Thread
import time

#创建udp套接字
udpSocket = socket(AF_INET,SOCK_DGRAM)

#准备接受方地址
sendAddr = ("10.217.11.92",8080)


while True:
	#从键盘获取发送内容
	Data = "haha,i am ghost--^w^!!!!!"
	sendData = Data.encode()
	print(sendData)
	time.sleep(0.5)


	#发送到指定电脑上
	udpSocket.sendto(sendData,sendAddr)



