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

    def intro_screen(self):
        self.screen.fill(BGCOLOR)
        self.util.play_background_music_main_scene()
        self.util.draw_text("Start new Game", 28, 
                             MOJICOLOR, WIDTH / 2, HEIGHT * 3 / 4, self.screen)
        pg.display.flip()
        self.util.wait_event()
        

    def run(self):
        # 描画更新
        self.intro_screen()
        while self.running:
            # イベント処理
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

           
            self.clock.tick(60)

        pg.quit()


if __name__ == "__main__":
    new_game = game()
    new_game.run()
