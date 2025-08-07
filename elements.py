import pygame


pygame.init()


screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Simple Pygame Example")


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


font = pygame.font.Font(None, 36)
text = font.render("Hello, Pygame!", True, BLACK)


rect = pygame.Rect(200, 150, 200, 100)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)                
    pygame.draw.rect(screen, BLUE, rect) 
    screen.blit(text, (220, 100))     

    pygame.display.flip()            

pygame.quit()