#对比append方法和extend方法的区别

str=['唐僧','悟空','八戒','沙僧','如来','观音']
str1=['观音','黑熊精']

#使用extend方法合并
#str.extend(str1)
#print (str)
'''
['唐僧', '悟空', '八戒', '沙僧', '如来', '观音', '观音', '黑熊精']   逐个从str1中取出，在添加到str后面
'''

#使用append方法合并
str.append(str1)
print (str)
'''
['唐僧', '悟空', '八戒', '沙僧', '如来', '观音', ['观音', '黑熊精']]     直接将str1这个列表加入到str中
'''