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
            self.current_color = self.hover_color
        else:
            self.current_color = self.color
            
        pg.draw.rect(screen, self.current_color, self.rect, border_radius=5)
        screen.blit(self.text_surface, self.text_rect)

    def check_click(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
class TextSprite(pg.sprite.Sprite):
    def __init__(self, text, font, fore_color, bg_color, x, y, all_sprites):
        super().__init__()
        self.text = text
        self.font = font
        self.color = fore_color
        self.bg_color = bg_color
        # self.image = self.font.render(self.text, True, self.color, self.bg_color)
        self.image = self.font.render(self.text, True, self.color)
        self.surface = self.image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.alpha = 0
        self.all_sprites = all_sprites
        self.all_sprites.add(self)

    def update_message(self, screen, message):
        self.screen = screen
        self.text = message
        self.image = self.font.render(self.text, True, self.color)
        self.surface = self.image

    def draw(self, screen):
        self.screen = screen
        self.screen.blit(self.surface, self.rect.topleft)


class TextAnimation(pg.sprite.Sprite):
    def __init__(self, font, fore_color, bg_color, x, y, all_sprites):
        super().__init__()
        self.font = font
        self.color = fore_color
        self.bg_color = bg_color
        self.current_text = ''  # 現在表示されている文字列（1文字ずつ表示）
        self.full_text = ''  # 完全なテキスト（最初は全て表示されない）
        self.image = self.font.render(self.current_text, True, self.color)
        self.surface = self.image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.all_sprites = all_sprites
        self.all_sprites.add(self)
        self.animation_timer = 0  # アニメーションの経過時間

    def update(self, delta_time):
        """ 1文字ずつアニメーションで表示する """
        self.animation_timer += delta_time
        if self.animation_timer >= 5:  # 30msごとに1文字追加
            if len(self.current_text) < len(self.full_text):
                self.current_text += self.full_text[len(self.current_text)]  # 1文字追加
                self.image = self.font.render(self.current_text, True, self.color)
                self.surface = self.image
            self.animation_timer = 0  # タイマーをリセット

    def display_text_animation(self, screen, message):
        """ メッセージを引数として受け取り、1文字ずつ表示するアニメーション """
        print(message)
        self.full_text = message  # 引数で受け取ったメッセージを設定
        self.current_text = ''  # 現在の表示テキストをリセット
        self.image = self.font.render(self.current_text, True, self.color)  # 変更後のテキストを空文字で初期化
        self.surface = self.image
        self.animation_timer = 0  # アニメーションをリセット
        
        # screen.fill((0, 0, 0))  # 背景を毎フレーム白に塗りつぶし
        screen.blit(self.surface, self.rect.topleft)
        pg.display.update()


