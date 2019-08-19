#字符串的常见操作方法--rpartition（'从右'开始将字符串分为三段）
#定位中间的界点，其余往两边散
#类似于体育课做操

str="my name is yidaiweiren"

#使用rpartition（'界点字符'）方法输出
print (str.rpartition('yi'))
'''
('my name is ', 'yi', 'daiweiren')  将字符分隔为3段
'''