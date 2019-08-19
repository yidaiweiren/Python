import os
import time
ret = os.fork()


if ret==0:
	while True:
		print("-----1-----")
		time.sleep(2)

else:
	while True:
		print("-----2-----")
		time.sleep(2)



'''
结果

-----2-----
-----1-----
-----1-----
-----2-----
-----1-----
-----2-----
-----1-----
-----2-----
-----2-----
-----1-----

'''