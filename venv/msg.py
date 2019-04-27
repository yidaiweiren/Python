from socket import *
from time import ctime
import os
HOST = 'localhost'
PORT = 23333
BUFSIZ = 1024
ADDR = (HOST,PORT)
tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)
while True:
  data = input('Plase input  message > ')
  if data == 'q':
    data = "I'm quit talking"
    tcpCliSock.send(data.encode())
    tcpCliSock.close()
    break
  tcpCliSock.send(data.encode())
  print("Message alreaed send,Plase await message")
  data = tcpCliSock.recv(BUFSIZ)
  if not data:
    break
  print(ctime())
  print(data.decode('utf-8'))
tcpCliSock.close()