from dis import dis
import pygame
import math
import sys

pygame.init()

# CONSTANTS

WIDTH = HEIGHT = 600
BACKGROUND = "black"
ENEMY_COLOR = "blue"


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Funcions

    # Input 2 touples or list like the followings: (x, y) OR [x, y]
def dist(coords1, coords2):
    return round(math.sqrt((coords2[1]-coords1[1])**2+(coords2[0]-coords1[0])**2) + 10) # +10 for rad

def slope(x1, x2, y1, y2):
    m = (y2 - y1) / (x2 - x1)
    return m

# Classes

class Circle(object):
    def __init__(self):
        self.rad = 10
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.color = ENEMY_COLOR
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.rad)
    
    def move(self):
        
        # Calculate using slope and opposite of the line


        if self.x + self.rad > WIDTH:
            self.x = WIDTH - self.rad

        if self.x - self.rad < 0:
            self.x = self.rad

        if self.y + self.rad > HEIGHT:
            self.y = HEIGHT - self.rad
        
        if self.y - self.rad < 0:
            self.y = self.rad
    

# Setup

enemy = Circle()
mouse_coords = (0, 0)

# Game Loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    mouse_coords = pygame.mouse.get_pos()
    distance = dist((enemy.x, enemy.y), mouse_coords)

    if distance <= 20:

        
        m = slope(enemy.x, mouse_coords[0], enemy.y, mouse_coords[1])
        m = -m
        unit = 2
        enemy.x += enemy.x - round(unit)
        enemy.y += enemy.y - round(m * unit)


        enemy.move()
    
    # Drawing on the screen

    screen.fill("black")

    enemy.draw(screen)
    
    pygame.display.flip()
    pygame.display.update()

    clock.tick(60)
