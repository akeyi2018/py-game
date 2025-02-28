import pygame as pg
from sub.settings import *

from sub.map import Map
from sub.groups import AllSprites
from battle import BattleScreen
from sub.game_over import GameOver
from sub.game_start import StartMenu
from utils import Backmusic
from save_load import GameData
import os
from communication import Communication

class Game:
    def __init__(self):
        pg.mixer.init()
        pg.init()

        # screen
        self.display_surface = pg.display.set_mode((WIDTH, HEIGHT))
        # title
        pg.display.set_caption(TITLE)

        # clock
        self.clock = pg.time.Clock()
        self.running = True

        # 全てのスプライトを再生成
        self.all_sprites = AllSprites()

        self.battle_sprites = AllSprites()

        self.enemy_sprites = AllSprites()

        self.game_stage = STAGE
        self.current_stage = self.game_stage

        self.start = None
        self.com_npc = None

        # バトル管理
        self.init_battle = True  # バトル画面初期化フラグ
        self.update_message_flag = False

        # バトル初期化
        self.battle = BattleScreen(self, self.battle_sprites)

    def show_game_menu(self, stage, dt):
        menus = {
            "main": self.main_screen,
            "battle": self.show_battle_screen,
            "game_over": self.show_game_over,
            "start_menu": self.start_menu,
            "community": self.community,
        }
        return menus[stage](dt)
    
    def play_background_music(self, stage):
        """ 音楽を再生する """
        bgm_path = BGM.get(stage)

        if bgm_path and os.path.exists(bgm_path):  # ファイルの存在チェック
            self.bgm = Backmusic(bgm_path)
            self.bgm.play()
            # print(bgm_path)
        else:
            # print(f"音楽ファイルが見つかりません: {bgm_path}")
            pass

    def run(self):
        """ゲームループ"""
        dt = self.clock.tick(FPS) /1000

        while self.running:

            # events
            self.events()
   
            self.show_game_menu(self.game_stage, dt)

            if self.current_stage != self.game_stage:
                self.play_background_music(self.game_stage)
                self.current_stage = self.game_stage

            if not pg.mixer.music.get_busy():
                self.play_background_music(self.game_stage)

            pg.display.flip()
        
        pg.quit()

    def start_menu(self, dt):
        self.display_surface.fill((BLUE))
        if self.start == None:
            self.start = StartMenu(self)
        
        self.start.draw()

    def community(self, dt):
        if self.com_npc == None:
            self.com_npc = Communication(self)

        self.com_npc.draw()

    def main_screen(self, dt):
        self.all_sprites.update(dt, self.current_map)
        self.display_surface.fill(BLUE)
        self.all_sprites.draw()
        self.enemy_sprites.draw()
        if self.battle.status.view_status['HP']:
            val = self.battle.status.view_status['HP']
            self.bar.draw_bar_of_main(100,100+30, val, self.display_surface)

    def show_battle_screen(self, dt):
        # バトル初期化
        if self.init_battle:
            self.battle.reset()
            if not self.player.collided_enemy == None:
                self.battle.draw(self.player)
                self.battle_sprites.draw_battle()
            self.init_battle = False
        
        # バトル更新処理
        self.battle.update(dt)

        # 戦闘コマンドの描画(マウスホーバーを検知するため、ループの外側で実装)
        if self.battle.battle_active:
            self.battle.draw_buttons()

    def show_game_over(self, dt):
        
        self.display_surface.fill((0, 0, 0))  # RGBで黒 (0, 0, 0)
        self.game = GameOver(self)
        self.game.draw()

    # メインステージ、敵の数、Playerの数上手くリセットできていない
    def init_game_state(self):

        for e in self.all_sprites:
            if e.alive(): e.kill()

        # プレイヤーとマップを再生成
        self.player, self.current_map, self.bar = Map(self, self.all_sprites).create()

        # print(f'all:{len(self.all_sprites)}')

        # バトルの状態を完全にリセット
        self.reset_battle()

        # ゲームステージを"main"に戻す
        self.game_stage = 'main'

    def reset_game_state(self, save_info):

        self.player = None

        for e in self.all_sprites:
            if e.alive(): e.kill()

        # プレイヤーとマップを再生成
        self.player, self.current_map, self.bar = Map(self, self.all_sprites).reset(save_info)
        
        # print(f'all:{len(self.all_sprites)}')

        # バトルの状態を完全にリセット
        self.reset_battle()

        # ゲームステージを"main"に戻す
        self.game_stage = 'main'

    def reset_battle(self):

        # メインメニューをリセットする
        self.start = None
        # バトルの状態を完全にリセット
        self.battle = BattleScreen(self, self.battle_sprites)
        self.init_battle = True
        self.battle.reset()


    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # セーブはフィールドマップのみ
                if self.game_stage == 'main':
                    save_data = {
                        "x": max(int(self.player.rect.centerx/TILE_SIZE),2),
                        "y": max(int(self.player.rect.centery/TILE_SIZE),2)
                    }
                    # print(f'pos:{save_data}')
                    game_data = GameData(save_info=save_data)
                    game_data.save()

                self.running = False

            if event.type == pg.KEYDOWN:
                # バトル終了後、メイン画面に戻る処理
                if event.key == pg.K_SPACE and self.game_stage == 'battle':
                    self.battle.get_battle_result()

                elif event.key == pg.K_SPACE and self.game_stage == 'community':
                    self.game_stage = 'main'

            if not self.battle == None: 
                # BattleScreenのマウスイベントを処理
                self.update_message_flag = self.battle.handle_mouse_event(event)

            # メインメニューのマウスイベント処理
            if not self.start == None: self.start.handle_mouse_event(event)

if __name__ == "__main__":
    new_game = Game()
    new_game.run()
