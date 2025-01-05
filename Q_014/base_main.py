import pygame as pg
from settings import *

from map import Map
from groups import AllSprites
from battle import Battle

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

        self.game_stage = 'main'

        # バトル管理
        self.battle = None  # Battleクラスのインスタンスを保持
        self.fade_in_done = False  # フェードイン制御フラグ
        self.update_message_flag = False

        # バトル初期化
        self.battle = Battle()

        # Map
        self.player, self.current_map = Map(self.all_sprites).create()


        
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
            pg.display.flip()

        pg.quit()

    def main_screen(self, dt):
        # pg.display.set_mode((WIDTH, HEIGHT))
        self.all_sprites.update(dt, self.current_map)
        self.display_surface.fill(BLUE)
        self.all_sprites.draw()

    def battle_screen(self):

        # フェードインがまだ完了していなければ実行
        if not self.fade_in_done:
            self.battle.battle_message = []
            self.battle.fade_in()
            self.fade_in_done = True  # フェードイン完了を記録



            # バトル画面描画
            self.battle.draw(self.player)

    def events(self):
        # イベント処理
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    self.fade_in_done = False
                    self.player.game_stage = "main"  # 状態を"main"に戻す

            # Battleクラスのマウスイベントを処理
            self.battle.handle_mouse_event(event)


if __name__ == "__main__":
    new_game = game()
    new_game.run()
