from socket import *
import struct
import os

def main():
	#0.获取要下在文件名
	downloadFilename = bytes(input("请输入要下载的文件名："),"utf-8")	#字符串转换为字节
	#print(type(downloadFilename))
	#print(len(downloadFilename))


	#1.创建socket
	udpSocket = socket(AF_INET,SOCK_DGRAM)
	#1.1封装请求数据包
	requestFileData = struct.pack("!H%dsb5sb"%len(downloadFilename),1,downloadFilename,0,b"octet",0)

	#2.发送下载文件的请求
	udpSocket.sendto(requestFileData,("10.217.11.86",69))


	flag = True	#表示可以下载数据，如果是False，那就删除数据
	num = 0
	f = open(downloadFilename,"bw")

	while True:
		#3.接受返回的数据
		responseData = udpSocket.recvfrom(1024)
		print(responseData)

		#3.1对接收的数据进行解包
		recvData,serverInfo = responseData

		#3.2对tftp协议返回来的“回应数据”解包
		opNum = struct.unpack("!H",recvData[:2])
		print("操作码=%d"%opNum[0])

		packetNum = struct.unpack("!H",recvData[2:4])

		print("文件块编号=%d"%packetNum[0])


		#3.3如果服务器发送过来的是文件的内容的话：
		if opNum[0] == 3:	#因为opNum返回的是一个元祖，所以使用下标提取[0]

			#计算出这次应该接收到的文件的序号值，应该是上一次接收到的值的基础上+1
			num = num+1

			#如果接受一个特别大的文件，即接收数据包编号大于2个字节，那么会从0继续开始，所以这里要使用判断，如果超过了65535，就将num改为0
			if num == 65535:
				num = 0


			#判断这次接收数据包的编号，是否为上一次编号+1，如果是，继续写入，如果不是，就不能写入了（因为会重复某一块数据，或者丢失某一块数据）
			if num == packetNum[0]:
				#把数据写入到文件中
				f.write(recvData[4:])
				num = packetNum[0]


			#3.4整理ACK的数据包。ACK:返回给服务器的接收信息确认码
			ackData = struct.pack("!HH",4,packetNum[0])	#4是返回给服务器的确认操作码tftp协议规定的
			udpSocket.sendto(ackData,serverInfo)

		elif opNum[0] == 5:
			print("Sorry,服务器好像没有这个文件。。。")
			flag = False

		#判断文件是否传输完毕，传输完毕文件小于516字节
		print("本次接收的数据长度为：%d"%len(recvData))
		if len(recvData)<516:
			print("文件下载完毕！")
			break

	if flag == True:
		f.close()	#关闭文件
	else:
		os.unlink(downloadFilename)	#如果没有找到要下载文件，就把刚才创建的文件删除



if __name__ == "__main__":
	main()