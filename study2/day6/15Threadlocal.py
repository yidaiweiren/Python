import threading

#创建全局Thread.local对象
#threadlocal()创建的对象，是全局的，可以支持多个线程同时给里面传值，各线程添加的值只对这个线程有效，不会影响其他线程

local_school = threading.local()


def process_student():
	#获取当前线程关联的student
	std = local_school.student
	print("hello ,%s (in %s)"%(std,threading.current_thread().name))


def process_thread(name):
	#绑定threadlocal的student
	local_school.student = name
	process_student()



t1 = threading.Thread(target=process_thread,args=('yidaiweiren',),name='Thread-A')
t2 = threading.Thread(target=process_thread,args=('崔渊博',),name='Thread-B')

t1.start()
t2.start()

t1.join()
t2.join()