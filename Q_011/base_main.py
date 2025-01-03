import pygame as pg
from settings import *

from player import Player
from map import Map

class game:
    def __init__(self):
        pg.init()

        # screen
        self.display_surface = pg.display.set_mode((WIDTH, HEIGHT))
        # title
        pg.display.set_caption(TITLE)
        # clock
        self.clock = pg.time.Clock()
        self.running = True

        # 通過不可Sprite
        self.collision_sprites = pg.sprite.Group()
        # Enemy Sprite
        self.enemy_sprites = pg.sprite.Group()

        self.game_stage = 'main'

        # Map
        self.player, self.map_list, self.enemy_list, self.mob_pos_info, self.current_map = Map(
            self.collision_sprites,self.enemy_sprites).create()
        
    def events(self):
        # イベント処理
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    self.player.game_stage = "main"  # 状態を"main"に戻す
                    # print(f'player pos: x:{int(self.map.player.rect.centerx/TILE_SIZE)}, y:{int(self.map.player.rect.centery/TILE_SIZE)}')

    def main_screen(self, dt):
        # draw
        self.display_surface.fill(BLUE)

        # 衝突用ブロック
        for map in self.map_list:
            self.display_surface.blit(map.surface, map.rect)

        # Enemyの表示
        for enemy in self.enemy_list:
            self.display_surface.blit(enemy.surface, enemy.rect)

        # playerの表示    
        self.display_surface.blit(self.player.surface,self.player.rect)

        # player Update
        self.player.update(dt, self.enemy_list, self.mob_pos_info, self.current_map)

    def battle_screen(self):
        pg.display.set_caption('Battle')
        self.display_surface.fill((125, 125, 0))  # 背景を赤に
        font = pg.font.SysFont("yumincho", 74)
        text = font.render(f"{self.player.enemy_name}に遭遇!", True, (255, 255, 255))
        self.display_surface.blit(text, (250, 250))

    def run(self):
        """ゲームループ"""
        dt = self.clock.tick(FPS) / 1000

        while self.running:
            # events
            self.events()
            self.game_stage = self.player.game_stage
            if self.game_stage == 'main':
                self.main_screen(dt)

            elif self.game_stage == 'battle':
                # 敵と衝突した後の画面
                self.battle_screen()
            pg.display.update()

        pg.quit()

if __name__ == "__main__":
    new_game = game()
    new_game.run()
