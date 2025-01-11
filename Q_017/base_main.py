import pygame as pg
from settings import *

from map import Map
from groups import AllSprites
from battle import BattleScreen
from game_over import GameOver

class Game:
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

        self.battle_sprites = AllSprites()

        # self.game_stage = 'main'
        self.game_stage = 'game_over'

        # バトル管理
        self.battle = None  # BattleScreenクラスのインスタンスを保持
        self.init_battle = True  # バトル画面初期化フラグ
        self.update_message_flag = False

        # バトル初期化
        self.battle = BattleScreen(self.battle_sprites)

        # 
        self.game_over_flag = False

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
                self.show_battle_screen()

            elif self.game_stage == 'game_over':
                self.show_game_over()

            pg.display.flip()

        pg.quit()

    def main_screen(self, dt):
        self.all_sprites.update(dt, self.current_map)
        self.display_surface.fill(BLUE)
        self.all_sprites.draw()

    def show_battle_screen(self):

        # バトル画面の初期化
        if self.init_battle:
            self.battle.battle_message = []
            self.init_battle = False  

            # バトル画面描画
            self.battle.draw(self.player, self.display_surface)
            self.battle_sprites.draw_battle()
        
        # 戦闘時メッセージの更新
        if self.update_message_flag:
            self.battle.update_message(self.display_surface)
            self.battle_sprites.draw_battle()
            self.update_message_flag = False

        # 戦闘コマンドの描画(マウスホーバーを検知するため、ループの外側で実装)
        if self.battle.battle_active:
            self.battle.draw_buttons()

        self.battle.status.draw_status(self.display_surface)
            

    def show_game_over(self):
        self.display_surface.fill((0, 0, 0))  # RGBで黒 (0, 0, 0)
        self.game = GameOver()
        self.game.text.draw(self.display_surface)
        self.game.text2.draw(self.display_surface)

    # メインステージ、敵の数、Playerの数上手くリセットできていない
    def reset_game_state(self):
        # 全てのスプライトを再生成
        self.all_sprites = AllSprites()
        self.battle_sprites = AllSprites()

        # プレイヤーとマップを再生成
        self.player, self.current_map = Map(self.all_sprites).create()

        # バトルの状態を完全にリセット
        self.battle = BattleScreen(self.battle_sprites)
        self.init_battle = True
        self.battle.reset()

        # ゲームステージを"main"に戻す
        self.game_stage = 'main'


    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            if event.type == pg.KEYDOWN:
                # バトル終了後、メイン画面に戻る処理
                if event.key == pg.K_SPACE and self.game_stage == 'battle':
                    if self.battle.get_battle_result() == 0:
                        self.player.game_stage = 'game_over'
                    elif self.battle.get_battle_result() == 1:
                        self.init_battle = True
                        self.battle.battle_active = True
                        self.player.game_stage = "main"  # "main"に戻す
                    
                # Game Overからメイン画面に戻る処理
                if event.key == pg.K_SPACE and self.game_stage == 'game_over':
                    self.reset_game_state()

            # BattleScreenのマウスイベントを処理
            self.update_message_flag = self.battle.handle_mouse_event(event)

if __name__ == "__main__":
    new_game = Game()
    new_game.run()
