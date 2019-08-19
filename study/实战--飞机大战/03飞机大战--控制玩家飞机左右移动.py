#飞机大战
#-*-coding=utf-8-*-

import pygame
import time

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
        x+=1
        y-=1

        #time.sleep(0.01)

if __name__ == "__main__":
    main()