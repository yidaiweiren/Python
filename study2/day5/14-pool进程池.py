'''
pool:进程池

close:关闭进程池，关闭之后不在接收新的请求

'''

from multiprocessing import Pool
import os
import random
import time

def worker(num):
	for i in range(5):
		print("=====pid=%d--num=%d====="%(os.getpid(),num))
		time.sleep(1)

pool = Pool(3)
'''
Pool(3)：表示进程池中最多有三个任务共同执行
'''

for i in range(10):
	print("-----%d-----"%i)
	pool.apply(worker,(i,))
'''
pool.apply():堵塞方式执行进程，执行一次i，然后执行5次pid，然后在执行下一个i。。。。。。
 
'''


print("-----start-----")

pool.close()
pool.join()
'''
join:主进程 创建/添加 任务后，主进程 默认不会等待进程池中的任务执行完后才结束。而是当主进程，任务做完后，立马结束。
如果这个地方没有join，会导致进程池中的任务不会执行
'''

print("-----end-----")