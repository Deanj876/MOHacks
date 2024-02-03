import pygame

pygame.init()
screen = pygame.display.set_mode((8200,6800))

run = True

while run:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
            
            
pygame.quit()