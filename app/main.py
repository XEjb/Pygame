import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((618, 359))
pygame.display.set_caption('Nauty Game')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('images/fon.jpg')
walk_left = [
    pygame.image.load('images/left.png'),
    pygame.image.load('images/runleft.png'),
]
walk_right = [
    pygame.image.load('images/right.png'),
    pygame.image.load('images/runright.png'),
]

player_anim_count = 0
bg_x = 0

run = True
while run:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 618, 0))
    screen.blit(walk_right[player_anim_count], (300, 250))

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    bg_x -= 2
    if bg_x == -618:
        bg_x = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    clock.tick(20)
