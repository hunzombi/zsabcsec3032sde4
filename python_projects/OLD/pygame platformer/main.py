import pygame, sys
from settings import *
from tiles import tile
from level import Level

pygame.init()
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                level.world_shift = 20
            elif event.key == pygame.K_d:
                level.world_shift = -20
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                level.world_shift = 0
            elif event.key == pygame.K_d:
                level.world_shift = 0
    
    screen.fill("black")
    level.run()

    pygame.display.update()
    clock.tick(60)