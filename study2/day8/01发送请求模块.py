'''
首先导入struct模块
'''
import struct
from socket import *

sendData = struct.pack("!H8sb5sb",1,b"test.png",0,b"octet",0)
'''
!H8sb5sb详解
！:使用大端传输
H:用来接受将来请求的2个字节的1(读-下载)/2(写-上传)
8s:文件名长度为8
b:传输时需要的请求
5s:octet，模式
b:穿输时需要的请求
'''

udpSocket = socket(AF_INET,SOCK_DGRAM)
udpSocket.sendto(sendData,("10.217.11.92",69))

result = struct.unpack("!H",sendData[:2])
'''
上面使用H占用2个字节，把1替换到H，原本的1就是一个字节，这样以来，就满足协议需求，变成两个字节
同样，unpack解包，解得是两个字节，然后用H接受，转换成1个字节的数字
'''
print(result)
