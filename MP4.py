
from graphics import *
import random

win = GraphWin('Animation', 600, 600, autoflush=False)


class Animated_Circle():
    def __init__(self):
        self. c= Circle(Point(300, 300), random.randint(5, 45))
        self.c.setFill(color_rgb(random.randint(0, 255),
                                 random.randint(0, 255),
                                 random.randint(0, 255)))
        self.dx= random.randint(-15, 15)
        self.dy= random.randint(-15, 15)
        self.c.draw(win)
        self.c.move(self.dx ,self.dy)



    def outside_x(self):
        center = self.c.getCenter()
        radius = self.c.getRadius()
        x, y = center.getX(), center.getY()
        if x + radius >= 600 or x - radius <= 0:
            return True
        else:
            return False

    def outside_y(self):
        center = self.c.getCenter()
        radius = self.c.getRadius()
        x, y = center.getX(), center.getY()
        if y + radius >= 600 or y - radius <= 0:
            return True
        else:
            return False

    def move(self):
        if not self.outside_y():
            if not self.outside_x():
                self.c.move(self.dx ,self.dy)

            else:
                self.dx =-self.dx
                self.c.move(self.dx ,self.dy)
        else:
            if not self.outside_x():
                self.dy =-self.dy
                self.c.move(self.dx ,self.dy)
            else:
                self.dy =-self.dy
                self.dx =-self.dx
                self.c.move(self.dx ,self.dy)


circles = []

for i in range(50):
    circles.append(Animated_Circle())

while True:
    for i in range(50):
        circles[i].move()
    update(30)