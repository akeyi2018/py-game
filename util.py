import pygame as pg
from config import *

class Utils:
    def __init__(self):
        self.clock = pg.time.Clock()

    def draw_text(self, text, size, color, x, y, screen):
        self.screen = screen
        self.font = pg.font.SysFont("yumincho", size)
        self.color = color
        self.text = text
        self.x = x
        self.y = y
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (self.x, self.y)
        self.screen.blit(text_surface, text_rect)

    def wait_event(self):
        self.waiting = True
        while self.waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.waiting = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.waiting = False   
