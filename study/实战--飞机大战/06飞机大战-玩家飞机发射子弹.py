#飞机大战
#-*-coding=utf-8-*-

import pygame
import time
from pygame.locals import *

class HeroPlane(object):
    '''创建一个飞机对象'''
    def __init__(self,screen_temp):
        self.x = 200
        self.y = 700
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/hero1.png")
        self.bullet_list = []   #存储发射出去的子弹对象


    def display(self):
        '''封装显示飞机的功能'''
        self.screen.blit(self.image,(self.x,self.y))  #hero此处就相当于属性中的self.image

        #调用飞机的同时显示发射出去的子弹
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def move_left(self):
        '''控制飞机向左移动'''
        self.x -= 15

    def move_right(self):
        '''控制飞机向右移动'''
        self.x += 15

    def move_up(self):
        '''控制飞机向上移动'''
        self.y -= 15

    def move_down(self):
        '''控制飞机向下移动'''
        self.y += 15

    def fire(self):
        '''开火'''
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))
        print (self.bullet_list)

class Bullet(object):   #bullet：释义为“子弹”
    '''创建子弹类'''
    def __init__(self,screen_temp,x,y):
        '''定义子弹的初始属性'''
        self.x = x+40
        self.y = y-18
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/bullet.png")

    def display(self):
        '''封装显示子弹的功能'''
        self.screen.blit(self.image,(self.x,self.y))    #窗口指向谁，就把这个对象显示到谁上

    def move(self):
        '''子弹发射出去'''
        self.y -= 10

def key_control(hero_temp):     #因为函数中不能直接掉用hero，所以这里放一个hero_temp形参来接受传进来的hero
    '''键盘的操作'''
    # 获取事件，比如按键等
    for event in pygame.event.get():

        # 判断是否点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()

        # 判断用户是否按下了按键
        if event.type == KEYDOWN:
            # 检测按键是否a或者left
            if event.key == K_a or event.key == K_LEFT:
                print("left")
                hero_temp.move_left()

            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print("right")
                hero_temp.move_right()

            # 检测按键是否是w或者up
            elif event.key == K_w or event.key == K_UP:
                print("up")
                hero_temp.move_up()

            # 检测按键是否是s或者down
            elif event.key == K_s or event.key == K_DOWN:
                print("down")
                hero_temp.move_down()

            # 检测用户是否按空格键space
            elif event.key == K_SPACE:
                print("space")
                hero_temp.fire()

def main():
    #创建窗口
    screen = pygame.display.set_mode((480,852),0,32)

    #创建一个和窗口一样大的背景图片
    background = pygame.image.load("./feiji/background.png")

    #创建一个飞机对象
    hero = HeroPlane(screen)



    #把背景图片放到窗口中显示
    while True:

        #设定需要显示的背景图
        screen.blit(background,(0,0))   #blit:释义为“填充”

        #显示飞机对象
        hero.display()

        #更新需要显示的内容
        pygame.display.update()

        #键盘操作
        key_control(hero)


        #程序休眠时间（内存小的机器比较好用）
        #time.sleep(0.01)

if __name__ == "__main__":
    main()