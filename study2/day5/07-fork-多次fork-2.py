import os
import time
ret = os.fork()


if ret==0:
	print("-----1-----")

else:
	print("-----2-----")


	ret = os.fork()

	if ret==0:
		print("-----11-----")
	else:
		print("-----22-----")



'''
				程序执行（创建进程）

		子进程						父进程

								子进程	父进程	

'''

'''
结果
-----2-----
-----1-----
-----22-----
-----11-----
'''