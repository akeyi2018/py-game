import pygame as pg
from settings import *
from utils import Button, Popup, TextSprite

class Battle(pg.sprite.Sprite):
    def __init__(self, all_sprites):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.back_ground_img = pg.transform.scale(pg.image.load('../battle/bg.png'), (819, 614))

        self.bg_size = self.back_ground_img.get_size()

        self.rect = self.back_ground_img.get_rect()
        self.off_set = pg.Vector2()
        self.off_set.x = -int((self.rect.centerx - WIDTH /2))
        self.off_set.y = -int((self.rect.centery - HEIGHT /2))

        self.font = pg.font.Font("../battle/Meiryo.ttf", 24)
        self.battle_message = []
        self.mob_surface = None

        self.show_popup = False  # ポップアップ表示フラグ
        self.popup = self.show_popup_message()

        px = 30
        py = 30
        btn_width = 100
        btn_height = 40
        self.main_buttons = [
            Button(px, py, btn_width,btn_height, "攻撃", self.attack),
            Button(px, py + 50, btn_width,btn_height, "魔法", self.show_sub_commands),
            Button(px, py + 500, btn_width,btn_height, "逃げる", self.escape)
        ]        

        px = 30
        offset = 0
        self.sub_buttons = [
            Button(px, py + offset, btn_width,btn_height, "ホイミ", self.hoimi, ),
            Button(px, py + 50 + offset, btn_width,btn_height, "メラ", self.mera, ),
            Button(px, py + 100 + offset, btn_width,btn_height, "ヒャド", self.hyado, )
        ]

        self.currend_command = self.main_buttons

        self.all_sprites = all_sprites
        self.text_sprites = TextSprite('', self.font, (255,255,255), 250, 430, self.all_sprites)

        pg.display.set_caption('Battle')

    def draw(self, player):
        
        enemy = player.collided_enemy
        self.mob_pos =  ((WIDTH - 128) /2,HEIGHT /8)
        self.mob_surface = enemy.battle_surface.copy()
        self.display_surface.blit(enemy.battle_surface, self.mob_pos)
        
        # メッセージ
        message_str = f'{enemy.name}が現れました!' 
        self.battle_message.append(message_str)
        
        self.draw_text()

    def initial_action(self):
        self.fade_text()
        self.clear_text_area()
        self.check_message()

    def check_message(self):
        if len(self.battle_message) > 5:
            del self.battle_message[0]

    def fade_text(self):
        for alpha in range(0, 120, 5):
            # self.display_surface.fill((0, 0, 0))
            temp_surface = self.back_ground_img.copy()
            temp_surface.set_alpha(alpha)
            self.display_surface.blit(temp_surface, self.rect.topleft + self.off_set)
            self.display_surface.blit(self.mob_surface, self.mob_pos)
            pg.display.flip()
            pg.time.delay(1)

    def draw_text(self):
        # テキストを描画
        self.initial_action()

        self.check_message()
        view_message = ['  ' + item for item in self.battle_message]
        view_message = '\n'.join(view_message)

        # self.text_sprites.update_text(view_message, 128)

        
        self.text_surface = self.font.render(view_message, True, (255, 255, 255))  # 白色でテキストを描画
        self.display_surface.blit(self.text_surface, (255, 432))

    def clear_text_area(self):
        """必要最小限の透明マスクを新規作成し、配置する"""

        # テキスト描画用の最小領域を定義
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

    
    def draw_menu_backgroud(self):
        pg.draw.rect(self.display_surface, (0, 200, 200), [2, 2, self.off_set.x -2, HEIGHT-2])
        pg.draw.rect(self.display_surface, (255, 255, 255), [0, 0, self.off_set.x, HEIGHT],5,border_radius=5)

    # 描画
    def draw_buttons(self):
        for button in self.currend_command:
            button.draw(self.display_surface)

        # メインコマンドを表示
    def show_main_commands(self):
        self.currend_command = self.main_buttons

    # サブコマンドを表示
    def show_sub_commands(self):
        # print('SUB COMMAND')
        self.currend_command = self.sub_buttons

    def handle_mouse_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # クリックした位置を取得
            for button in self.currend_command:
                if button.check_click(mouse_pos):  # ボタンがクリックされたか判定
                    button.action()  # ボタンに設定された関数を呼び出し

    def show_popup_message(self):
        # ポップアップを表示する
        # self.show_popup = True
        self.popup = Popup(
            screen=self.display_surface,
            text="Button Clicked!",
            rect=(0, 200, self.off_set.x, HEIGHT-200),
            bg_color=(0, 0, 200),
            text_color=(125, 250, 125)
        )
        return self.popup

    def attack(self):
        self.battle_message.append('攻撃')
       
        self.draw_text()


    def magic(self):
        self.battle_message.append('魔法')
       
        self.draw_text()


    def escape(self):
        self.battle_message.append('逃げる')
      
        self.draw_text()

    def hoimi(self):
        # print('hoimi')
        self.battle_message.append('ホイミ')
        self.draw_text()
        self.show_main_commands()

    def mera(self):
        self.battle_message.append('メラ')
        self.draw_text()
        self.show_main_commands()

    def hyado(self):
        self.battle_message.append('ヒャド')
        self.draw_text()
        self.show_main_commands() 

    def fade_in(self):
        for alpha in range(0, 125, 5):
            temp_surface = self.back_ground_img.copy()
            temp_surface.set_alpha(alpha)
            self.display_surface.blit(temp_surface, self.rect.topleft + self.off_set)
            pg.display.flip()
            pg.time.delay(30)
