import os

os.fork()
os.fork()
os.fork()

print("-----1-----")

'''
结果
---1-----
-----1-----
-----1-----
-----1-----
-----1-----
-----1-----
-----1-----
-----1-----
'''


'''
fork炸弹:直接会干死系统的代码

import os
os.fork()
os.fork()
while True()
	os.fork()
print("-----1-----")
'''