import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Pygame")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()
running = True

# 원의 초기 위치
x = 400
y = 300
speed = 7

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 받기
    keys = pygame.key.get_pressed()

    # 방향키 + WASD 이동
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += speed

    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (x, y), 50)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()