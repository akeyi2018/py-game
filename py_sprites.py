import pygame
from config import *
import math 
import random
from util import Utils 

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self.util = Utils()
        self.screen = self.game.screen
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0
        self.facing = 'down'

        self.image = self.game.character_spritesheet.get_sprite(2, 4, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.rect.x += self.x_change
        self.collide_blocks('x') 
        self.rect.y += self.y_change
        self.collide_blocks('y')
        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'    

    def collide_blocks(self, direction):
        mob_hits = pygame.sprite.spritecollide(self, self.game.mobs, False)
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        if direction == 'x':
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

            if mob_hits:
                if self.x_change > 0:
                    self.rect.x = mob_hits[0].rect.left - self.rect.width
                    self.show()
                if self.x_change < 0:
                    self.rect.x = mob_hits[0].rect.right
                    self.show()

        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

            if mob_hits:
                if self.y_change > 0:
                    self.rect.y = mob_hits[0].rect.top - self.rect.height
                    self.show()
                if self.y_change < 0:
                    self.rect.y = mob_hits[0].rect.bottom
                    self.show()

    def show(self):
        self.util.draw_text("モンスターが現れました。", 20, 
                             MOJICOLOR, WIN_WIDTH / 2, WIN_HEIGHT + 60, self.screen)
        pygame.display.flip()
        self.util.wait_event()

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game =game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(960, 448, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0,0),(x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite

class Backmusic:
    def __init__(self, file):
        self.music = pygame.mixer.music.load(file)

    def play(self):
        pygame.mixer.music.play(-1)

    def stop(self):
        pygame.mixer.music.stop()
        
class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(64, 352, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Mob(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = EVENT_LAYER
        self.groups = self.game.all_sprites, self.game.mobs
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.mob_spritesheet.get_sprite(0,2, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Battle(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.util = Utils()
        self.game = game
        # self._layer = BATTLE_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.battle_spritesheet.get_sprite(933,645, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = 480 + self.y
    