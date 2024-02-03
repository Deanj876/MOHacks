import pygame

WIDTH, HEIGHT = 1900,1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255,255,255))


run = True
while run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

pygame.quit()