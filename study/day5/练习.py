'''
要求：
    1.给定一个字符串，包含换行，空格
    2.对字符串进行分隔清洗
    3.重新拼接一个新的纯净的字串
'''

str="my  \n name \t is yidaiweiren"

#先使用split（）方法清洗字串
result=str.split()
print (result)
'''
['my', 'name', 'is', 'yidaiweiren']     清洗完成，结果为列表
'''

#使用join（）方法对列表进行重组
new_result="".join(result)
print(new_result)
'''
mynameisyidaiweiren     得到最终结果
'''