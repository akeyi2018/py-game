from settings import * 
import pygame as pg

class AllSprites(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.offset = pg.Vector2()

    def draw(self, target_pos):
        self.offset.x = WIDTH / 2 - target_pos[0]
        self.offset.y = HEIGHT / 2 - target_pos[1]
        # self.offset
        for sprite in self:
            self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)
        