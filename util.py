import pygame as pg
from config import *

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

class Utils:
    def __init__(self):
        self.clock = pg.time.Clock()

    def draw_text(self, text, size, color, x, y, screen):
        self.screen = screen
        self.font = pg.font.SysFont("yumincho", size)
        self.color = color
        self.text = text
        self.x = x
        self.y = y
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (self.x, self.y)
        self.screen.blit(text_surface, text_rect)

    def wait_event(self):
        self.waiting = True
        while self.waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.waiting = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.play_sort_sound()
                    self.waiting = True


    def play_background_music_main_scene(self):
        self.main_background_music = Backmusic('./music/y004.mp3')
        try:
           self.main_background_music.play()
        except Exception as e:
            print(f"音楽ファイルの読み込みに失敗しました: {e}")
    
    def stop_background_music_main_scene(self):
        self.main_background_music.stop()

    def play_sort_sound(self):
        self.main_background_music = Backmusic('./music/sort_snd.mp3')
        try:
           self.main_background_music.play_one()
        except Exception as e:
            print(f"音楽ファイルの読み込みに失敗しました: {e}")

