'''
join([timeout]):是否等待进程实例执行结束，timeout选填参数，设置等待时间
#堵塞  当程序走到这个位置时，如果上面还有紫禁城没有执行完，程序会一直在这里等待
#解堵塞，当条件慢走后在继续执行（相当于子进程执行完）

terminate()：不管进程有没有结束，直接干死
'''

from multiprocessing import Process
import os
import time
import random


def test():
	for i in range(random.randint(1,5)):
		print("-----%d-----"%i)
		time.sleep(1)

p = Process(target=test)

p.start()

p.join(1)	#1s后结束主进程，不等待
#p.join()	#堵塞  当程序走到这个位置时，如果上面还有紫禁城没有执行完，程序会一直在这里等待
#解堵塞，当条件慢走后在继续执行（相当于子进程执行完）


p.terminate()

print("-----main-----")


'''
结果
----0-----
-----1-----
-----2-----
-----3-----
-----4-----
-----main-----

'''