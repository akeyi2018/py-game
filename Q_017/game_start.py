import pygame as pg

from settings import *
from utils import TextSprite, Button, TextAnimation
from save_load import GameData

class StartMenu:
    def __init__(self, parent):
        self.parent = parent
        self.screen = self.parent.display_surface
        self.start_sprites = pg.sprite.Group()
        self.font_size = 36
        # self.font_description = pg.font.Font('SimHei.ttf', 24)
        self.font_description = pg.font.Font(FONT, 24)
        self.forecolor = "#FFFFFF"
        self.text = TextSprite('北境の黎明', self.font_size, 
                               self.forecolor,  
                               (0,0,255), 
                               WIDTH / 2 - 200, 50, self.start_sprites)
        
        self.speed = 100

        self.stage = 'start'
        
        
        self.img = pg.image.load('../img/winter-forest1.jpg')
        self.back_ground_img = pg.transform.scale(self.img, (WIDTH, HEIGHT))
        self.rect = self.back_ground_img.get_rect()
        
        self.story_description = '清朝末期。歴史に稀を見る時代は混乱を極み、\n\
中原の人々は天災、戦乱、飢饉により、酷寒で漢民族の禁足の地の満州に渡った、\n\
その中、ひとりの若者が静かに動き出すのだった...'
#         self.story_description = '烈风带残云，落花天地白。万物静，鸟不鸣。\n\
# 中原の人々は天災、戦乱、飢饉により、酷寒で漢民族の禁足の地の満州に渡った、\n\
# その中、ひとりの若者が静かに動き出すのだった...'
        self.descriptions = TextAnimation(
            self.font_description,
            self.forecolor, (0,0,255),
            WIDTH*0.15 , HEIGHT /2 -200 , 
            self.speed,
            self.screen
        )
        
        self.px = WIDTH / 2
        self.pos_y = [HEIGHT /2 + 100, HEIGHT /2 + 150, HEIGHT /2 + 200]

        self.buttons = self.create_buttons(self.get_actions(), 
                                           self.px, 
                                           self.pos_y)
        
        self.counter = 0

    def get_actions(self):
        return [
            ("Start", self.start),
            ("Load", self.load),
            ("Settings", self.option),
        ]
    
    def create_buttons(self, actions, x, y_positons):
        btn_width, btn_height = 100, 40
        return [
            Button(x, y_positons[i], btn_width, btn_height, name, action)
            for i, (name, action) in enumerate(actions)
        ]

    def draw(self):

        self.screen.blit(self.back_ground_img, self.rect)
        self.text_area = pg.Rect(WIDTH*(0.15)-5, HEIGHT*0.05, WIDTH * 0.7, HEIGHT * 0.4)
        surf = pg.Surface(self.text_area.size, pg.SRCALPHA)
        surf.fill((10,15,5,128))
        self.screen.blit(surf, self.text_area)
        self.text.draw(self.screen)

        self.draw_text_anime()

        for button in self.buttons:
            button.draw(self.screen)


    def draw_text_anime(self):
        flag, self.counter = self.descriptions.draw_anime(self.story_description, self.counter)

        if flag and self.counter <= len(self.story_description) :
            self.counter += 1


    def handle_mouse_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # クリックした位置を取得
            for button in self.buttons:
                if button.check_click(mouse_pos):  # ボタンがクリックされたか判定
                    button.action()  # ボタンに設定された関数を呼び出し
                    return True

    def start(self):
        print('start')
        self.parent.init_game_state()

    def load(self):
        print('load')
        game_data = GameData()
        save_info = game_data.load_files()
        
        self.parent.reset_game_state(save_info)

    def option(self):
        print('option')
        

class LoadMenu:
    def __init__(self):
        self.img = pg.image.load('../img/load_menu.png')
        self.back_ground_img = pg.transform.scale(self.img, (WIDTH, HEIGHT))
        self.rect = self.back_ground_img.get_rect()

    def draw(self, screen):
        screen.fill((0,0,0))
        screen.blit(self.back_ground_img, self.rect)
    
