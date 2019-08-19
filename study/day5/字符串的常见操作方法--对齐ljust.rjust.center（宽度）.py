#字符串的常见操作方法--对齐ljust/rjust/center（宽度）

str="my name is yidaiweiren"

#使用ljust（width）方法输出
print (str.ljust(60))
'''
my name is yidaiweiren  宽度为60，居左显示
'''
#使用rjust（width）方法输出
print (str.rjust(60))
'''
                                      my name is yidaiweiren    宽度为60，居右显示
'''
#使用center（width）方法输出
print (str.center(60))
'''
                   my name is yidaiweiren                       宽度为60，居中显示
'''