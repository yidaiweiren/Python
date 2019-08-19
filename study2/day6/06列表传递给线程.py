'''
列表传递给线程:线程对于列表也共享
'''

from threading import Thread
import time

def work1(nums):
	nums.append(44)
	print("-----in work1-----",nums)

def work2(nums):
	#延时一会，保证t1线程执行完毕
	time.sleep(2)
	print("-----in work2-----",nums)

g_nums = [11,22,33]

t1 = Thread(target=work1,args=(g_nums,))
t1.start()

t2 = Thread(target=work2,args=(g_nums,))
t2.start()	
