import pygame
import random

# Pygameの初期化
pygame.init()

# 画面のサイズ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 画面の作成
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Layered Sprite Example")

# スプライトクラスの定義
class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.image.fill((135, 206, 250))  # 空の色
        self.rect = self.image.get_rect()

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((34, 139, 34))  # 緑色のブロック
        self.rect = self.image.get_rect(topleft=(x, y))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))  # 赤色の敵
        self.rect = self.image.get_rect(topleft=(x, y))

class Citizen(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 0, 255))  # 青色の町人
        self.rect = self.image.get_rect(topleft=(x, y))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 255, 0))  # 黄色のプレイヤー
        self.rect = self.image.get_rect(topleft=(x, y))

# スプライトグループの作成
background_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
citizen_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

# 背景の追加
background = Background()
background_group.add(background)

# ブロックの追加
for _ in range(10):
    x = random.randint(0, SCREEN_WIDTH - 50)
    y = random.randint(100, SCREEN_HEIGHT - 50)
    block = Block(x, y)
    block_group.add(block)

# 敵の追加
for _ in range(5):
    x = random.randint(0, SCREEN_WIDTH - 30)
    y = random.randint(0, SCREEN_HEIGHT - 30)
    enemy = Enemy(x, y)
    enemy_group.add(enemy)

# 町人の追加
for _ in range(3):
    x = random.randint(0, SCREEN_WIDTH - 20)
    y = random.randint(0, SCREEN_HEIGHT - 20)
    citizen = Citizen(x, y)
    citizen_group.add(citizen)

# プレイヤーの追加
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
player_group.add(player)

# ゲームループ
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 画面の更新
    background_group.draw(screen)
    block_group.draw(screen)
    enemy_group.draw(screen)
    citizen_group.draw(screen)
    player_group.draw(screen)

    # 画面の更新
    pygame.display.flip()

    # フレームレートの設定
    clock.tick(60)

# Pygameの終了
pygame.quit()