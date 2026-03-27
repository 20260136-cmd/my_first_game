import pygame
import sys
import math
from sprites import load_sprite

pygame.init()

# 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Collision: Circle + AABB + OBB")
clock = pygame.time.Clock()

# 색상
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# 이미지 로드 및 크기 조정
def scale_image(image, target_width, target_height):
    orig_width, orig_height = image.get_size()
    scale_ratio = min(target_width / orig_width, target_height / orig_height)
    new_width = int(orig_width * scale_ratio)
    new_height = int(orig_height * scale_ratio)
    return pygame.transform.smoothscale(image, (new_width, new_height))

player_img = load_sprite("adventurer")
center_img = load_sprite("stone")
player_img = scale_image(player_img, 80, 80)
center_img = scale_image(center_img, 80, 80)

# Rect 설정
player_rect = pygame.Rect(100, 100, 80, 80)
center_rect = pygame.Rect(WIDTH//2 - 40, HEIGHT//2 - 40, 80, 80)

speed = 4
rotation_angle = 0
rotation_speed = 0.5

# --- 수학 및 충돌 함수 ---

def rotate_point(point, angle, origin):
    ox, oy = origin
    px, py = point
    radians = math.radians(-angle) 
    qx = ox + math.cos(radians) * (px - ox) - math.sin(radians) * (py - oy)
    qy = oy + math.sin(radians) * (px - ox) + math.cos(radians) * (py - oy)
    return qx, qy

def get_rotated_vertices(rect, angle):
    center = rect.center
    corners = [rect.topleft, rect.topright, rect.bottomright, rect.bottomleft]
    return [rotate_point(p, angle, center) for p in corners]

def project_polygon(vertices, axis):
    dots = [v[0] * axis[0] + v[1] * axis[1] for v in vertices]
    return min(dots), max(dots)

def overlap(proj1, proj2):
    return not (proj1[1] < proj2[0] or proj2[1] < proj1[0])

def SAT_collision(rect1, angle1, rect2, angle2):
    verts1 = get_rotated_vertices(rect1, angle1)
    verts2 = get_rotated_vertices(rect2, angle2)
    axes = []
    for i in range(4):
        for verts in [verts1, verts2]:
            p1, p2 = verts[i], verts[(i + 1) % 4]
            edge = (p2[0] - p1[0], p2[1] - p1[1])
            axes.append((-edge[1], edge[0]))
    for axis in axes:
        mag = math.hypot(*axis)
        if mag == 0: continue
        norm_axis = (axis[0]/mag, axis[1]/mag)
        if not overlap(project_polygon(verts1, norm_axis), project_polygon(verts2, norm_axis)):
            return False
    return True

# --- 메인 루프 ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]: rotation_speed += 0.05
    if keys[pygame.K_LEFT]:  player_rect.x -= speed
    if keys[pygame.K_RIGHT]: player_rect.x += speed
    if keys[pygame.K_UP]:    player_rect.y -= speed
    if keys[pygame.K_DOWN]:  player_rect.y += speed

    rotation_angle += rotation_speed
    
    # [1] 원형 충돌 계산
    p_radius = player_rect.width // 2
    c_radius = center_rect.width // 2
    dist = math.hypot(player_rect.centerx - center_rect.centerx, player_rect.centery - center_rect.centery)
    collision_circle = dist < (p_radius + c_radius)

    # [2] AABB 충돌 계산
    collision_AABB = player_rect.colliderect(center_rect)

    # [3] OBB 충돌 계산
    collision_OBB = SAT_collision(player_rect, rotation_angle, center_rect, rotation_angle)

    screen.fill(BLACK)

    # 이미지 회전 및 그리기
    rot_p_img = pygame.transform.rotate(player_img, rotation_angle)
    rot_p_rect = rot_p_img.get_rect(center=player_rect.center)
    rot_c_img = pygame.transform.rotate(center_img, rotation_angle)
    rot_c_rect = rot_c_img.get_rect(center=center_rect.center)

    screen.blit(rot_p_img, rot_p_rect.topleft)
    screen.blit(rot_c_img, rot_c_rect.topleft)

    # --- 디버그용 도형 그리기 ---
    
    # 🔵 파란 원 (Circle)
    pygame.draw.circle(screen, BLUE, player_rect.center, p_radius, 2)
    pygame.draw.circle(screen, BLUE, center_rect.center, c_radius, 2)

    # 🔴 빨간 사각형 (AABB)
    pygame.draw.rect(screen, RED, player_rect, 1)
    pygame.draw.rect(screen, RED, center_rect, 1)
    
    # 🟢 초록 사각형 (OBB - 실제 SAT 판정선)
    p_verts = get_rotated_vertices(player_rect, rotation_angle)
    c_verts = get_rotated_vertices(center_rect, rotation_angle)
    pygame.draw.polygon(screen, GREEN, p_verts, 2)
    pygame.draw.polygon(screen, GREEN, c_verts, 2)

    # UI 텍스트
    font = pygame.font.SysFont("Arial", 20)
    res = [("Circle", collision_circle, BLUE), ("AABB", collision_AABB, RED), ("OBB", collision_OBB, GREEN)]
    for i, (name, hit, col) in enumerate(res):
        text = font.render(f"{name}: {'HIT' if hit else 'NO'}", True, col)
        screen.blit(text, (10, 10 + i * 25))

    pygame.display.flip()
    clock.tick(60)