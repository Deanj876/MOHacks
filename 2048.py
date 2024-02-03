import pygame

WIDTH, HEIGHT = 600,650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
color = (255,255,255)
screen.fill(color)
pygame.draw.rect(screen, (100,100,100), [50,50,500,500])
pygame.draw.rect(screen, (200,200,200), [70,70,110,110])
pygame.draw.rect(screen, (200,200,200), [185,70,110,110])
pygame.draw.rect(screen, (200,200,200), [300,70,110,110])
pygame.draw.rect(screen, (200,200,200), [415,70,110,110])

pygame.draw.rect(screen, (200,200,200), [70,185,110,110])
pygame.draw.rect(screen, (200,200,200), [185,185,110,110])
pygame.draw.rect(screen, (200,200,200), [300,185,110,110])
pygame.draw.rect(screen, (200,200,200), [415,185,110,110])

pygame.draw.rect(screen, (200,200,200), [70,300,110,110])
pygame.draw.rect(screen, (200,200,200), [185,300,110,110])
pygame.draw.rect(screen, (200,200,200), [300,300,110,110])
pygame.draw.rect(screen, (200,200,200), [415,300,110,110])

pygame.draw.rect(screen, (200,200,200), [70,415,110,110])
pygame.draw.rect(screen, (200,200,200), [185,415,110,110])
pygame.draw.rect(screen, (200,200,200), [300,415,110,110])
pygame.draw.rect(screen, (200,200,200), [415,415,110,110])

pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render("1", True, (0,0,0))
textRect = text.get_rect()

pygame.display.flip()

run = True
while run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

pygame.quit()