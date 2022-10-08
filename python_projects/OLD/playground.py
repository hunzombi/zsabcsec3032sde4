from random import randint, choice
import turtle
from os import system
from time import sleep


system("cls")
ts = turtle.Screen()
ts.tracer(0)
run = True
t1 = turtle.Turtle()
t1.speed(0)
t1.hideturtle()
t1.pu()
t1.goto(-110, 250)
t1.pd()

def draw_line():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(300, -300)
    t.pendown()
    t.pensize(5)
    t.goto(300, 300)

def write_text(text):
    t1.clear()
    t1.write(text ,font=["fantasy", 30])


def check_win(array):
    global run
    global ts
    ts.update()
    for i in array:
        if i.x >= 300 and run:
            print("The Winner Is {}".format(i.color))
            t1.pu()
            t1.goto(-200, 250)
            t1.pd()
            t1.color(i.color)
            write_text("The Winner Is {}".format(i.color))
            run = False


class Tur():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.t = turtle.Turtle()
    def start(self):
        self.t.speed(0)
        self.t.pensize(3)
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()
        self.t.color(self.color)
    def go(self):
        self.x += randint(7, 30)
        self.t.goto(self.x, self.y)
        self.t.color(self.color)


# Running The Functions
arr = [Tur(-340, 0, "Green"), Tur(-340, 40, "Red"), Tur(-340, -40, "Brown"), Tur(-340, 80, "Gray"), Tur(-340, -80, "Cyan"), Tur(-340, -120, "Magenta"), Tur(-340, 120, "Orange"), Tur(-340, -160, "Blue"), Tur(-340, 160, "Purple"), Tur(-340, -200, "Goldenrod1"), Tur(-340, 200, "Chartreuse"), Tur(-340, -240, "Aquamarine4"), Tur(-340, -280, "IndianRed"), Tur(-340, -320, "OrangeRed")]
draw_line()
write_text("Turtle Race")

for i in arr:
    i.start()

while run:
    sleep(0.1)
    for i in arr:
        i.go()
    ts.update()
    check_win(arr)

turtle.done()