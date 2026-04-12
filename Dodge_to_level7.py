import pygame
import base64
import io
import random  # (Warning 방지: 아래 MovingObject에서 사용함)
import sys     # (Warning 방지: sys.exit()에서 사용함)

# --- 1. 교수님이 주신 4개의 긴 문자열 ---
# (여기에 실제 데이터를 하나씩 복사해서 넣으세요)
SHEET_UP_B64    = "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"
SHEET_DOWN_B64  = "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"
SHEET_LEFT_B64  = "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"
SHEET_RIGHT_B64 = "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"
 


# 설정값
FRAME_W, FRAME_H = 17, 17
COLS = 4
FRAME_DELAY = 130
WIDTH, HEIGHT = 800, 600

# 색상 정의
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
RED, YELLOW, ORANGE = (220, 50, 50), (240, 200, 0), (255, 140, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doro's Adventure: Level 7")
clock = pygame.time.Clock()

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2. 유틸리티 함수
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def make_frames(b64_data, indices):
    try:
        sheet_bytes = base64.b64decode(b64_data)
        img = pygame.image.load(io.BytesIO(sheet_bytes)).convert_alpha()
        frames = []
        for i in indices:
            row, col = divmod(i, COLS)
            rect = pygame.Rect(col * FRAME_W, row * FRAME_H, FRAME_W, FRAME_H)
            frames.append(img.subsurface(rect))
        return frames
    except:
        s = pygame.Surface((FRAME_W, FRAME_H)); s.fill((50, 50, 200))
        return [s]

def draw_text(surf, text, x, y, size=30, color=WHITE, center=False):
    font = pygame.font.SysFont("malgungothic", size)
    if font.get_ascent() <= 0: font = pygame.font.SysFont(None, size)
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect()
    if center:
        text_rect.center = (x, y)
        surf.blit(text_surf, text_rect)
    else:
        surf.blit(text_surf, (x, y))

# 프레임 준비
UP_WALK    = make_frames(SHEET_UP_B64,    [2, 6, 10])
DOWN_WALK  = make_frames(SHEET_DOWN_B64,  [1, 5, 9])
LEFT_WALK  = make_frames(SHEET_LEFT_B64,  [0, 4, 8])
RIGHT_WALK = make_frames(SHEET_RIGHT_B64, [3, 7, 11])

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3. 클래스 정의
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH//2, HEIGHT//2, 40, 40)
        self.hp, self.level = 3, 1
        self.dash_count, self.dash_timer = 3, 0
        self.invincible_timer, self.speed = 0, 5
        self.current_frames = DOWN_WALK
        self.facing = 'down'
        self.is_moving = False
        self.frame_index = 0
        self.frame_timer = 0

    def move(self, keys):
        s = int(self.speed * 2.5) if self.dash_timer > 0 else self.speed
        self.is_moving = False
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= s; self.facing = 'left'; self.is_moving = True
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += s; self.facing = 'right'; self.is_moving = True
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= s; self.facing = 'up'; self.is_moving = True
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += s; self.facing = 'down'; self.is_moving = True
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

    def update_animation(self, dt):
        old_frames = self.current_frames
        if self.is_moving:
            if self.facing == 'up': self.current_frames = UP_WALK
            elif self.facing == 'down': self.current_frames = DOWN_WALK
            elif self.facing == 'left': self.current_frames = LEFT_WALK
            elif self.facing == 'right': self.current_frames = RIGHT_WALK
        else:
            self.current_frames = [self.current_frames[0]]
        if old_frames != self.current_frames:
            self.frame_index = 0; self.frame_timer = 0
        self.frame_timer += dt
        if self.frame_timer >= FRAME_DELAY:
            self.frame_index = (self.frame_index + 1) % len(self.current_frames)
            self.frame_timer = 0

    def draw(self, surface):
        if self.invincible_timer % 10 < 5:
            img = self.current_frames[self.frame_index % len(self.current_frames)]
            scaled = pygame.transform.scale(img, (self.rect.width, self.rect.height))
            surface.blit(scaled, self.rect)

class MovingObject:
    def __init__(self, size, color, speed_range, itype=None):
        self.rect = pygame.Rect(0, 0, size, size)
        self.color, self.type = color, itype
        side = random.randint(0, 3)
        speed = random.randint(*speed_range)
        if side == 0: self.rect.x, self.rect.y = random.randint(0, WIDTH-size), -size; self.vx, self.vy = 0, speed
        elif side == 1: self.rect.x, self.rect.y = random.randint(0, WIDTH-size), HEIGHT; self.vx, self.vy = 0, -speed
        elif side == 2: self.rect.x, self.rect.y = -size, random.randint(0, HEIGHT-size); self.vx, self.vy = speed, 0
        else: self.rect.x, self.rect.y = WIDTH, random.randint(0, HEIGHT-size); self.vx, self.vy = -speed, 0
    def update(self): self.rect.x += self.vx; self.rect.y += self.vy

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 4. 상태 화면 (Game Over / Victory)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def show_end_screen(title, color):
    while True:
        screen.fill(BLACK)
        draw_text(screen, title, WIDTH//2, HEIGHT//2 - 50, 60, color, True)
        draw_text(screen, "Press 'R' to Restart or 'Q' to Quit", WIDTH//2, HEIGHT//2 + 50, 30, WHITE, True)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: return True  # 재시작
                if event.key == pygame.K_q: pygame.quit(); sys.exit()

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 5. 메인 루프
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def main():
    try:
        bg = pygame.image.load("./assets/sprites/DORO.png").convert_alpha()
        bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
    except: bg = None

    p = Player()
    enemies, items = [], []
    spawn_timer, item_timer = 0, 0
    level_conf = [
        {"sp": (4,6), "n": 35}, {"sp": (5,7), "n": 25}, {"sp": (6,9), "n": 18},
        {"sp": (7,11), "n": 12}, {"sp": (8,12), "n": 8}, {"sp": (10,15), "n": 5}
    ]

    while True:
        dt = clock.tick(60)
        conf = level_conf[min(p.level-1, 5)]

        for e in pygame.event.get():
            if e.type == pygame.QUIT: pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN and e.key in [pygame.K_SPACE, pygame.K_LSHIFT]:
                if p.dash_count > 0 and p.dash_timer <= 0:
                    p.dash_count -= 1; p.dash_timer = 12

        keys = pygame.key.get_pressed()
        p.move(keys)
        p.update_animation(dt)
        if p.dash_timer > 0: p.dash_timer -= 1
        if p.invincible_timer > 0: p.invincible_timer -= 1

        spawn_timer += 1
        if spawn_timer >= conf["n"]:
            enemies.append(MovingObject(25, ORANGE, conf["sp"])); spawn_timer = 0
        
        item_timer += 1
        if item_timer > 400:
            itype = "heal" if random.random() > 0.8 else "lvup"
            items.append(MovingObject(20, RED if itype=="heal" else YELLOW, (5, 8), itype))
            item_timer = 0

        for en in enemies[:]:
            en.update()
            if not screen.get_rect().inflate(200, 200).contains(en.rect): enemies.remove(en)
            elif p.rect.colliderect(en.rect) and p.dash_timer <= 0 and p.invincible_timer <= 0:
                p.hp -= 1; p.invincible_timer = 60
                if p.hp <= 0:
                    if show_end_screen("GAME OVER", RED): main()

        for it in items[:]:
            it.update()
            if not screen.get_rect().inflate(200, 200).contains(it.rect): items.remove(it)
            elif p.rect.colliderect(it.rect):
                if it.type == "lvup": p.level += 1; p.dash_count = 3
                else: p.hp = min(3, p.hp + 1)
                items.remove(it)

        if bg: screen.blit(bg, (0,0))
        else: screen.fill((30, 30, 40))
        for it in items: pygame.draw.rect(screen, it.color, it.rect)
        for en in enemies: pygame.draw.rect(screen, en.color, en.rect)
        p.draw(screen)

        draw_text(screen, f"LV: {p.level}", 20, 20, 30, YELLOW)
        draw_text(screen, f"HP: {'♥' * p.hp}", 20, 55, 30, RED)
        draw_text(screen, f"DASH: {p.dash_count}", 20, 90, 25, WHITE)

        if p.level >= 7:
            if show_end_screen("VICTORY!", YELLOW): main()

        pygame.display.flip()

if __name__ == "__main__":
    main()