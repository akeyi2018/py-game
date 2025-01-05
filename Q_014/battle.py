import pygame as pg
from settings import *
from utils import Button

class Battle:
    def __init__(self):

        self.display_surface = pg.display.get_surface()
        self.back_ground_img = pg.image.load('../battle/bg.png').convert()
        self.bg_size = self.back_ground_img.get_size()

        self.rect = self.back_ground_img.get_rect()
        self.off_set = pg.Vector2()
        self.off_set.x = -int((self.rect.centerx - WIDTH /2))
        self.off_set.y = -int((self.rect.centery - HEIGHT /2))

        self.font = pg.font.Font("../battle/Meiryo.ttf", 24)
        self.battle_message = []
        self.mob_surface = None
        pg.display.set_caption('Battle')

        self.controller = 200

    def draw(self, player):
        
        enemy = player.collided_enemy
        self.mob_pos =  ((WIDTH - 128) /2,HEIGHT /8)
        self.mob_surface = enemy.battle_surface.copy()
        self.display_surface.blit(enemy.battle_surface, self.mob_pos)

        self.action_command()
        
        # メッセージ
        message_str = f'{enemy.name}が現れました!' 
        self.battle_message.append(message_str)

        self.clear_text_area()
        self.draw_text()

    def initial_action(self):
        self.fade_text()
        self.clear_text_area()
        self.check_message()

    def check_message(self):
        if len(self.battle_message) > 5:
            del self.battle_message[0]

    def fade_text(self):
        for alpha in range(0, 70, 5):
            # self.display_surface.fill((0, 0, 0))
            temp_surface = self.back_ground_img.copy()
            temp_surface.set_alpha(alpha)
            self.display_surface.blit(temp_surface, self.rect.topleft + self.off_set)
            pg.display.flip()
            pg.time.delay(1)
        self.display_surface.blit(self.mob_surface, self.mob_pos)

    def draw_text(self):
        self.check_message()
        view_message = ['  ' + item for item in self.battle_message]
        view_message = '\n'.join(view_message)

        # テキストを描画
        self.text_surface = self.font.render(view_message, True, (255, 255, 255))  # 白色でテキストを描画
        self.display_surface.blit(self.text_surface, (250, 430))

    def clear_text_area(self):
        """必要最小限の透明マスクを新規作成し、配置する"""

        # テキスト描画用の最小領域を定義
        self.text_area_rect = pg.Rect(250, 430, self.bg_size[0] * 0.95, self.bg_size[1] * 0.3)

        # 半透明の背景色を設定
        semi_transparent_surface = pg.Surface(self.text_area_rect.size, pg.SRCALPHA)
        semi_transparent_surface.fill((0, 0, 255, 128))  # 半透明の青色

        # 新規マスク付きSurfaceを描画
        self.display_surface.blit(semi_transparent_surface, self.text_area_rect.topleft)

        # 枠線を再描画
        pg.draw.rect(self.display_surface, (255, 255, 255), self.text_area_rect, 3, border_radius=5)

    def action_command(self):
        px = 100
        py = 300
        btn_width = 100
        btn_height = 40
        self.action_buttons = [
            Button(px, py, btn_width,btn_height, "攻撃", self.attack),
            Button(px, py + 50, btn_width,btn_height, "魔法", self.magic),
            Button(px, py + 100, btn_width,btn_height, "逃げる", self.escape)
        ]        

        # ボタンを描画
        for button in self.action_buttons:
            button.draw(self.display_surface)

    def handle_mouse_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # クリックした位置を取得
            for button in self.action_buttons:
                if button.check_click(mouse_pos):  # ボタンがクリックされたか判定
                    button.action()  # ボタンに設定された関数を呼び出し
        
    def attack(self):
        self.initial_action()
        self.battle_message.append('攻撃')
        # print("攻撃!")
        self.draw_text()
        pg.display.update()

    def magic(self):
        self.initial_action()
        self.battle_message.append('魔法')
        # print("魔法!")
        self.draw_text()
        pg.display.update()

    def escape(self):
        self.initial_action()
        self.battle_message.append('逃げる')
        self.draw_text()
        pg.display.update()
    

    def fade_in(self):
        for alpha in range(0, 125, 5):
            # self.display_surface.fill((0, 0, 0))
            temp_surface = self.back_ground_img.copy()
            temp_surface.set_alpha(alpha)
            self.display_surface.blit(temp_surface, self.rect.topleft + self.off_set)
            pg.display.flip()
            pg.time.delay(30)
