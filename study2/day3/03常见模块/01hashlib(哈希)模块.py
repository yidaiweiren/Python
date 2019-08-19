

import hashlib
m = hashlib.md5()
print(m)
m.update(b'yidaiweiren')    #更新要加密的字串，b表示unicode编码转换
print(m.hexdigest())    #返回16进制数字字符串