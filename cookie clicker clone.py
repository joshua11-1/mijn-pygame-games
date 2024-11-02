import pygame
from time import sleep

WINDOW = 600
BLACK = 0,0,0
BLUE = 0,0,255
SCORE = 0

pygame.init()
screen = pygame.display.set_mode([WINDOW] * 2)
clock = pygame.time.Clock()
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
pygame.display.set_caption('cookie clicker clone')

font = pygame.font.Font('freesansbold.ttf', 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill(BLUE)

    pygame.draw.circle(screen, 'red' ,player_pos, 40)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        SCORE = SCORE + 1
        pygame.draw.circle(screen, 'black' ,player_pos, 40)
        sleep(0.3)
        print(SCORE)

    text = font.render('Score: ' + str(SCORE), True, 'white')
    screen.blit(text, (40, 100))

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update
