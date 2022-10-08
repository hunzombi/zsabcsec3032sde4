import os
import time

class Rect(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

class Drawer(object):
    def __init__(self, parent):
        self.parent = parent
    
    def rect(self, rect, char):
        pixels = self.parent.pixels
        for y in range(rect.h):
            for x in range(rect.w):
                if y + rect.y > self.parent.H - 1 or rect.y + y < 0:
                    continue
                if x + rect.x > self.parent.W - 1 or rect.x + x < 0:
                    continue
                pixels[y + rect.y][x + rect.x] = char


class Screen(object):
    def __init__(self, W, H):
        self.W = W
        self.H = H
        self.pixels = []
        self.draw = Drawer(self)
        for i in range(self.H):
            new_row = []
            for j in range(self.W):
                new_row.append("-")
            self.pixels.append(new_row)
    
    def update(self):
        os.system("cls")
        for row in self.pixels:
            for pixel in row:
                print(pixel, end="")
            print("")
    
    def clean(self):
        for i in range(self.H):
            for j in range(self.W):
                self.pixels[i][j] = "-"


#Trying to make a bouncing rect
class Myrect(object):
    def __init__(self):
        self.x = 75
        self.y = 18
        self.w = 10
        self.h = 4
        self.x_vel = 5
        self.rect = Rect(self.x, self.y, self.w, self.h)
    
    def move(self):
        self.x += self.x_vel
        if self.x + self.w >= 150 or self.x < 0:
            self.x_vel = -self.x_vel
        self.rect.x = self.x


screen = Screen(150, 40)
myrect = Myrect()
while True:
    screen.clean()
    myrect.move()
    screen.draw.rect(myrect.rect, "%")
    screen.update()
    time.sleep(0.5)
