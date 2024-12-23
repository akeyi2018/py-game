import pygame as pg
from settings import *
from py_sprites import Backmusic

class game:
    def __init__(self):
        pg.init()
        pg.mixer.init()  # ミキサーを初期化
        # screen
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True

    def intro_screen(self):
        self.screen.fill(BGCOLOR)
        pg.display.flip()
        self.start_music()

    def start_music(self):
        self.music = Backmusic('./music/y004.mp3')
        try:
           self.music.play()
        except Exception as e:
            print(f"音楽ファイルの読み込みに失敗しました: {e}")

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
