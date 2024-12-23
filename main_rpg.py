import pygame as pg
from settings import *

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
        # ゲーム本体画面 (ここでは単に背景色を変更)
        self.screen.fill((0, 0, 0))
        font = pg.font.Font(None, 36)
        text = font.render("This is the game screen. \nPress ESC to quit.", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pg.display.flip()

    def run(self):
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
            
            # 画面更新
            if self.current_screen == "intro":
                self.intro_screen()
            elif self.current_screen == "game":
                # self.util.stop_background_music_main_scene()
                # ここで別の音楽を鳴らしたい
                self.main_game_screen()

            self.clock.tick(60)

        pg.quit()


if __name__ == "__main__":
    new_game = game()
    new_game.run()
