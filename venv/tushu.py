print('----------豆瓣音乐TOP250----------\n')
file123=open('123.txt','r',encoding='UTF-8')
#python读取文件时提示"UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 205: illegal multibyte sequence"
#解决方法：
#file123=open('123.txt')改为
#file123=open('123.txt','r',encoding='UTF-8')
print(file123.read())
#读取文件所有内容
#file123.read()
#print(file123.readline())
#结果是什么都没有
#print(file123.tell())
#统计文件一共有多少个字符
#file123.seek(0.0)
#将文件指针移到文件开头
#print(file123.tell())
#统计字符
#print(file123.readline())