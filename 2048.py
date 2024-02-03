WIDTH, HEIGHT = 8200,6800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

run = True
while run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

pygame.quit()
