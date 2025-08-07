import pygame
import sys


pygame.init()



screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Two Rectangles")


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()


speed = 5


running = True
while running:
    clock.tick(60)  # Limit to 60 FPS

  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += speed
    if keys[pygame.K_UP]:
        player_rect.y -= speed
    if keys[pygame.K_DOWN]:
        player_rect.y += speed

    
    screen.fill(WHITE)  
    pygame.draw.rect(screen, RED, player_rect)   
    pygame.draw.rect(screen, BLUE, enemy_rect)  

    
    pygame.display.flip()


pygame.quit()
sys.exit()