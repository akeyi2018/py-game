from settings import * 
import pygame as pg
from utils import Button, TextAnimation, Sound, TextSprite

class Communication:
    def __init__(self, parent):
        self.parent = parent
        self.font = pg.font.Font(FONT, MESSAGE_FONT_SIZE)
        self.speed = 200
        self.display_surface = pg.display.get_surface()
        self.text = TextAnimation(
            self.font, 
            (255,255,255),
            (0,0,255), 
            self.parent.player.rect.centerx -90, 
            self.parent.player.rect.centery + 50, 
            self.speed, 
            self.display_surface)
        
        self.description = 'ここは通れません。'
        self.counter = 0
        self.draw_flag = False

    def draw(self):
        self.parent.player.rect.centerx
        pg.draw.rect(self.display_surface, '#8E7698', [self.parent.player.rect.centerx - 100, 
                                                       self.parent.player.rect.centery - 10 + 50, 200-2, 50])
        pg.draw.rect(self.display_surface,'#D3DED0', [self.parent.player.rect.centerx -100, 
                                                      self.parent.player.rect.centery -10 + 50, 200, 50],5,border_radius=5)

        flag, self.counter = self.text.draw_anime(self.description, self.counter)

        if flag and self.counter <= len(self.description) :
            self.counter += 1

        if self.counter > len(self.description): 
            self.draw_flag = True