'''
多线程：类似于进程，也是为了实现统一功能执行多次
线程是进程中真正执行代码的东西
Thread创建 的线程：即使主线程执行完毕，子线程没有完，也会等子线程全部执行完毕在退出
'''
from threading import Thread
import time


'''
如果多个线程执行的都是同一个函数的话，各自之间不会有影响，各是各的
'''
def test():
	print("-----你好，世界-----")
	time.sleep(1)

for i in range(5):
	t = Thread(target=test)
	t.start()