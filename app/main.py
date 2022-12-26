import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption('Nauty Game')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)


square = pygame.Surface((50, 170))
square.fill('Blue')

myfont = pygame.font.Font('fonts/Sevillana-Regular.ttf', 40)
text_surface = myfont.render('Nauty', True, 'Red')


player = pygame.image.load('images/icon.png')

run = True
while run:

    pygame.draw.circle(screen, 'Red', (10, 7), 5)
    screen.blit(square, (10, 0))
    screen.blit(text_surface, (300, 100))
    screen.blit(player, (100, 50))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
