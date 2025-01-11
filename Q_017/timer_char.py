import pygame, sys
from pygame.locals import *

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 500

pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

font = pygame.font.Font("../battle/Meiryo.ttf", 36)

def display_text_animation(string):
    text = ''
    for i in range(len(string)):
        DISPLAYSURF.fill(WHITE)
        text += string[i]
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (0, 10)  # 指定したy座標で表示
        DISPLAYSURF.blit(text_surface, text_rect.topleft)
        pygame.display.update()
        pygame.time.wait(30)

def main():
    y_position = WINDOW_HEIGHT / 2  # 最初のメッセージの開始位置

    # メッセージを順番に表示
    display_text_animation('10ダメージを与えました。敵を倒しました。\n10ダメージを与えました。反撃を受けました\n1000ダメージを与えました。敵を倒しました。')
    # y_position += 50  # 次のメッセージは少し下に表示
    # display_text_animation('10ダメージを与えました。反撃を受けました', y_position)
    # y_position += 50  # 次のメッセージはさらに下に表示
    # display_text_animation('1000ダメージを与えました。敵を倒しました。', y_position)

    # イベントループ
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

main()

