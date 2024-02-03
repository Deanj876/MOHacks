import pygame

WIDTH, HEIGHT = 600,650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
color = (255,255,255)
screen.fill(color)
pygame.display.flip()
# pygame.draw.rect(screen, (200,200,200), [])

run = True
while run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

pygame.quit()