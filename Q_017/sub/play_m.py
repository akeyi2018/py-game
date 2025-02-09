import pygame as pg
import os

class Game:
    def __init__(self):
        pg.mixer.init()  # 先にオーディオを初期化
        pg.init()

        # screen
        self.display_surface = pg.display.set_mode((800, 600))  # WIDTH, HEIGHT を仮に 800x600 に
        pg.display.set_caption("My Game")  # TITLE を仮のものに

        # clock
        self.clock = pg.time.Clock()
        self.running = True

        self.game_stage = 'start_menu'

        self.bgm_dict = {
            "main": "music/town/Forgotten-Place.mp3",
            "battle": "music/battle/Battle-Rosemoon.mp3",
            "game_over": "music/game_over.mp3",
            "start_menu": "../music/town/Forgotten-Place.mp3"
        }

        self.play_background_music(self.game_stage)  # 最初の音楽を再生

    def play_background_music(self, stage):
        """ 音楽を再生する """
        bgm_path = self.bgm_dict.get(stage)

        if bgm_path and os.path.exists(bgm_path):  # ファイルの存在チェック
            pg.mixer.music.stop()  # 現在の音楽を停止
            pg.mixer.music.load(bgm_path)
            pg.mixer.music.set_volume(1.0)  # 音量を最大に設定
            pg.mixer.music.play(-1)  # ループ再生
        else:
            print(f"音楽ファイルが見つかりません: {bgm_path}")

    def run(self):

        dt = self.clock.tick(60) / 1000# FPS を 60 に
        
        """ゲームループ"""
        while self.running:
            # pg.event.pump()  # Pygame の内部イベント処理を呼び出す

            # 音楽が停止していたら再生し直す
            if not pg.mixer.music.get_busy():
                self.play_background_music(self.game_stage)

            self.events()
            self.display_surface.fill((0, 0, 255))  # BLUE の代わりに RGB (0, 0, 255) を使用
            pg.display.flip()
            

        pg.quit()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

if __name__ == "__main__":
    new_game = Game()
    new_game.run()
