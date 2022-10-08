import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("runner")
clock = pygame.time.Clock()
mfont = pygame.font.Font(None, 50)

ground = pygame.Surface((800, 100))
ground.fill("green")

enemy_surface = pygame.Surface((50, 50))
enemy_surface.fill("red")
enemy_rect = enemy_surface.get_rect(midbottom=(625, 300))

player_surf = pygame.Surface((50, 100))
player_surf.fill("gray")
player_rect = player_surf.get_rect(midbottom=(80, 300))

enemy_x = 600
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.fill("blue")
    
    screen.blit(ground, (0, 300))
    enemy_rect.right -= 4
    if enemy_rect.right <= 0:
        enemy_rect.right = 850

    screen.blit(enemy_surface, enemy_rect)
    screen.blit(player_surf, player_rect)

    if bool(player_rect.colliderect(enemy_rect)):
        print("collision")

    pygame.display.update()
    clock.tick(60)