import pygame as pg
from settings import *

from map import Map
from groups import AllSprites

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

        # all sprite
        self.all_sprites = AllSprites()
 
        # # Enemy Sprite
        # self.enemy_sprites = pg.sprite.Group()

        self.game_stage = 'main'

        # Map
        self.player, self.current_map = Map(self.all_sprites).create()
        
    def events(self):
        # イベント処理
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    self.player.game_stage = "main"  # 状態を"main"に戻す

    def main_screen(self, dt):
        # draw
        
        self.all_sprites.update(dt, self.current_map)
        self.display_surface.fill(BLUE)
        self.all_sprites.draw()
        # self.display_surface.blit(self.player.surface, self.player.rect.topleft)

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
