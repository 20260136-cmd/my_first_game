import pygame
import sys
import random

# 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("원과 정사각형 이동 및 색상 변화")

WHITE = (255, 255, 255)

clock = pygame.time.Clock()
running = True

# 🔵 원 초기 설정
circle_x, circle_y = 400, 300
circle_radius = 50
circle_speed = 7
circle_color = (0, 0, 255)

# 🔴 정사각형 초기 설정
square_x, square_y = 200, 150
square_size = 100
square_speed = 7
square_color = (255, 0, 0)

# 랜덤 색상 함수
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 🔹 키 누를 때 즉시 색상 변경
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                circle_color = random_color()
            if event.key in [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]:
                square_color = random_color()

    # 🔵 원 이동 (방향키)
    keys = pygame.key.get_pressed()
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
    circle_x = max(circle_radius, min(800 - circle_radius, circle_x))
    circle_y = max(circle_radius, min(600 - circle_radius, circle_y))

    # 🔒 정사각형 경계 처리
    square_x = max(0, min(800 - square_size, square_x))
    square_y = max(0, min(600 - square_size, square_y))

    # 화면 업데이트
    screen.fill(WHITE)
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)
    pygame.draw.rect(screen, square_color, (square_x, square_y, square_size, square_size))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()