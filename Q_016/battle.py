import pygame as pg
from settings import *
from utils import Button, TextSprite
from status import PlayerStatus

class Battle(pg.sprite.Sprite):
    def __init__(self, battle_sprites):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.back_ground_img = pg.image.load('../battle/bg.png')
        self.back_ground_img = pg.transform.scale(self.back_ground_img, (819, HEIGHT))

        self.bg_size = self.back_ground_img.get_size()

        self.rect = self.back_ground_img.get_rect()
        self.off_set = pg.Vector2()
        self.off_set.x = -int((self.rect.centerx - WIDTH /2))
        self.off_set.y = -int((self.rect.centery - HEIGHT /2))

        self.font = pg.font.Font("../battle/Meiryo.ttf", 24)
        self.battle_message = []
        self.surface = None

        self.enemy = None

        px = 30
        py = 30
        pos_y = [30, 130, 530]
        btn_width = 100
        btn_height = 40
        self.main_buttons = [
            Button(px, pos_y[i], btn_width, btn_height, name, action)
            for i, (name, action) in enumerate([
                ("攻撃", self.attack), 
                ("魔法", self.show_sub_commands), 
                ("逃げる", self.escape)])
        ]        

        px = 30
        offset = 0
        self.sub_buttons = [
            Button(px, py + offset, btn_width,btn_height, "ホイミ", self.hoimi, ),
            Button(px, py + 50 + offset, btn_width,btn_height, "メラ", self.mera, ),
            Button(px, py + 100 + offset, btn_width,btn_height, "ヒャド", self.hyado, )
        ]

        self.currend_command = self.main_buttons

        self.battle_sprites = battle_sprites

        # player status
        self.status = PlayerStatus(self.off_set, self.bg_size, self.battle_sprites)
        
        # messege
        self.text_sprites = TextSprite('', self.font, (255,255,255),  (0,0,255), 250, 430, self.battle_sprites)

    def draw_background(self, screen):
        self.screen = screen
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.back_ground_img, self.rect.topleft + self.off_set)

    def draw(self, player, screen):
        self.enemy = player.collided_enemy
        self.mob_pos =  ((WIDTH - 128) /2,HEIGHT /8)
        self.mob_surface = self.enemy.battle_surface.copy()
        # メッセージ
        self.battle_message.append(f'{self.enemy.name}が現れました!') 
        self.render_scene(screen)

    def render_scene(self, screen):
        self.draw_background(screen)
        self.display_surface.blit(self.enemy.battle_surface, self.mob_pos)

        self.draw_background_text_area()
        self.draw_text(screen)
        self.draw_menu_backgroud()

        # player status
        self.status.draw_status(screen)


    def update_message(self, screen):
        self.render_scene(screen)

    def set_message(self):
        if len(self.battle_message) > 5:
            del self.battle_message[0]

        view_message = ['  ' + item for item in self.battle_message]
        return '\n'.join(view_message)

    def draw_text(self, screen):
        self.text_sprites.update_message(screen, self.set_message())

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

    
    def draw_menu_backgroud(self):
        pg.draw.rect(self.display_surface, '#8E7698', [2, 2, self.off_set.x -2, HEIGHT-2])
        pg.draw.rect(self.display_surface,'#D3DED0', [0, 0, self.off_set.x, HEIGHT],5,border_radius=5)

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
                    return True

    def attack(self):
        self.battle_message.append('攻撃')

    def escape(self):
        self.battle_message.append('逃げる')

    def hoimi(self):
        self.battle_message.append('ホイミ')
        self.show_main_commands()

    def mera(self):
        self.battle_message.append('メラ')
        self.show_main_commands()

    def hyado(self):
        self.battle_message.append('ヒャド')
        self.show_main_commands()
