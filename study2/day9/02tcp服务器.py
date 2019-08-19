#coding=utf-8

from socket import *

#创建tcp套接字
serverSocket = socket(AF_INET,SOCK_STREAM)

#绑定
serverSocket.bind(("",9990))

#主动套接字变被动套接字，监听。相当于等电话响
serverSocket.listen(5)	#最多有5个客户端给他发送数据，相当于10086，同时可有有多人给10086打电话


#等待客户端链接
#相当于等待接听，类似于10086只负责呼入，呼入后转入其他人工坐席，释放10086这个链接
print("-----1-accept-----")
clientSocket,clientInfo = serverSocket.accept()
#accept()的返回值是元祖
#clienSocket:表示这个新的客户端
#clientInfo:表示这个新的客户端的ip以及port

#客户端接收用户的数据 
print("-----2-recv-----")
recvData = clientSocket.recv(1024)
print("-----3-----")
print("来自于%s的消息:%s"%(str(clientInfo),recvData.decode("GB2312")))



#使用完关闭套接字,先关闭client，在关闭server
clientSocket.close()
serverSocket.close()
