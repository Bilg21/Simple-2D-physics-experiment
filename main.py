import pygame
import random
import math
import time
from particle import Particle




bg_color = (255,255,255)
(width, height) = (300, 200)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Physics")
screen.fill(bg_color)

pygame.display.flip()

number_of_particles = 10
my_particles = []
for n in range(number_of_particles):
    size = random.randint(10, 20)
    x = random.randint(size, width-size)
    y = random.randint(size, height-size)
    
    particle = Particle((x,y), size)
    particle.speed = random.random()
    particle.angle = random.uniform(0, math.pi * 2)

    my_particles.append(particle)

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(144)
    screen.fill(bg_color)
    for particle in my_particles:
        particle.move()
        particle.bounce(width, height)
        particle.display(screen)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
