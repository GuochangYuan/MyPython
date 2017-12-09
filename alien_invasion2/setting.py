class Settings():

    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width=1200
        self.screen_height=700
        self.bg_color=(230,230,230)#此为一个元组
        #设置飞船的速度
        self.ship_speed_factor=1.5#1.5表示像素，但rect的centerx等属性只能存储整数值，因此需要对Ship类做些调整
        #设置子弹
        self.bullet_speed_factor=1
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=60,60,60
        self.bullets_allowed=3#设置子弹数量