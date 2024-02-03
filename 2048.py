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

text1 = font.render('2', True, (0,0,0))
textRect1 = text1.get_rect(topleft=(115,110))
text2 = font.render('2', True, (0,0,0))
textRect2 = text2.get_rect(topleft=(230,110))
text3 = font.render('2', True, (0,0,0))
textRect3 = text3.get_rect(topleft=(345,110))
text4 = font.render('2', True, (0,0,0))
textRect4 = text4.get_rect(topleft=(460,110))

# text5 = font.render('2', True, (0,0,0))
# textRect5 = text5.get_rect(topleft=(115,230))
# text6 = font.render('2', True, (0,0,0))
# textRect6 = text6.get_rect(topleft=(235,110))
# text7 = font.render('2', True, (0,0,0))
# textRect7 = text7.get_rect(topleft=(110,110))
# text8 = font.render('2', True, (0,0,0))
# textRect8 = text8.get_rect(topleft=(110,110))

text9 = font.render('2', True, (0,0,0))
textRect9 = text9.get_rect(topleft=(115,110))
text10 = font.render('2', True, (0,0,0))
textRect10 = text10.get_rect(topleft=(230,110))
text11 = font.render('2', True, (0,0,0))
textRect11 = text11.get_rect(topleft=(345,110))
text12 = font.render('2', True, (0,0,0))
textRect12 = text12.get_rect(topleft=(460,110))


pygame.display.flip()

run = True
while run:
    
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    screen.blit(text4, textRect4)
    screen.blit(text9, textRect9)
    screen.blit(text10, textRect10)

    pygame.display.flip()
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

pygame.quit()