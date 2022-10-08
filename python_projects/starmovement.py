


"""
 This script is Made By "hunzombi" or my real name "Finta Zsombor" let's the camera move in an infinite 2d space, it's not perfect as it does
 not save the stars behind you it can be made by generating more stars and set the lower limit to -WIDTH/-HEIGHT and the upper limit to
 WIDTH * 2/HEIGHT * 2. It does not move the camera instead it moves the background(only the stars) it is a common technique in game developement
 Controls:
    W - UP
    S - DOWN
    A - LEFT
    D - RIGHT
    T - EXIT THE PROGRAM
"""



import random
import pygame
from sys import exit

pygame.init()

class Background():

    class Star():
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.rad = 1
            self.color = (255, 255, 255)
            self.up = False
            self.down = False
            self.left = False
            self.right = False

        def draw(self, win):
            pygame.draw.circle(win, self.color, (self.x, self.y), self.rad)
        
        def check_end(self, w, h):
            if self.x + self.rad > w:
                self.x = self.rad
                self.y = random.randint(10, h - 10)
            if self.x - self.rad < 0:
                self.x = w - self.rad
                self.y = random.randint(10, h - 10)
            if self.y + self.rad > h:
                self.y = self.rad
                self.x = random.randint(10, w - 10)
            if self.y - self.rad < 0:
                self.y = h - self.rad
                self.x = random.randint(10, w - 10)
        
        def move(self):
            if self.up:
                self.y += 10
            if self.down:
                self.y -= 10
            if self.left:
                self.x += 10
            if self.right:
                self.x -= 10
        
        def update(self, win, w, h):
            self.move()
            self.check_end(w, h)
            self.draw(win)
    
    def __init__(self):
        self.WIDTH = 1920
        self.HEIGHT = 1080
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.stars = []
        self.bgcolor = (0, 0, 0)
    
    def setup(self):
        for i in range(225):
            self.stars.append(self.Star(random.randint(10, self.WIDTH - 10), random.randint(10, self.HEIGHT - 10)))

    def update(self):
        self.screen.fill(self.bgcolor)

        for star in self.stars:
            star.update(self.screen, self.WIDTH, self.HEIGHT)
    
    def EventHandler(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w:
                    for star in self.stars:
                        star.up = True
                
                if event.key == pygame.K_s:
                    for star in self.stars:
                        star.down = True
                
                if event.key == pygame.K_a:
                    for star in self.stars:
                        star.left = True
                
                if event.key == pygame.K_d:
                    for star in self.stars:
                        star.right = True
                
                if event.key == pygame.K_t:
                    pygame.quit()
                    exit()
            
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_w:
                    for star in self.stars:
                        star.up = False
                
                if event.key == pygame.K_s:
                    for star in self.stars:
                        star.down = False
                
                if event.key == pygame.K_a:
                    for star in self.stars:
                        star.left = False

                if event.key == pygame.K_d:
                    for star in self.stars:
                        star.right = False

    def run(self):
        self.setup()
        
        while True:
            self.EventHandler()
            self.update()
            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(70)


if __name__ == '__main__':
    game = Background()
    game.run()