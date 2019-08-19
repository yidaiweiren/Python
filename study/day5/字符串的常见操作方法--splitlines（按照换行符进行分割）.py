#字符串的常见操作方法--splitlines（按照换行符进行分割）

str="my\nname\nis\nyidaiweiren"

#输出字符出串
print (str)
'''
my
name
is
yidaiweiren
'''

#使用splitlines（）方法输出
print (str.splitlines())
'''
['my', 'name', 'is', 'yidaiweiren']     输出的值为列表
'''