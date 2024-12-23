import pygame
from spritesheet import Spritesheet

################################# LOAD UP A BASIC WINDOW #################################
pygame.init()
DISPLAY_W, DISPLAY_H = 480, 270
canvas = pygame.Surface((DISPLAY_W,DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
running = True
###########################################################################################

my_spritesheet = Spritesheet('trainer_sheet.png')
trainer = [my_spritesheet.parse_sprite('trainer1.png'), my_spritesheet.parse_sprite('trainer2.png'),my_spritesheet.parse_sprite('trainer3.png'),
           my_spritesheet.parse_sprite('trainer4.png'),my_spritesheet.parse_sprite('trainer5.png')]
# f_trainer = [my_spritesheet.parse_sprite('f_trainer1.png'), my_spritesheet.parse_sprite('f_trainer2.png'),my_spritesheet.parse_sprite('f_trainer3.png'),
#            my_spritesheet.parse_sprite('f_trainer4.png'),my_spritesheet.parse_sprite('f_trainer5.png')]

# Animation variables
index = 0
frame_counter = 0
update_frames = 0  # Tracks how many frames to animate

# Main loop
while running:
    ################################# CHECK PLAYER INPUT #################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                update_frames = 5  # Set to animate for 5 frames

    ################################# UPDATE SPRITE #################################
    if update_frames > 0:
        frame_counter += 1
        if frame_counter >= 5:  # Adjust to control the speed of animation
            index = (index + 1) % len(trainer)
            frame_counter = 0
            update_frames -= 1  # Decrease the frame counter

    ################################# UPDATE WINDOW AND DISPLAY #################################
    canvas.fill((255, 255, 255))
    canvas.blit(trainer[index], (0, DISPLAY_H - 128))
    window.blit(canvas, (0, 0))
    pygame.display.update()

    # Cap frame rate
    pygame.time.Clock().tick(60)










