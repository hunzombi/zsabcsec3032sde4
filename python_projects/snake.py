import pygame
import sys
import random

pygame.init()

# Basic Setup

screen = pygame.display.set_mode((600, 700))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 100)
game_surf = pygame.surface.Surface((600, 600))
hud_surf = pygame.surface.Surface((600, 100))
score = 0

# The map

map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# Classes

class Queue(object):
    def __init__(self):
        self.values = []
    
    def get_last(self):
        return self.values.pop()
    
    def get(self):
        return self.values
    
    def get_first(self):
        return self.values[0]
    
    def insert(self, val):
        if not self.values:
            self.values = [val]
        else:
            vals = self.values
            vals = vals[::-1]
            vals.append(val)
            vals = vals[::-1]
            self.values = vals


class Pixel(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self) -> None:
        map[self.y][self.x] = 1
        pygame.draw.rect(game_surf, "green", pygame.rect.Rect(self.x*30, self.y*30, 30, 30))
    
    def clear(self):
        map[self.y][self.x] = 0
        pygame.draw.rect(game_surf, "black", pygame.rect.Rect(self.x*30, self.y*30, 30, 30))


class Snake(object):
    def __init__(self):
        self.pixels = Queue()
        self.left = self.up = self.down = False
        self.right = True
        self.apple = False

        self.pixels.insert(Pixel(9, 9))
    
    # Moving with teleporting to the other side of the map if
    # touching the border of the map
    def move(self):
        global score

        self.apple = False
        first_pixel = self.pixels.get_first()

        if self.left:
            if first_pixel.x > 0:
                next_pixel = Pixel(first_pixel.x - 1, first_pixel.y)
            else:
                next_pixel = Pixel(19, first_pixel.y)
            self.pixels.insert(next_pixel)
            if map[next_pixel.y][next_pixel.x] == 2:
                self.apple = True
            
            elif map[next_pixel.y][next_pixel.x] == 1:
                start()

        
        if self.right:
            if first_pixel.x < 19:
                next_pixel = Pixel(first_pixel.x + 1, first_pixel.y)
            else:
                next_pixel = Pixel(0, first_pixel.y)
            self.pixels.insert(next_pixel)
            if map[next_pixel.y][next_pixel.x] == 2:
                self.apple = True
            
            elif map[next_pixel.y][next_pixel.x] == 1:
                start()

        
        if self.up:
            if first_pixel.y > 0:
                next_pixel = Pixel(first_pixel.x, first_pixel.y - 1)
            else:
                next_pixel = Pixel(first_pixel.x, 19)
            self.pixels.insert(next_pixel)
            if map[next_pixel.y][next_pixel.x] == 2:
                self.apple = True
            
            elif map[next_pixel.y][next_pixel.x] == 1:
                start()


        if self.down:
            if first_pixel.y < 19:
                next_pixel = Pixel(first_pixel.x, first_pixel.y + 1)
            else:
                next_pixel = Pixel(first_pixel.x, 0)
            self.pixels.insert(next_pixel)
            if map[next_pixel.y][next_pixel.x] == 2:
                self.apple = True
            
            elif map[next_pixel.y][next_pixel.x] == 1:
                start()

        if self.apple:
            score += 1
            make_apple()

        self.clear()
        if not self.apple:
            self.pixels.get_last()
    

    def clear(self):
        for pixel in self.pixels.get():
            pixel.clear()

    def draw(self):
        for pixel in self.pixels.get():
            pixel.draw()


# Creating apples

def make_apple():
    generated = False
    while not generated:
        x = random.randint(0, 19)
        y = random.randint(0, 19)
        if map[y][x] == 0:
            map[y][x] = 2
            generated = True


# Drawing the apples

def draw_map():
    for y, row in enumerate(map):
        for x, pixel in enumerate(row):
            if pixel == 2:
                pygame.draw.rect(game_surf, "red", pygame.rect.Rect(x*30, y*30, 30, 30))


# Showing the score

def show_score():
    text = font.render(str(score), True, "black")
    hud_surf.blit(text, (500, 20))


# Declaring the vaiables

player = Snake()

# Reset the game

def start():
    global map
    global player
    global score
    score = 0
    player = Snake()
    for y in range(20):
        for x in range(20):
            map[y][x] = 0
    make_apple()

# Setting up the game

start()

# Game Loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    for i in range(1):
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if not player.down:
                player.left = player.right = False
                player.up = True

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if not player.up:
                player.left = player.right = False
                player.down = True
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if not player.right:
                player.up = player.down = False
                player.left = True
            
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if not player.left:
                player.up = player.down = False
                player.right = True
    
    # Background Processes

    player.move()

    # Drawing the game to the game window

    screen.fill("black")
    game_surf.fill("black")
    hud_surf.fill("grey")
    show_score()
    player.draw()
    draw_map()
    screen.blit(hud_surf, (0, 0))
    screen.blit(game_surf, (0, 100))

    # Updating the screen

    pygame.display.flip()
    pygame.display.update()

    # Setting the tick

    clock.tick(10)
