#飞机大战
#-*-coding=utf-8-*-

import pygame
import time
from pygame.locals import *

def main():
    #创建窗口
    screen = pygame.display.set_mode((480,852),0,32)

    #创建一个和窗口一样大的背景图片
    background = pygame.image.load("./feiji/background.png")

    #创建一个飞机
    hero = pygame.image.load("./feiji/hero1.png")

    #玩家飞机出事位置
    x = 200
    y = 650

    #把背景图片放到窗口中显示
    while True:

        #设定需要显示的背景图
        screen.blit(background,(0,0))   #blit:释义为“填充”
        screen.blit(hero,(x,y))

        #更新需要显示的内容
        pygame.display.update()

        #获取事件，比如按键等
        for event in pygame.event.get():

            #判断是否点击了退出按钮
            if event.type == QUIT:
                print ("exit")
                exit()

            #判断用户是否按下了按键
            if event.type == KEYDOWN:
                #检测按键是否a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print ("left")
                    x-=5

                #检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    print ("right")
                    x+=5

                #检测用户是否按空格键space
                elif event.key == K_SPACE:
                    print ("space")


        #程序休眠时间（内存小的机器比较好用）
        #time.sleep(0.01)

if __name__ == "__main__":
    main()