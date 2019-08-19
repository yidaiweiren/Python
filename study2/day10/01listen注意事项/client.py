#coding=utf-8
from socket import *


connNum = int(input("请输入连接服务器的次数："))
print (type(connNum))
for i in range(connNum):
	print(i)
	s=socket(AF_INET,SOCK_STREAM)
	s.connect(("10.131.198.122",37788))
	print(i)
