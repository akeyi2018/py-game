import pygame as pg
from sub.settings import *
from utils import Button, TextAnimation, Sound, TextSprite
from sub.status import PlayerStatus
import queue
from sub.battle_menu import BattleMenu
from sub.battle_layout import BattleLayout
from sub.magic import Magic, Magic_maneger, Model

class BattleScreen(pg.sprite.Sprite):
    def __init__(self, parent, battle_sprites):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.font = pg.font.Font(FONT, MESSAGE_FONT_SIZE)

        self.enemy = None

        self.parent = parent

        self.battle_sprites = battle_sprites

        # Layout
        self.layout = BattleLayout()

        self.current_command = 0
        self.speed = 100
        self.counter = 0

        # menu
        self.menu = BattleMenu(self.get_actions())

        # player status
        self.status = PlayerStatus((BG_SIZE_WIDTH, HEIGHT), self.battle_sprites)
        
        # messege
        self.text_sprites = TextAnimation(self.font, 
                                          (255,255,255),  (0,0,255), 
                                          250, 435, 
                                          self.speed, 
                                          self.display_surface)

        # Battle state
        self.battle_active = True  # 戦闘がアクティブかどうかを管理するフラグ
        
        self.battle_message = []

        self.message_next_flag = True
        self.msg_que = queue.Queue()

        self.que_cool_timer = 0
        self.que_cool_down = 50

    def reset(self):
        # バトル関連の状態をリセット
        self.battle_message = []
        self.battle_active = True
        self.current_command = None
        self.enemy = None

    def update(self, dt):
        self.process_message_queue()
        self.get_que_cool_time()
        self.text_sprites.update(dt)
        self.draw_messages()
        # HP更新
        self.status.draw_status(self.display_surface)

    def process_message_queue(self):
        if self.msg_que.qsize() > 0 and self.message_next_flag:
            que = self.msg_que.get()
            self.que_cool_timer = pg.time.get_ticks()
            self.battle_message.append(que)
            if len(self.battle_message) > MAX_MESSAGE:
                del self.battle_message[0]
            self.message_next_flag = False

    def get_actions(self):
        # 
        magic_list = Magic_maneger(self).magic_list
        magic_list.append(("cancel", self.cancel))   
        # print(magic_list)     

        return {
            "main": [
                ("Attack", self.attack),
                ("Magic", self.show_sub_commands),
                ("逃げる", self.escape),
            ],
            "magic": magic_list,
        }

    def attack(self):
        # 攻撃力は HP* 0.8
        damege = int(self.status.infact_status['ATK'] / 4) - int(self.enemy.mob_info['DEF']/3)
        # damege = int(self.status.infact_status['ATK']*2 ) - int(self.enemy.mob_info['DEF']/3)

        self.enemy.mob_info['HP'] -= damege
        # self.enemy.mob_info['HP'] -= 200
        
        mes = f'{self.status.view_status['name']}は攻撃しました。' + \
            f'{self.enemy.name}は{damege}のダメージを受けました。'
        self.general_message([mes])
        self.music = Sound('../music/battle/tm2_swing000.wav')
        self.music.play()
        if self.enemy.mob_info['HP'] <= 0:
            self.music = Sound('../music/battle/win_001.wav')
            self.music.play()
            mes_02 = f'{self.enemy.name}を倒しました。'
            self.general_message([mes_02])
            self.battle_active = False  # 戦闘終了フラグを設定        
        # 反撃(一回でPlayerが倒される)
        else:
            p_damege = int(self.enemy.mob_info['STR']) - int(self.status.infact_status['DEF']/4)
            # p_damege = 200

            self.status.view_status['HP'] -= p_damege
            if self.status.view_status['HP'] <= 0 : self.status.view_status['HP'] = 0
            mes_02 = f'{self.enemy.name}の攻撃、' + \
            f'{self.status.view_status['name']}は{p_damege}のダメージを受けました。'
            self.general_message([mes_02])
            if self.status.view_status['HP'] == 0:
                self.music = Sound('../music/battle/game_over_001.wav')
                self.music.play()
                mes_03 = f'{self.status.view_status['name']}は倒れました。'
                self.general_message([mes_03])
                self.battle_active = False  # 戦闘終了フラグを設定

    def get_battle_result(self):
        if self.enemy.mob_info['HP'] <= 0:
            self.parent.init_battle = True
            self.battle_active = True
            self.parent.game_stage = 'main'
        elif self.status.view_status['HP'] == 0:

            self.parent.game_stage = 'game_over'

    def get_que_cool_time(self):
        if not self.message_next_flag:
            current_time = pg.time.get_ticks()
            if current_time - self.que_cool_timer >= self.que_cool_down:
                self.message_next_flag = True

    def escape(self):
        self.msg_que.put(f'  逃げる')

    def cancel(self):
        self.menu.show_main_commands()

    # サブコマンドを表示
    def show_sub_commands(self):
        self.menu.show_sub_commands()

    def draw(self, player):
        self.enemy = player.collided_enemy
        self.mob_pos =  ((WIDTH - 128) /2,HEIGHT /8)

        self.mob_surface = self.enemy.surface
        
        self.msg_que.put(f'  {self.enemy.name}が現れました!')
        
        self.render_scene()

    def draw_messages(self):
        if len(self.battle_message) > 0:
            flag, self.counter = self.text_sprites.draw(
                self.battle_message, 
                self.counter
            )
            if flag and self.counter <= len(self.battle_message[-1]):
                self.counter += 1

    def render_scene(self):
        # 背景レイヤー
        self.layout.draw_background(self.display_surface)

        # キャラクターレイヤー
        if self.battle_active or self.status.view_status['HP'] <= 0:
            self.display_surface.blit(self.enemy.battle_surface, self.mob_pos)

        # UIレイヤー
        self.layout.draw_background_text_area(self.display_surface)
        self.status.draw_status(self.display_surface)

        # メニューレイヤー（最前面）
        self.layout.draw_menu_background()
        if self.battle_active:
            self.draw_buttons()  

    def update_message(self, screen):
        self.render_scene(screen)

    def general_message(self, message_list):

        view_message = ['  ' + item for item in message_list]
        view_message = '\n'.join(view_message)

        # キューに入れる
        self.msg_que.put(view_message)

    def handle_mouse_event(self, event):
        # 戦闘中のみボタンの押下処理を有効化
        if self.battle_active:
            return self.menu.handle_mouse_event(event)
        return False
    
    def draw_buttons(self):

        self.menu.draw_buttons(self.layout)
