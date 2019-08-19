from socket import *

#模块化思想--封装成函数
def main():
	udpSocket = socket(AF_INET,SOCK_DGRAM)

	#绑定端口
	udpSocket.bind(("",7788))

	while True:
		#收，打印
		recvData = udpSocket.recvfrom(1024)

		#拆包
		content,recvInfo = recvData

		ip,port = recvInfo


		print("[来自于%s的%s端口的消息]：%s"%(ip,port,content.decode("GB2312")))


if __name__ == "__main__":
	main()