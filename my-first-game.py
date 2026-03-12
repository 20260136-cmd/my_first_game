import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ULTRA Particle Playground")

clock = pygame.time.Clock()

particles = []


class Particle:

    def __init__(self, x, y, power=1):

        self.x = x
        self.y = y

        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(1, 6) * power

        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed

        self.life = random.randint(80, 150)
        self.max_life = self.life

        self.size = random.randint(2, 5)

        self.hue = random.randint(0, 360)

    def update(self, mx, my):

        dx = mx - self.x
        dy = my - self.y

        dist = math.hypot(dx, dy)

        if dist < 200:
            force = 0.05
            self.vx += dx * force / (dist + 1)
            self.vy += dy * force / (dist + 1)

        self.x += self.vx
        self.y += self.vy

        self.vy += 0.03

        self.vx += math.sin(self.life * 0.1) * 0.02

        self.life -= 1
        self.hue += 1

    def color(self):

        c = pygame.Color(0)
        c.hsva = (self.hue % 360, 80, 100, 100)
        return c

    def draw(self, surf):

        if self.life <= 0:
            return

        color = self.color()

        alpha = int(255 * (self.life / self.max_life))

        glow_size = self.size * 6
        glow = pygame.Surface((glow_size * 2, glow_size * 2), pygame.SRCALPHA)

        pygame.draw.circle(
            glow,
            (*color[:3], 40),
            (glow_size, glow_size),
            glow_size
        )

        surf.blit(glow, (self.x - glow_size, self.y - glow_size),
                  special_flags=pygame.BLEND_ADD)

        pygame.draw.circle(
            surf,
            color,
            (int(self.x), int(self.y)),
            self.size
        )

    def alive(self):
        return self.life > 0


def draw_background(surface, t):

    for y in range(HEIGHT):

        r = int(20 + 20 * math.sin(y * 0.02 + t))
        g = int(40 + 30 * math.sin(y * 0.01 + t))
        b = int(100 + 60 * math.sin(y * 0.015 + t))

        pygame.draw.line(surface, (r, g, b), (0, y), (WIDTH, y))


def explosion(x, y):

    for _ in range(120):
        particles.append(Particle(x, y, power=2))


running = True
time = 0

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 3:
                explosion(*pygame.mouse.get_pos())

    mouse = pygame.mouse.get_pos()
    buttons = pygame.mouse.get_pressed()

    if buttons[0]:
        for _ in range(12):
            particles.append(Particle(mouse[0], mouse[1]))

    time += 0.03

    draw_background(screen, time)

    for p in particles:
        p.update(mouse[0], mouse[1])
        p.draw(screen)

    particles = [p for p in particles if p.alive()]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()