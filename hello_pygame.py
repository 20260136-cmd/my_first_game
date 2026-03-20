import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("원과 정사각형 이동")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)   # 원 색상
RED = (255, 0, 0)    # 정사각형 색상

clock = pygame.time.Clock()
running = True

# 원 초기 위치
circle_x = 400
circle_y = 300
circle_radius = 50
circle_speed = 7

# 정사각형 초기 위치와 크기
square_x = 200
square_y = 150
square_size = 100
square_speed = 7

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # 🔵 원 이동 (방향키)
    if keys[pygame.K_LEFT]:
        circle_x -= circle_speed
    if keys[pygame.K_RIGHT]:
        circle_x += circle_speed
    if keys[pygame.K_UP]:
        circle_y -= circle_speed
    if keys[pygame.K_DOWN]:
        circle_y += circle_speed

    # 🔴 정사각형 이동 (WASD)
    if keys[pygame.K_a]:
        square_x -= square_speed
    if keys[pygame.K_d]:
        square_x += square_speed
    if keys[pygame.K_w]:
        square_y -= square_speed
    if keys[pygame.K_s]:
        square_y += square_speed

    # 🔒 원 경계 처리
    if circle_x < circle_radius:
        circle_x = circle_radius
    if circle_x > 800 - circle_radius:
        circle_x = 800 - circle_radius
    if circle_y < circle_radius:
        circle_y = circle_radius
    if circle_y > 600 - circle_radius:
        circle_y = 600 - circle_radius

    # 🔒 정사각형 경계 처리
    if square_x < 0:
        square_x = 0
    if square_x > 800 - square_size:
        square_x = 800 - square_size
    if square_y < 0:
        square_y = 0
    if square_y > 600 - square_size:
        square_y = 600 - square_size

    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (circle_x, circle_y), circle_radius)
    pygame.draw.rect(screen, RED, (square_x, square_y, square_size, square_size))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()