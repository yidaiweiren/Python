'''
线程的执行顺序：无序的，先创建的不一定先执行
原因：操作系统调度问题
'''

import threading
import time

class MyThread(threading.Thread):
	def run(self):
		for i in range(5):
			time.sleep(1)
			msg = "I'am "+self.name+"@"+str(i)	#name属性中保存当前线程的名字
			print(msg)

def test():
	for i in range(5):
		t = MyThread()
		t.start()

if __name__ == "__main__":
	test()

'''
结果
I'am Thread-2@0
I'am Thread-1@0
I'am Thread-4@0
I'am Thread-3@0
I'am Thread-5@0
I'am Thread-2@1
I'am Thread-3@1
I'am Thread-4@1
I'am Thread-1@1
I'am Thread-5@1
I'am Thread-2@2
I'am Thread-4@2
I'am Thread-3@2
I'am Thread-1@2
I'am Thread-5@2
I'am Thread-3@3
I'am Thread-2@3
I'am Thread-4@3
I'am Thread-1@3
I'am Thread-5@3
I'am Thread-3@4
I'am Thread-4@4
I'am Thread-1@4
I'am Thread-2@4
I'am Thread-5@4

'''