#体重bim指数
#用到循环
#使用到运算
#使用到float（）浮点型
print("身高使用‘米’，体重使用‘KG’")
print (":::::::::::::::::::::::::::::::::::::")
name=input("请输入您的姓名：")
height=float(input("请输入您的身高："))
weight=float(input("请输入您的体重："))
bim=weight/(height*height)
print ("::::::::::::::::::::::::::::::::::::")
print (name+"，您好！")
if bim<18.5:
    print ("您的BIM指数为："+str(bim))
    print ("体重过轻 ~@_@~")
if bim>=18.5 and bim<24.9:
    print ("您的BIM指数为："+str(bim))
    print ("正常范围，注意保持 -_-")
if bim>=24.9 and bim<29.9:
    print ("您的BIM指数为："+str(bim))
    print ("体重过重 ~@<>@~")
if bim>29.9:
    print ("您的BIM指数为："+str(bim))
    print ("肥胖 ^@_@^")