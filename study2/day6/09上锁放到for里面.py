'''
线程共享全局变量的问题:如果用不好，计算结果就出错了
同一把锁只能上锁一次，如果两边都在上锁，只能等一遍上完锁，在解锁，然后另一边才能继续上锁
for循环中可以上锁，非要上锁的时候，在代码越少的时候在上锁
等待解锁的方式：通知机制（不会像while True那样会占用cpu）
执行顺序：线程都是从上往下走的，只是常见出来的线程，起步的位置可能不太一样
解锁后的上锁顺序：没有固定的执行顺序，只有解锁以后，所有线程就会去抢着加锁。
'''
from threading import Thread,Lock
import time

g_num = 0

'''
这个线程和test2线程都在抢着对这个锁进行上锁，如果有一方成功上锁，那么就会导致另外一方堵塞（一直等待）到这个锁被解开为止
'''

def test1():
	global g_num

	
	for i in range(1000000):
		#上锁
		mutex.acquire()
		g_num+=1
		
		#解锁
		mutex.release()
		
	
	print("-----in test1, g_num is %d-----"%g_num)

def test2():
	global g_num

	
	for i in range(1000000):
		#上锁
		mutex.acquire()

		g_num+=1

		#解锁
		mutex.release()


	print("-----in test2, g_num is %d-----"%g_num)


#创建一把互斥锁，默认这把锁是打开的
mutex = Lock()

p1 = Thread(target=test1)
p1.start()

#time.sleep(3)

p2 = Thread(target=test2)
p2.start()

print("-----g_num = %d-----"%g_num)