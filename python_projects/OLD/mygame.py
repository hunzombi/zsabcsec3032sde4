from ast import PyCF_ONLY_AST
from this import s
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((600, 600))
Clock = pygame.time.Clock()

player = pygame.rect.Rect(300, 300, 50, 50)
player.center = (300, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: 
                player.y -= 10
            if event.key == pygame.K_s:
                player.y += 10
            if event.key == pygame.K_a:
                player.x -= 10
            if event.key == pygame.K_d:
                player.x += 10
    
    screen.fill("black")
    pygame.draw.circle(screen, "blue", player.center, 50)

    pygame.display.flip()
    pygame.display.update()
    Clock.tick(60)