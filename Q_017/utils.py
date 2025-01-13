import pygame as pg 
from settings import * 

class Util:
    pass


class Backmusic:
    def __init__(self, file):
        self.music = pg.mixer.music.load(file)

    def play(self):
        pg.mixer.music.set_volume(0.5)
        pg.mixer.music.play(-1)

    def play_one(self):
        pg.mixer.music.set_volume(0.5)
        pg.mixer.music.play()

    def stop(self):
        pg.mixer.music.stop()

# ボタンのクラス
class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.color = (0, 0, 200)
        self.hover_color = (200, 0, 0)
        self.font = pg.font.Font("appmin.otf", 24)
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
    def __init__(self, font, fore_color, bg_color, x, y, speed, screen):
        super().__init__()
        self.font = font
        self.color = fore_color
        self.bg_color = bg_color
        self.x = x
        self.y = y
        self.speed = speed
        self.screen = screen
        
    def draw(self, fixed_texts, counter):
        """現在の状態を描画"""
        self.fixed_texts = fixed_texts
        last_line = len(self.fixed_texts)
        # すでに表示された固定テキストを描画
        for i, text in enumerate(self.fixed_texts):
            if i == last_line -1:
                text_surface = self.font.render(text[0:counter//self.speed], True, self.color)
                self.screen.blit(text_surface, (self.x, self.y + i * 32))
            else:
                text_surface = self.font.render(text, True, self.color)
                self.screen.blit(text_surface, (self.x, self.y + i * 32))

