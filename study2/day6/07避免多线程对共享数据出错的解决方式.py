'''
线程共享全局变量的问题:如果用不好，计算结果就出错了
'''
from threading import Thread
import time

g_num = 0
g_flag = 1

def test1():
	global g_num
	global g_flag

	if g_flag == 1:
		for i in range(1000000):
			g_num+=1
		g_flag = 0
	
	print("-----in test1, g_num is %d-----"%g_num)

def test2():
	global g_num

	#轮询
	while True:
		if g_flag != 1:
			for i in range(1000000):
				g_num+=1
			break

	print("-----in test2, g_num is %d-----"%g_num)


p1 = Thread(target=test1)
p1.start()

#time.sleep(3)

p2 = Thread(target=test2)
p2.start()

print("-----g_num = %d-----"%g_num)