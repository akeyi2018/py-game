from settings import * 
import pygame as pg


class AllSprites(pg.sprite.Group):
    def __init__(self, *sprites):
        super().__init__(*sprites)
        
        # display
        self.display_surface = pg.display.get_surface()

        self.offset =pg.Vector2()

    def draw(self):
        pg.display.set_caption('FIELD')
        for sprite in self:
            self.display_surface.blit(sprite.surface, sprite.rect.topleft)

    def draw_battle(self):
        pg.display.set_caption('BATTLE')
        for sprite in self:
            self.display_surface.blit(sprite.image, sprite.rect.topleft)
