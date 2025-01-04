import pygame as pg
from settings import *


class Battle:
    def __init__(self):

        self.display_surface = pg.display.get_surface()
        self.back_ground_img = pg.image.load('../battle/bg.png').convert()
        self.bg_size = self.back_ground_img.get_size()

        self.rect = self.back_ground_img.get_rect()
        self.off_set = pg.Vector2()
        self.off_set.x = -int((self.rect.centerx - WIDTH /2))
        self.off_set.y = -int((self.rect.centery - HEIGHT /2))

        self.font = pg.font.Font("../battle/Meiryo.ttf", 24)

    def draw(self, player):

        enemy = player.collided_enemy
        mob_pos =  ((WIDTH - 128) /2,HEIGHT /8)
        self.display_surface.blit(enemy.battle_surface, mob_pos)

        # self.display_surface.fill(BLUE)
        pg.display.set_caption('Battle')
        # pg.draw.rect(self.display_surface, WHITE, pg.Rect(20, 320, 600, 140), 3)
        
        # メッセージ
        text_surface = self.font.render(f"  {enemy.name}が現れました!  ", True, (255, 255, 255))
        # 背景用の透明なSurfaceを作成
        bg_surface = pg.Surface((self.bg_size[0]*0.95, self.bg_size[1] * 0.3), pg.SRCALPHA)
        bg_surface.fill((0, 0, 200, 128))  # (R, G, B, Alpha)で透明度を指定（128は50%透明）
        # bg_surface.set_alpha(1)
        message_rect = bg_surface.get_rect()
        # self.display_surface.blit(message_rect,3)
        pg.draw.rect(bg_surface, WHITE, message_rect, 3, border_radius=5)

        self.display_surface.blit(bg_surface, (250, 430))
        self.display_surface.blit(text_surface, (250, 430))
        

        
        # self.display_surface.blit(self.back_ground_img, self.rect.topleft + self.off_set)
        

    def fade_in(self):
        for alpha in range(0, 125, 5):
            # self.display_surface.fill((0, 0, 0))
            temp_surface = self.back_ground_img.copy()
            temp_surface.set_alpha(alpha)
            self.display_surface.blit(temp_surface, self.rect.topleft + self.off_set)
            pg.display.flip()
            pg.time.delay(30)
