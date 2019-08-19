#异常名称统一处理

try:
    11/0    #分母为零，结果无穷大
    open("123.txt")
    print ("-----1-----")

except (FileNotFoundError,NameError):   #如果有多个可能结果，外面用括号括起来，里面用逗号隔开
    print("如果捕获到异常后做的处理，")
except Exception as ret:   #如果用了Exception，表示除了上面ecept中列出的那两个以外，其余所有的异常均按照Exception处理
    #如果想要同时看到异常名，请在Exception后加as 接受的变量。Exception as ret
    print ("-----Exception处理异常-----")
    print ("异常名为：%s"%ret)

print ("-----2-----")
'''
结果
-----Exception处理异常-----
-----2-----
'''
