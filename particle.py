import pygame
import math

gravity = (0, 0.002)
drag = 0.999
elasticity = 0.75

def addVectors(v1, v2):
    (angle1, length1) = v1
    (angle2, length2) = v2
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2
    
    angle = 0.5 * math.pi - math.atan2(y, x)
    length  = math.hypot(x, y)

    return (angle, length)

class Particle:
    def __init__(self, coord, size):
        (x,y) = coord
        self.x = x
        self.y = y
        self.size = size
        self.color = (0,0,255)
        self.thickness = 1
        self.angle = 0
        self.speed = 2

    def move(self):
        self.speed *= (1 - self.size/ 10000.0)
        (self.angle, self.speed) = addVectors((self.angle, self.speed), gravity)
        self.x += math.sin(self.angle) * self.speed
        self.y += math.cos(self.angle) * self.speed
    
    def bounce(self, width, height):
        if self.x > width - self.size:
            self.x = 2 * (width - self.size) - self.x
            self.angle = -self.angle
        elif self.x < self.size:
            self.x = 2 * self.size - self.x
            self.angle = -self.angle

        if self.y > height - self.size:
            self.y = 2 * (height - self.size) - self.y
            self.angle = math.pi - self.angle
        elif self.y < self.size:
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle

    def display(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size, self.thickness)