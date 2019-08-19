'''
模仿qq聊天
难点：系统要么发要么收，没有任务就卡住，不发收不了，收了发不了
解决办法：利用多线程解决堵塞
元祖套元祖取数据：
In [1]: a=(1,2,3,(4,5))                                                                   

In [2]: a[0]                                                                              
Out[2]: 1

In [3]: a[3]                                                                              
Out[3]: (4, 5)

In [4]: a[3][1]                                                                           
Out[4]: 5

In [5]: a[3][0]                                                                           
Out[5]: 4

'''
from threading import Thread
from socket import *

#1.收数据
def recvData():
	#收到就打印
	while True:
		recvInfo = udpSocket.recvfrom(1024)
		print("\r>>来自于%s的%s端口的信息:\n>>%s"%(str(recvInfo[1][0]),str(recvInfo[1][1]),recvInfo[0].decode("GB2312"))+"\n<<")
		#print("<<")


#2.发数据
def sendData():
	#不用结束，持续聊天
	while True:
		sendInfo = input("<<")
		udpSocket.sendto(sendInfo.encode("GB2312"),(destIP,destPort))
		


udpSocket = None
destIP = ""	#IP是str类型
sestPort = 0	#端口是int类型

#让两个线程都到main中执行
def main():

	
	global udpSocket	#udpSocket别的函数用不了，所以声明为全局变量，这里将全局变量的None修改为套接字对象，其他函数也能使用
	global destIP
	global destPort

	#创建保存对方的主机的信息
	destIP = input("对方的ip:")
	destPort = int(input("对方的端口:"))

	#创建套接字
	udpSocket = socket(AF_INET,SOCK_DGRAM)

	#绑定端口
	udpSocket.bind(("",4567))

	#创建两个线程
	tr = Thread(target=recvData)
	ts = Thread(target=sendData)

	#开启两个主线程
	tr.start()
	ts.start()

	#主线程等待子线程执行完毕，用join
	tr.join()
	ts.join()

if __name__ == "__main__":
	main()