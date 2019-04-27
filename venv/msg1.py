from socket import *
from time import ctime
HOST = ''
PORT = 23333
BUFSIZ = 1024
ADDR = (HOST,PORT)
tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(1)

while True:
  print('Waiting for message...')
  tcpCliSock,addr = tcpSerSock.accept()
  print('...message from:',addr)
  while True:
    data = tcpCliSock.recv(BUFSIZ)
    #if not data:
    #  break
    print(ctime())
    print(data.decode())
    message = input("Plase input send message > ")
    if message == 'q':
      tcpCliSock.close()
      tcpSerSock.close()
      break
    tcpCliSock.send(message.encode())
    print("Message alreaed send,Plase wait...")
  tcpCliSock.close()
tcpSerSock.close()