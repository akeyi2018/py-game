import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Text Outline Effect")

# Define a font
font = pygame.font.Font(None, 64)

# Render the text
text_color = (255, 255, 255)
outline_color = (0, 0, 255)
text_surface = font.render("Outline Text", True, text_color)

# Create the outline
outline_offset = 2  # アウトラインの幅
text_rect = text_surface.get_rect(center=(400, 300))  # テキストの中心座標

# 描画ループでアウトラインを描画
for x_offset in range(-outline_offset, outline_offset + 1):
    for y_offset in range(-outline_offset, outline_offset + 1):
        if x_offset == 0 and y_offset == 0:
            continue  # 中心のテキストはスキップ
        outline_pos = (text_rect.x + x_offset, text_rect.y + y_offset)
        outline_surface = font.render("New Text", True, outline_color)
        screen.blit(outline_surface, outline_pos)

# Render the main text on top
screen.blit(text_surface, text_rect.topleft)

# Update the display
pygame.display.flip()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
