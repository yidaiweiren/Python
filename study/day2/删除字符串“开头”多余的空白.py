#删除字符串“开头”的多余的空白
#使用lstrip()方法-----删除字符串开头空白
name=" hello-python"
print (name.lstrip())   #已经删除的效果，但不是永久生效
print (name)    #未删除的效果

#永久删除的效果，请看下面
name_1=" hello-python"
name_1=name_1.lstrip()
print (name_1)  #永久删除的效果