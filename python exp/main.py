import pygame
import button

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('First Game')

start_img = pygame.image.load('assets/start_btn.png').convert_alpha()
exit_img = pygame.image.load('assets/exit_btn.png').convert_alpha()

start_button = button.Button(100, 300, start_img, 0.8)
exit_button = button.Button(450, 300, exit_img, 0.8)
player = pygame.Rect((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 50, 50))

run = True
while run:

    screen.fill((202, 228, 241))

    if start_button.draw(screen):
        print('Start')

    if exit_button.draw(screen):
        run = False

    pygame.draw.rect(screen, (255, 0, 0), player)

    #keys things 
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()