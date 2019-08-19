'''
兼容全平台的fork，windows也可以使用

模块：multiprocessing
'''

from multiprocessing import Process
import os
import time


def test():
	while True:
		print("-----test-----")
		time.sleep(1)
p = Process(target=test)	#把要执行的test函数放到Process中,创建完不会执行，当调用.start时才执行

p.start()	#开始进程。这个程序开始执行test中的代码

while True:
	print("-----main-----")
	time.sleep(1)


'''
结果
-----main-----
-----test-----
-----main-----
-----test-----
-----main-----
-----test-----
-----main-----
-----test-----
-----main-----
-----test-----
-----main-----
-----test-----


'''