import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("원과 정사각형 이동 및 색상 변화 + Shift 속도")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)   # 초기 원 색상
RED = (255, 0, 0)    # 초기 정사각형 색상

clock = pygame.time.Clock()
running = True

# 원 초기 위치
circle_x = 400
circle_y = 300
circle_radius = 50
circle_speed = 7
circle_color = BLUE

# 정사각형 초기 위치와 크기
square_x = 200
square_y = 150
square_size = 100
square_speed = 7
square_color = RED

def random_color():
    """0~255 범위의 랜덤 RGB 색상 생성"""
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # 🔹 Shift 키 속도 적용
    current_circle_speed = circle_speed * 2 if keys[pygame.K_RSHIFT] else circle_speed
    current_square_speed = square_speed * 2 if keys[pygame.K_LSHIFT] else square_speed

    # 🔵 원 이동 (방향키)
    moved_circle = False
    if keys[pygame.K_LEFT]:
        circle_x -= current_circle_speed
        moved_circle = True
    if keys[pygame.K_RIGHT]:
        circle_x += current_circle_speed
        moved_circle = True
    if keys[pygame.K_UP]:
        circle_y -= current_circle_speed
        moved_circle = True
    if keys[pygame.K_DOWN]:
        circle_y += current_circle_speed
        moved_circle = True

    # 🔴 정사각형 이동 (WASD)
    moved_square = False
    if keys[pygame.K_a]:
        square_x -= current_square_speed
        moved_square = True
    if keys[pygame.K_d]:
        square_x += current_square_speed
        moved_square = True
    if keys[pygame.K_w]:
        square_y -= current_square_speed
        moved_square = True
    if keys[pygame.K_s]:
        square_y += current_square_speed
        moved_square = True

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

    # 🔹 색상 변경
    if moved_circle:
        circle_color = random_color()
    if moved_square:
        square_color = random_color()

    screen.fill(WHITE)
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)
    pygame.draw.rect(screen, square_color, (square_x, square_y, square_size, square_size))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

