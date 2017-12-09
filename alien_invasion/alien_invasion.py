import sys

import pygame
from pygame.sprite import Group

from setting import Settings

from ship import Ship

import game_functions as gf

"""创建一系列整个游戏都要用到的对象"""

def run_game():
	#初始化pygame、设置并创建一个屏幕对象
	pygame.init()#初始化背景设置
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	#创建一个名为screen的显示窗口，这个游戏的所有图形元素都将在其中绘制，宽1200,高800
	pygame.display.set_caption('Alien Invasion')

	#创建一艘飞船
	ship=Ship(ai_settings,screen)

	#创建一个用于存储子弹的编组
	bullets=Group()

	#开始游戏的主循环
	while True:

		#监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		bullets.update()
		gf.update_screen(ai_settings,screen,ship,bullets)

		#每次循环时都重绘屏幕
		

run_game()
