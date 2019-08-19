import threading
import time

class MyThread(threading.Thread):
	def run(self):
		for i in range(5):
			time.sleep(1)
			msg = "I'am "+self.name+"@"+str(i)	#name属性中保存当前线程的名字
			print(msg)


if __name__ == "__main__":
	t = MyThread()
	t.start()