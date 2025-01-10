import pygame as pg
from settings import *
from utils import Button, TextSprite
from status import PlayerStatus

class BattleMenu:
    def __init__(self, actions):
        self.display_surface = pg.display.get_surface()
        
        self.px = 30
        self.main_pos_y = [30, 80, 530]
        self.sub_pos_y = [30, 80, 130] 

        self.buttons = {
            "main": self.create_buttons(actions['main'], self.px, self.main_pos_y),
            "sub": self.create_buttons(actions['sub'], self.px, self.sub_pos_y),
        }
        
        self.currend_command = "main"

    def create_buttons(self, actions, x, y_positons):
        btn_width, btn_height = 100, 40
        return [
            Button(x, y_positons[i], btn_width, btn_height, name, action)
            for i, (name, action) in enumerate(actions)
        ]

    # メインコマンドを表示
    def show_main_commands(self):
        self.currend_command = 'main'

    def show_sub_commands(self):
        self.currend_command = 'sub'

    # 描画
    def draw_buttons(self):
        for button in self.buttons[self.currend_command]:
            button.draw(self.display_surface)

    def handle_mouse_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # クリックした位置を取得
            for button in self.buttons[self.currend_command]:
                if button.check_click(mouse_pos):  # ボタンがクリックされたか判定
                    button.action()  # ボタンに設定された関数を呼び出し
                    return True

class BattleLayout:
    def __init__(self):
        self.display_surface = pg.display.get_surface()
        self.back_ground_img = pg.image.load('../battle/bg.png')
        self.back_ground_img = pg.transform.scale(self.back_ground_img, (819, HEIGHT))

        self.bg_size = self.back_ground_img.get_size()
        self.rect = self.back_ground_img.get_rect()
        self.off_set = pg.Vector2()
        self.off_set.x = -int((self.rect.centerx - WIDTH /2))
        self.off_set.y = -int((self.rect.centery - HEIGHT /2))
    
    def draw_background(self, screen):
        self.screen = screen
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.back_ground_img, self.rect.topleft + self.off_set)

    def draw_menu_backgroud(self):
        pg.draw.rect(self.display_surface, '#8E7698', [2, 2, self.off_set.x -2, HEIGHT-2])
        pg.draw.rect(self.display_surface,'#D3DED0', [0, 0, self.off_set.x, HEIGHT],5,border_radius=5)

    def draw_background_text_area(self):
        """必要最小限の透明マスクを新規作成し、配置する"""
        self.text_area_rect = pg.Rect(250, 430, self.bg_size[0] * 0.95, self.bg_size[1] * 0.3)

        # 半透明の背景色を設定
        semi_transparent_surface = pg.Surface(self.text_area_rect.size, pg.SRCALPHA)
        semi_transparent_surface.fill((0, 0, 255, 50))  # 半透明の青色
        
        # 角の描画ですこし小さくする
        self.display_surface.blit(semi_transparent_surface, 
                                  [self.text_area_rect.x + 2,
                                   self.text_area_rect.y + 2,
                                   self.text_area_rect.width -2,
                                   self.text_area_rect.height -2])

        # 枠線を再描画
        pg.draw.rect(self.display_surface, (255, 255, 255), self.text_area_rect, 3, border_radius=5)

class BattleScreen(pg.sprite.Sprite):
    def __init__(self, battle_sprites):
        super().__init__()
        self.display_surface = pg.display.get_surface()

        self.font = pg.font.Font("../battle/Meiryo.ttf", MESSAGE_FONT_SIZE)
        # self.battle_message = []

        self.enemy = None

        self.battle_sprites = battle_sprites

        # Layout
        self.layout = BattleLayout()

        self.current_command = 0

        # menu
        self.menu = BattleMenu(self.get_actions())

        # player status
        self.status = PlayerStatus((BG_SIZE_WIDTH, HEIGHT), self.battle_sprites)
        
        # messege
        self.text_sprites = TextSprite('', self.font, (255,255,255),  (0,0,255), 250, 430, self.battle_sprites)

    def get_actions(self):
        return {
            "main": [
                ("攻撃", self.attack),
                ("魔法", self.show_sub_commands),
                ("逃げる", self.escape),
            ],
            "sub": [
                ("ホイミ", self.hoimi),
                ("メラ", self.mera),
                ("ヒャド", self.hyado),
            ],
        }

    def attack(self):
        # 攻撃力は HP* 0.8
        mes = f'{self.status.view_status['name']}は攻撃しました。' + \
            f'{self.enemy.name}は{int(self.status.infact_status['ATK'] / 4) - int(self.enemy.mob_info['DEF']/3)}のダメージを受けました。'
        self.general_message([mes])

    def escape(self):
        self.battle_message.append('逃げる')

    def hoimi(self):
        self.battle_message.append('ホイミ')
        self.menu.show_main_commands()

    def mera(self):
        self.battle_message.append('メラ')
        self.menu.show_main_commands()

    def hyado(self):
        self.battle_message.append('ヒャド')
        self.menu.show_main_commands()

    # サブコマンドを表示
    def show_sub_commands(self):
        self.menu.show_sub_commands()

    def draw(self, player, screen):
        self.enemy = player.collided_enemy
        self.mob_pos =  ((WIDTH - 128) /2,HEIGHT /8)
        self.mob_surface = self.enemy.battle_surface.copy()
        # メッセージ
        self.battle_message.append(f'{self.enemy.name}が現れました!') 
        self.render_scene(screen)

    def render_scene(self, screen):
        self.layout.draw_background(screen)

        self.display_surface.blit(self.enemy.battle_surface, self.mob_pos)

        self.layout.draw_background_text_area()

        self.draw_text(screen)
        self.layout.draw_menu_backgroud()

        # player status
        self.status.draw_status(screen)

    def update_message(self, screen):
        self.render_scene(screen)

    def general_message(self, message_list):
        for m in message_list:
            self.battle_message.append(m)
            if len(self.battle_message) > MAX_MESSAGE:
                del self.battle_message[0]

    def set_message(self):
        if len(self.battle_message) > MAX_MESSAGE:
            del self.battle_message[0]

        view_message = ['  ' + item for item in self.battle_message]
        return '\n'.join(view_message)

    def draw_text(self, screen):
        self.text_sprites.update_message(screen, self.set_message())

    def handle_mouse_event(self, event):
        return self.menu.handle_mouse_event(event)
    
    def draw_buttons(self):
        self.menu.draw_buttons()
