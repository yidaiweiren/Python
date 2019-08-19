'''
兼容全平台的fork，windows也可以使用

模块：multiprocessing

process创建的进程，主进程要等待所有的子进程都执行完毕才关闭，这点不同于fork
'''

from multiprocessing import Process
import os
import time




def test():
	for i in range(5):
		print("-----test-----")
		time.sleep(1)
p = Process(target=test)	#把要执行的test函数放到Process中

p.start()	#开始进程。这个程序开始执行test中的代码


'''
结果：主进程没有挂掉
-----test-----
-----test-----
-----test-----
-----test-----
-----test-----

'''