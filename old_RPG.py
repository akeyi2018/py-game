import pygame
from sprites import *
from config import *
from util import *
from py_sprites import *
import sys

class game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT + MESSAGE_AREA_HEIGHT))
        self.caption = pygame.display.set_caption("Python Game") 
        self.clock = pygame.time.Clock()
        self.running = True
        self.mobs = pygame.sprite.Group()
        self.util = Utils()
        self.character_spritesheet = Spritesheet('./img/F1.png')
        self.terrain_spritesheet = Spritesheet('./img/terrain.png')
        self.mob_spritesheet = Spritesheet('./img/enemy.png')
        self.battle_spritesheet = Spritesheet('./img/terrain.png')

    def load_contents(self):
        self.music = Backmusic('./music/y004.mp3')
        self.music.play()

    def createTilemap(self):
        
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == 'B':
                    Block(self, j, i)
                if column == 'P':
                    Player(self, j, i)
                if column == 'E':
                    Mob(self, j, i)

    def create_battlemap(self):
        for i, row in enumerate(battlemap):
            for j, column in enumerate(row):
                Battle(self, j, i)
        
    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.mobs = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.createTilemap()
        self.load_contents()
        # self.create_battlemap() 

    def events(self):
        # game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()
        
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def game_over(self):
        pass

    def intro_screen(self):
        self.music = Backmusic('./music/ks026.mp3')
        self.music.play()
        self.screen.fill(BGCOLOR)
        # create a surface object, image is drawn on it.
        self.image = pygame.image.load('./img/fortress.png').convert_alpha()
        alpha_surface = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
        alpha_surface.fill((255, 255, 255, 10))
        self.screen.blit(alpha_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        pygame.draw.rect(self.screen, BUTTON_COLOR_1, [150, WIN_HEIGHT * 3 / 4 -10, 300,50])

        self.util.draw_text("西暦2021年 春", 30, 
                             MOJICOLOR, WIN_WIDTH / 2, WIN_HEIGHT / 4, self.screen)
        self.util.draw_text("ITエンジニアという道に、少年Aが挑戦した物語", 25,
                             MOJICOLOR, WIN_WIDTH / 2, WIN_HEIGHT / 2, self.screen)
        self.util.draw_text("Start new Game", 28, 
                             MOJICOLOR, WIN_WIDTH / 2, WIN_HEIGHT * 3 / 4, self.screen)
        pygame.display.flip()
        self.util.wait_event()
        self.music.stop()
          

if __name__ == "__main__":
    new_game = game()
    new_game.intro_screen()
    new_game.new()
    while new_game.running:
        new_game.main()
        new_game.game_over()

    pygame.quit()       # Pygameの終了(画面閉じられる)
    sys.exit()