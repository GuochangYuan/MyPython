import sys

import pygame

"""包含一系列函数，游戏的大部分工作由该模块完成"""

def check_events(ship):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN:#键被按下
			if event.key==pygame.K_RIGHT:
				#向右移动飞船
				ship.moving_right=True
			elif event.key==pygame.K_LEFT:
				#向左移动飞船
				ship.moving_left=True
		elif event.type==pygame.KEYUP:#键被释放
			if event.key==pygame.K_RIGHT:
				ship.moving_right=False
			elif event.key==pygame.K_LEFT:
				ship.moving_left=False
			

def update_screen(ai_settings,screen,ship):
	"""更新屏幕上的图像，并切换到新屏幕"""
	#每次循环时都重绘屏幕
	screen.fill(ai_settings.bg_color)
	ship.blitme()

	#让最近绘制的屏幕可见
	pygame.display.flip()
