#将字符输出到指定的文件中
#使用到open（）函数
#coding=utf8
fp=open(r'./字符输出到指定文件.txt','a+',encoding='utf8')#打开文件,并提前声明，字符编码，以防乱码
print ("要么出众，要么出局",file=fp)#将结果输出到文件中
fp.close()#关闭文件