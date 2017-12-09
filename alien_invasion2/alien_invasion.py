import sys #sys模块提供了一系列有关Python运行环境的变量和函数
import pygame

from setting import Settings#引入自定义setting模块中的Settings类
from ship import Ship#引入自定义ship模块中的Ship类
import game_function as gf#引入自定义game_function模块，响应按键和鼠标事件
from pygame.sprite import Group#导入pygame.sprite中的Group类

def run_game():
    ai_settings=Settings()#实例化一个Settings类
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    screen=pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    #设置背景色,创建一种背景色，并存储在bg_color中
    #bg_color=(230,230,230)

    #创建一艘飞船
    ship=Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets=Group()


    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type==pygame.QUIT:
        #         sys.exit()
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()#移动飞船
        # bullets.update()
        # #删除已消失的子弹
        # for bullet in bullets.copy():
        #     if bullet.rect.bottom<=0:
        #         bullets.remove(bullet)
        # #print(len(bullets))
        gf.update_bullets(bullets)

        gf.update_screen(ai_settings,screen,ship,bullets)

        # #每次循环时，用背景色填充屏幕
        # screen.fill(ai_settings.bg_color)

        # #填充背景色后，绘制一艘飞船，以保证它出现在背景前面
        # ship.blitme()
        # #让最近绘制的屏幕可见
        # pygame.display.flip()
        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()