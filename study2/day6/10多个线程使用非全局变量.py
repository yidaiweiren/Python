'''
线程共享全局变量的问题:如果用不好，计算结果就出错了

线程执行的过程中，函数里的变量，各是各的，不共享

非全局变量，不需要加锁
'''
from threading import Thread
import threading
import time


def test1():
	name = threading.current_thread().name
	print("-----thread name is %s"%name)
	g_num = 100
	if name == "Thread-1":
		g_num+=1
	else:
		time.sleep(2)
	print("-----thread is %s, g_num is %d-----"%(name,g_num))

#def test2():
#	time.sleep(1)
#	g_num = 100
	#g_num+=1
#	print("-----in test2, g_num is %d-----"%g_num)


p1 = Thread(target=test1)
p1.start()



p2 = Thread(target=test1)
p2.start()

