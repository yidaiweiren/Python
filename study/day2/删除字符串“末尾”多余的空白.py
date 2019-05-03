#删除字符串"末尾"多余的空白
#使用rstrip()方法------删除多于空白
name="hello-python "
print (name.rstrip())   #这个已经去除末尾空白字符串
print (name)    #原始没有去除

#入过想要永久去除，请看下面方法
name_1="hello-python "
name_1=name_1.rstrip()
print (name_1)