import pygame
import random
import math
import colorsys

pygame.init()

# -------------------------
# SETTINGS
# -------------------------
WIDTH, HEIGHT = 900, 600
FPS = 60
GRAVITY = 0.05

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ultimate Particle Playground")

clock = pygame.time.Clock()

particles = []

# -------------------------
# COLOR UTIL
# -------------------------
def rainbow_color(t):
    r, g, b = colorsys.hsv_to_rgb(t % 1, 0.8, 1)
    return int(r*255), int(g*255), int(b*255)


# -------------------------
# PARTICLE
# -------------------------
class Particle:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        angle = random.uniform(0, math.tau)
        speed = random.uniform(2, 7)

        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed

        self.life = random.randint(60, 120)
        self.max_life = self.life

        self.size = random.randint(4, 8)

        self.color_offset = random.random()

    def update(self):

        self.x += self.vx
        self.y += self.vy

        self.vy += GRAVITY

        self.life -= 1

    def draw(self, surface, time):

        if self.life <= 0:
            return

        fade = self.life / self.max_life
        size = int(self.size * fade)

        color = rainbow_color(time + self.color_offset)

        # glow surface
        glow = pygame.Surface((size*6, size*6), pygame.SRCALPHA)

        pygame.draw.circle(
            glow,
            (*color, 120),
            (size*3, size*3),
            size*2
        )

        pygame.draw.circle(
            glow,
            (*color, 255),
            (size*3, size*3),
            size
        )

        surface.blit(
            glow,
            (self.x-size*3, self.y-size*3),
            special_flags=pygame.BLEND_ADD
        )

    def alive(self):
        return self.life > 0


# -------------------------
# BACKGROUND
# -------------------------
def draw_background(surface, t):

    for y in range(HEIGHT):

        r = int(20 + 10 * math.sin(y*0.01 + t))
        g = int(30 + 20 * math.sin(y*0.02 + t))
        b = int(60 + 30 * math.sin(y*0.015 + t))

        pygame.draw.line(surface, (r, g, b), (0, y), (WIDTH, y))


# -------------------------
# MAIN LOOP
# -------------------------
running = True
time = 0

while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse = pygame.mouse.get_pos()
    buttons = pygame.mouse.get_pressed()

    # particle spawn
    if buttons[0]:
        for _ in range(15):
            particles.append(Particle(mouse[0], mouse[1]))

    time += 0.01

    draw_background(screen, time)

    for p in particles:
        p.update()
        p.draw(screen, time)

    particles = [p for p in particles if p.alive()]

    pygame.display.flip()

pygame.quit()