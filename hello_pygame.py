import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Pygame")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)  # 정사각형 색상

clock = pygame.time.Clock()
running = True

# 원 초기 위치
x, y = 400, 300
speed = 7
radius = 50

# 정사각형 초기 위치와 크기
square_size = 100
square_x, square_y = 200, 150

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += speed

    # 원 경계 처리
    x = max(radius, min(800 - radius, x))
    y = max(radius, min(600 - radius, y))

    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (x, y), radius)
    pygame.draw.rect(screen, RED, (square_x, square_y, square_size, square_size))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()