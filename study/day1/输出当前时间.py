#输出当前时间
#主要学会使用datetime模块
#学会引入模块
#拓展：使用上节所学的open（）函数，将时间写入文件
import datetime     #调用datetime这个时间模块
fp=open(r'./当前时间.txt','+a',encoding='utf8')
print ("当前年份是："+str(datetime.datetime.now().year),file=fp)  #输出当前年份
print ("当前时间是："+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),file=fp)#输出当前时间