#coding=utf-8
from multiprocessing import Manager,Pool
import os,time,random

#写数据进程执行的代码：
def write(q):
	for value in ['A','B','C','D']:
		print("正在将-%s-添加到队列。。。"%value)
		q.put(value)
		time.sleep(random.random())


#读数据进程执行的代码：
def read(q):
	while True:
		if not q.empty():
			value = q.get(True)
			print("从消息队列中获取到--%s。"%value)
			time.sleep(random.random())
		else:
			break






if __name__ == "__main__":

	print("(%s) start"%os.getpid())

	#使用Manager中的Queue来初始化
	q = Manager().Queue()

	#创建进程池
	po = Pool()

	#将创建的队列传给子进程
	po.apply(write,(q,))
	po.apply(read,(q,))


	po.close()
	po.join()

	print("")
	print("(%s) end"%os.getpid())

'''
结果
(55973) start
正在将-A-添加到队列。。。
正在将-B-添加到队列。。。
正在将-C-添加到队列。。。
正在将-D-添加到队列。。。
从消息队列中获取到--A。
从消息队列中获取到--B。
从消息队列中获取到--C。
从消息队列中获取到--D。

(55973) end
'''