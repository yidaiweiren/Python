#猜拳游戏
#提示用户并获取用户输入
#熟悉了解random工具模块 随机模块
#randint() 方法，随机生成数字   （1.3）随机生成1.2.3其中一个数字
import random

plear=int(input("请输入 0剪刀  1石头  2布："))

#让电脑出一个数
computer = random.randint(0,2)   #默认电脑出一作为测试，但这样显然不符合游戏设定

#判断用户输入的结果

#if 玩家获胜的条件
if (plear==0 and computer==2) or (plear==1 and computer==0) or (plear==2 and computer==1):#and个or不能同时出现，否则会判断异常
    print ("赢了^@<>@^")
    print (computer)
#elif 平局的条件
elif plear==computer:
    print ("平局，洗洗手再来！！！")
    print (computer)
else:
    print ("输了，回家拿点钱，再来···")
    print (computer)