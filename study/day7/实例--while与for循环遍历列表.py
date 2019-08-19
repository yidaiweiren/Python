#while与for循环遍历列表

str=['唐僧', '悟空', '八戒', '沙僧', '如来', '观音', '哪吒', '葫芦娃', '蛇精']

i  = 0
#print (len(str))   获取列表的长度

#使用while循环遍历
while i<len(str):
    print (str[i])
    i+=1
'''
唐僧
悟空
八戒
沙僧
如来
观音
哪吒
葫芦娃
蛇精
'''

#使用for循环遍历
for i in str:
    print (i)
'''
同样正常打印结果，比while语句更简单
唐僧
悟空
八戒
沙僧
如来
观音
哪吒
葫芦娃
蛇精
'''