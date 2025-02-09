import pygame as pg
from sub.settings import *

class BattleLayout:
    def __init__(self):
        self.display_surface = pg.display.get_surface()
        self.back_ground_img = pg.image.load('../battle/bg.png')
        self.back_ground_img = pg.transform.scale(self.back_ground_img, (819, HEIGHT))

        self.bg_size = self.back_ground_img.get_size()
        self.rect = self.back_ground_img.get_rect()
        self.off_set = pg.Vector2()
        self.off_set.x = -int((self.rect.centerx - WIDTH /2))
        self.off_set.y = -int((self.rect.centery - HEIGHT /2))
    
    def draw_background(self, screen):
        self.screen = screen
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.back_ground_img, self.rect.topleft + self.off_set)

    def draw_menu_background(self):
        pg.draw.rect(self.display_surface, '#8E7698', [2, 2, self.off_set.x -2, HEIGHT-2])
        pg.draw.rect(self.display_surface,'#D3DED0', [0, 0, self.off_set.x, HEIGHT],5,border_radius=5)

    # def draw_menu_backgroud(self):
    #     # 半透明の背景
    #     semi_transparent = pg.Surface((self.off_set.x - 2, HEIGHT - 2), pg.SRCALPHA)
    #     semi_transparent.fill((142, 118, 152, 200))  # RGBA: 最後の値が透明度
    #     self.display_surface.blit(semi_transparent, (2, 2))

        # 枠線
        pg.draw.rect(self.display_surface, '#D3DED0', 
                    [0, 0, self.off_set.x, HEIGHT], 5, border_radius=5)

    def draw_background_text_area(self, screen):
        """必要最小限の透明マスクを新規作成し、配置する"""
        self.text_area_rect = pg.Rect(250, 430, self.bg_size[0] * 0.95, self.bg_size[1] * 0.3)

        # screen.fill((0,0,0), self.text_area_rect)

        # # 半透明の背景色を設定
        # semi_transparent_surface = pg.Surface(self.text_area_rect.size, pg.SRCALPHA)
        # semi_transparent_surface.fill((10, 15, 5, 190))  # 半透明の青色
        
        # # 角の描画ですこし小さくする
        # self.display_surface.blit(semi_transparent_surface, 
        #                           [self.text_area_rect.x + 2,
        #                            self.text_area_rect.y + 2,
        #                            self.text_area_rect.width -2,
        #                            self.text_area_rect.height -2])


        # 枠線を再描画
        pg.draw.rect(self.display_surface, (255, 255, 255), self.text_area_rect, 3, border_radius=5)