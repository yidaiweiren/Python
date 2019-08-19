'''
异步:正在干一件事，但不确定什么时候干完，这时又让去干另一件事，干完另一件事，又返回来干原来的事

同步：我干完这件事，再去干另一件事
'''

from multiprocessing import Pool
import time
import os


def test():
	print("-----进程池中的进程--pid=%d--ppid=%d-----"%(os.getpid(),os.getppid()))
	for i in range(3):
		print("-----%d-----"%i)
		time.sleep(1)
	return "haha"

def test2(args):
	print("-----callback func--pid=%d-----"%os.getpid())
	print("-----callback func--args=%s-----"%args)


pool = Pool(3)
pool.apply_async(func=test,callback=test2)

#time.sleep(5)
#print("-----主进程--pid=%d-----"%os.getpid())

while True:
	time.sleep(1)
	print("-----主进程--pid=%d-----"%os.getpid())