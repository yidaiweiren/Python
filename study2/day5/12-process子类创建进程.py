
'''
start()一定会自己调用run方法
'''
from multiprocessing import Process
import time

class MyNewProcess(Process):
	def run(self):
		while True:
			print("-----1-----")
			time.sleep(1)


p = MyNewProcess()

p.start()


#主进程
while True:
	print("-----main-----")
	time.sleep(1)

'''
结果
-----main-----
-----1-----
-----1-----
-----main-----
-----1-----
-----main-----
-----1-----
-----main-----
-----main-----
-----1-----

'''