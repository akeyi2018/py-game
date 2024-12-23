import pygame as pg
from settings import *
# from py_sprites import Spritesheet
from spritesheet import Spritesheet

from util import Utils

class game:
    def __init__(self):
        pg.init()
        pg.mixer.init()  # ミキサーを初期化
        # screen
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True
        self.util = Utils()
        self.current_screen = "intro"  # 現在の画面状態を管理
        # self.character_spritesheet = Spritesheet('./img/F1.png')

        self.my_spritesheet = Spritesheet('trainer_sheet.png')
        self.trainer = [self.my_spritesheet.parse_sprite('trainer1.png'), 
                        self.my_spritesheet.parse_sprite('trainer2.png'),
                        self.my_spritesheet.parse_sprite('trainer3.png'),
                        self.my_spritesheet.parse_sprite('trainer4.png'),
                        self.my_spritesheet.parse_sprite('trainer5.png')]

    def intro_screen(self):
        self.screen.fill(BGCOLOR)
        
        # self.util.draw_text("Start new Game", 28, 
        #                      MOJICOLOR, WIDTH / 2, HEIGHT * 3 / 4, self.screen)

        font = pg.font.Font(None, 36)
        text = font.render("Start new Game", True, MOJICOLOR)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pg.display.flip()
        # self.util.wait_event()
        # self.util.stop_background_music_main_scene()

    def main_game_screen(self):
        """ゲーム画面の描画とアニメーション処理"""
        # スプライト描画用変数を初期化
        if not hasattr(self, 'index'):
            self.index = 0
            self.frame_counter = 0
            self.update_frames = 0

        # 背景のクリア
        self.screen.fill((255, 255, 255))

        # アニメーション処理
        if self.update_frames > 0:
            self.frame_counter += 1
            if self.frame_counter >= 5:  # アニメーション速度を調整
                self.index = (self.index + 1) % len(self.trainer)
                self.frame_counter = 0
                self.update_frames -= 1

        # スプライトの描画
        self.screen.blit(self.trainer[self.index], (0, 270 - 128))

        # 画面の更新
        pg.display.flip()

    def run(self):
        """ゲームループ"""
        # 描画更新
        self.intro_screen()
        if self.current_screen == "intro":
            self.util.play_background_music_main_scene()  # 音楽再生を一度だけ呼び出し

        while self.running:
            # イベント処理
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                elif event.type == pg.MOUSEBUTTONDOWN and self.current_screen == 'intro':
                    self.current_screen = "game"
                    self.util.stop_background_music_main_scene()
                    self.util.play_sort_sound()
                elif event.type == pg.KEYDOWN and self.current_screen == "game":
                    if event.key == pg.K_ESCAPE:
                        self.running = False
                    elif event.key == pg.K_SPACE:
                        self.update_frames = 5  # スペースキーでアニメーション開始

            # 画面更新
            if self.current_screen == "intro":
                self.intro_screen()
            elif self.current_screen == "game":
                self.main_game_screen()

            self.clock.tick(60)
        pg.quit()


if __name__ == "__main__":
    new_game = game()
    new_game.run()
