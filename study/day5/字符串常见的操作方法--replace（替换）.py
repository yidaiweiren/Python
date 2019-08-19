#字符串的常见操作方法--replace（替换）

str="my is name is yidaiweiren"

#使用replace方法修改is伟大写
#replace ("原始值"，"替换值")
print (str.replace("is","IS"))
print ("原字符串："+str)
'''
my IS name IS yidaiweiren   结果发现将所有的is全部替换为大写
字符串：my is name is yidaiweiren   但是原字符串没有被改变，也不会被改变，相当于他只执行一次打印改变值，后期可将值赋给变量
'''

#想将is替换为xx
print (str.replace("is","xx"))
print ("原字符串："+str)
'''
my xx name xx yidaiweiren   法相将所有is都替换掉了，现在只想替换第一个
原字符串：my is name is yidaiweiren
'''

#只将第一个is替换为XX
#replace ("原始值","替换值","替换几次")
print (str.replace("is","XX",1))
print ("原字符串："+str)
'''
my xx name xx yidaiweiren      实现预期效果
原字符串：my is name is yidaiweiren
'''