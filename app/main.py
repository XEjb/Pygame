import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption('Nauty Game')
# icon = pygame.image.load('images/icon.png')
# pygame.display.set_icon(icon)

run = True
while run:

    # screen.fill((252, 152, 3))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                screen.fill((140, 3, 252))
