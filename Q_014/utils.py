import pygame as pg 
from settings import * 

class Util:
    pass

class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.color = (0, 0, 255)  # ボタンの色
        # フォント設定
        self.font = pg.font.Font("../battle/Meiryo.ttf", 24)
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))

    def draw(self, surface):
        pg.draw.rect(surface, self.color, self.rect)
        surface.blit(self.text_surface, (self.rect.x + (self.rect.width - self.text_surface.get_width()) // 2,
                                        self.rect.y + (self.rect.height - self.text_surface.get_height()) // 2))

    def check_click(self, pos):
        # マウスクリック時にボタンが押されたかを判定
        return self.rect.collidepoint(pos)
    
