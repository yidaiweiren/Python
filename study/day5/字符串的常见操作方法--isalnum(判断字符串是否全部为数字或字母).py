#字符串的常见的操作方法--isalnum（判断字符串是否全部位数字或字母）

str="12334"
str1="zxcvbb"
str2="zz123"
str3="zz22@#$"
#使用isalnum（）方法输出

print (str.isalnum())
print (str1.isalnum())
print (str2.isalnum())
print (str3.isalnum())
'''
True
True
True
False   存在特殊符号，所以返回为False
'''