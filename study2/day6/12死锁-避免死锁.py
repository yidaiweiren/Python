'''
两个线程都等待对方先解锁
避免死锁：
	1.添加超时时间
	2.避免使用银行家算法（后期自行了解）
'''
import threading
import time

class MyThread1(threading.Thread):
	def run(self):
		if mutexA.acquire():
			print(self.name+"-----do1--up-----")
			time.sleep(1)

			if mutexB.acquire(timeout=2):
				print(self.name+"-----do1--down-----")
				mutexB.release()

			mutexA.release()


class MyThread2(threading.Thread):
	def run(self):
		if mutexB.acquire():
			print(self.name+"-----do2--up-----")
			time.sleep(1)

			if mutexA.acquire(timeout=2):
				print(self.name+"-----do2--down-----")
				mutexA.release()

			mutexB.release()




mutexA = threading.Lock()
mutexB = threading.Lock()

if __name__ == "__main__":
	t1 = MyThread1()
	t2 = MyThread2()
	t1.start()
	t2.start()