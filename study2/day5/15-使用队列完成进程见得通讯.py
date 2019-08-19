from multiprocessing import Queue,Process
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

	#父进程创建一个队列
	q = Queue()

	#将创建的队列传给子进程
	pw = Process(target=write,args=(q,))
	pr = Process(target=read,args=(q,))


	#启动子进程pw
	pw.start()

	#等待pw进程执行完毕
	pw.join()

	#启动子进程pr
	pr.start()

	#等待pr进程执行完毕。注意，pr是死循环，必须强制终止，所以上面使用了break
	pr.join()

	print("")
	print("所有数据在队列中写入且读取完成")

'''
结果
正在将-A-添加到队列。。。
正在将-B-添加到队列。。。
正在将-C-添加到队列。。。
正在将-D-添加到队列。。。
从消息队列中获取到--A。
从消息队列中获取到--B。
从消息队列中获取到--C。
从消息队列中获取到--D。

所有数据在队列中写入且读取完成

'''