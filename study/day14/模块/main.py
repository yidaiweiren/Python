#调用sendmsg模块
#推荐使用方法一，其他作为了解
#调用一个模块，相当于先执行了一遍这个模块
#方式一
import sendmsg  #只写名称，不写后缀
import recvmsg
sendmsg.test1()
sendmsg.test2()
recvmsg.test1()
'''
sendmsg
-----test1-----
-----test2-----
-----test1-----
-----test2-----
-----recvmsg-test1-----


修改sendmsg中的代码后的结果
sendmsg
-----test1-----
-----test2-----
-----recvmsg-test1-----
'''


'''
方式二
from sendmsg import test1,test2
#from sendmsg import test2
test1()
test2()
'''


'''
方式三
from sendmsg import *
from recvmsg import *
test1()
test2()
'''
'''
结果有问题，没有打出来sendmsg中的test1
如果函数名相同，后面的会顶替掉前面的
-----recvmsg-test1-----
-----test2-----
'''
#############################################################################################################
#模块的别名

import time as tt   #引入time模块，并使用as为其取一个别名为tt

tt.sleep(3)
print ("@@@")