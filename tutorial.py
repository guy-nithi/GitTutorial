import pygame

WIDTH, HEIGHT = 1200, 700

def game():
    run = True
    clock = pygame.time.Clock()
    win = pygame.display.set_mode((WIDTH, HEIGHT))

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()
        
game()