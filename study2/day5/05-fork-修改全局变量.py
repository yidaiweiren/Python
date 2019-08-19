'''
进程之间不共享全局变量，也就是说，子进程修改了全局变量，对父进程不生效
进程中，每个进程所有的东西，变量什么的都是私有的
为了保证子进程一定先执行，可以给父进程添加一个延时

'''

import os
import time

ret = os.fork()

g_num = 100

if ret==0:
	print("-----子进程-----")
	g_num+=1
	print(g_num)
else:
	time.sleep(3)
	print("-----父进程-----")
	print(g_num)


'''
结果
----子进程-----
101
-----父进程-----
100
'''