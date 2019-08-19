

import os
import time

ret = os.fork()

if ret==0:
	print("-----子进程-----")
	time.sleep(5)
	print("-----子进程Over-----")
else:
	print("-----父进程-----")
	time.sleep(3)


print("-----over-----")	#主进程和子进程执行完都执行这句
'''
系统根据主进程执行完毕时，结束进程
主进程结束时，不会因为子进程没结束而等待，是直接结束 
'''

'''
结果
-----父进程-----
-----子进程-----
-----over-----
cuiyuanbo@cuiyuanbo-PC:~/Desktop/study2/day1$ -----子进程Over-----
-----over-----

'''