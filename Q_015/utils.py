import pygame as pg 
from settings import * 

class Util:
    pass


# ボタンのクラス
class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.color = (0, 0, 200)
        self.hover_color = (200, 0, 0)
        self.font = pg.font.Font("../battle/Meiryo.ttf", 24)
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        self.current_color = self.color  # 現在の色

    def draw(self, screen):
        
        # マウスがホバーしている場合の色を変更
        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            # pg.draw.rect(screen, self.hover_color, self.rect)
            self.current_color = self.hover_color
        else:
            self.current_color = self.color
            # pg.draw.rect(screen, self.color, self.rect)

        # pg.draw.rect(screen, self.current_color, self.rect)
        pg.draw.rect(screen, self.current_color, self.rect, border_radius=5)
        screen.blit(self.text_surface, self.text_rect)

    def check_click(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


    
class TextSprite(pg.sprite.Sprite):
    def __init__(self, text, font, color, x, y, all_sprites):
        super().__init__()
        self.text = text
        self.font = font
        self.color = color
        self.image = self.font.render(self.text, True, self.color, (0,0,255))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.alpha = 0
        self.all_sprites = all_sprites
        self.all_sprites.add(self)

    def update_text(self, new_text, alpha):
        """テキストを更新"""
        self.text = new_text
        self.alpha += alpha
        if self.alpha >= 255: self.alpha = 0
        self.surface = self.font.render(self.text, True, self.color, (0,0,255))
        # self.surface.set_alpha(self.alpha)

    def update_color(self, new_color):
        """色を更新"""
        self.color = new_color
        self.image = self.font.render(self.text, True, self.color, (0,0,255))
    


class Popup:
    def __init__(self, screen, text, rect, bg_color, text_color):
        self.screen = screen
        self.rect = pg.Rect(rect)
        self.bg_color = bg_color
        self.text_color = text_color
        self.text = text
        self.font = pg.font.Font(None, 36)
        self.text_surface = None

    def draw(self, command):

        pg.draw.rect(self.screen, self.bg_color, self.rect)
        pg.draw.rect(self.screen, (255, 255, 255),self.rect, 5, border_radius=5)

        if command == 2:
            self.create_sub_atack_commands()

    def create_sub_atack_commands(self):
        px = 30
        py = 230
        btn_width = 100
        btn_height = 40
        self.action_buttons = [
            Button(px, py, btn_width,btn_height, "ホイミ", self.hoimi, 1),
            Button(px, py + 50, btn_width,btn_height, "メラ", self.mera, 2),
            Button(px, py + 100, btn_width,btn_height, "ヒャド", self.hyado, 3)
        ]        

        # ボタンを描画
        for button in self.action_buttons:
            mouse_pos = pg.mouse.get_pos()
            button.update(mouse_pos)
            button.draw(self.screen)

    def handle_mouse_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # クリックした位置を取得
            for button in self.action_buttons:
                if button.check_click(mouse_pos):  # ボタンがクリックされたか判定
                    button.action()  # ボタンに設定された関数を呼び出し

    def hoimi(self):
        print('hoimi')

    def mera(self):
        print('mera')

    def hyado(self):
        print('hyado')      


