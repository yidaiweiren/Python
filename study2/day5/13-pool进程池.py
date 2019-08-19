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
	pool.apply_async(worker,(i,))
'''
pool.apply_asynnc():向进程池中添加任务
注意：如果添加的任务数量，超过了进程池中进程的个数，这种情况下，不会出现添加不进去的情况。
	 添加到进程中的任务，如果还没有被执行，那么他们将会等待进程池执行完当前的进程，然后再添加进去执行，自动的使用刚刚执行完的这个进程。然后完成当前的新任务。  
'''


print("-----start-----")

pool.close()
pool.join()
'''
join:主进程 创建/添加 任务后，主进程 默认不会等待进程池中的任务执行完后才结束。而是当主进程，任务做完后，立马结束。
如果这个地方没有join，会导致进程池中的任务不会执行
'''

print("-----end-----")