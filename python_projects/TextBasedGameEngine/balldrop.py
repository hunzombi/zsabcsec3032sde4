import pygame
import sys

pygame.init()

WIDTH = 600
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
main = pygame.surface.Surface((WIDTH, HEIGHT - 150))
ground = pygame.surface.Surface((WIDTH, 50))
menu = pygame.surface.Surface((WIDTH, 100))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 32)


class Ball(object):
    def __init__(self):
        self.rad = 15
        self.pos = [WIDTH // 2, 35]
        self.vel = [0, 0]
        self.aceleration = (0, 1)
        self.falling = False
        self.color = "red"
    
    def move(self):
        if self.falling:
            if self.pos[1] + self.rad >= HEIGHT - 150:
                if self.vel[1] >= -2 and self.vel[1] <= +2:
                    self.falling = False
                self.pos = [self.pos[0], HEIGHT - 150 - self.rad]
                self.vel = [self.vel[0] // 2, -self.vel[1] // 2]

            if self.falling:
                self.vel[0] += self.aceleration[0]
                self.vel[1] += self.aceleration[1]
            
                self.pos[0] += self.vel[0]
                self.pos[1] += self.vel[1]
    
    def update(self, surf):
        self.move()
        pygame.draw.circle(surf, self.color, self.pos, self.rad)


class Button(object):
    def __init__(self):
        self.x = WIDTH // 2
        self.y = 25
        self.w = 100
        self.h = 50
        self.rect = pygame.rect.Rect(self.x, self.y, self.w, self.h)
        self.text = font.render("Pause", True, "black")
    
    def update(self, surf):
        pygame.draw.rect(surf, "white", self.rect)
        surf.blit(self.text, (self.x + 10, self.y + 10))


myBall = Ball()
myButton = Button()

while True:

    button_pressed = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                button_pressed = True
            
            elif event.key == pygame.K_q:
                myBall.pos = [WIDTH // 2, 20]
                myBall.falling = True
            
            elif event.key == pygame.K_r:
                myBall.pos = [WIDTH // 2, 20]
                myBall.vel = [0, 0]
                myBall.falling = True

    if button_pressed:
        myBall.falling = not myBall.falling
        if not myBall.falling:
            myBall.vel = [0, 0]
    
    screen.fill("black")
    main.fill("cyan")
    ground.fill("green")
    menu.fill("black")
    
    myBall.update(main)
    myButton.update(menu)

    screen.blit(main, (0, 0))
    screen.blit(ground, (0, HEIGHT - 150))
    screen.blit(menu, (0, HEIGHT - 100))

    pygame.display.flip()
    pygame.display.update()
    clock.tick(30)
