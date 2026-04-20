import pygame
import base64
import io
import random  # (Warning 방지: 아래 MovingObject에서 사용함)
import sys     # (Warning 방지: sys.exit()에서 사용함)
import math
 
SHEET_UP_B64    = "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"
SHEET_DOWN_B64  = "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"
SHEET_LEFT_B64  = "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"
SHEET_RIGHT_B64 = "iVBORw0KGgoAAAANSUhEUgAAAEQAAAA0CAYAAAAzMZ5zAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAWvSURBVGhD7ZpPSBtZHMe/XRbBRZOUUpNahIi2dKWXWjHBQ0GyVMSD1cKWXjyV9by6dPfkob10F6Is9JLioXhZu4f6B0SwuIKHbSoqPa0gXRAkmBzEmAo9uofkN3nzy+/NvFnH3UPnA4KZ994n837vzST5MkBAgBMX+AEASA+nTtXX469XxX4m+OHyw0G4uURxejh1mmwPAwCyH45tbVygQ31jyWXi8cMBoQiqiztqhDQ42R5GNFI9XihWT4ZLODoHPHj8cMDBo3N8Ue1ShQ8GgGikWlkTJAc8evxwQOPROcSCZD8coy3Vh8sdCbSl+qzjXOpENAJr/OWOhO1/U49TP6c2jtpXnRe/HUAqiLp9fvh1GahsL7UwpoSuRPDdT78hdCVi+9+UQpEfqeLUJtGW6rPG0LwgXHI1BeE3IAC42ZMAUF5xU5z6OrWp3OxJoFC0T55e0zmZQO8njeHzrSkIADwauQsAePHsIVBZaQCYnlmx9XOC+r549hD723vY396zfKae6ZkV9NzvQ8/9PrSlyn/02tQB5f1oHnQeNE8VsSDTMysoHVSXpXRQRGp3D6/uXLf1k6CKv7pzHandPZQOimjpjKOlM17j4atDSA7C1KGi80hFrSkIXVPTMytIvH2P1O4ehj6WRQ2XzK7/sccjeBOPAwCGPpYnoHrexOMYezzCRtnxw0HQeZMn8fa9VQzXewiUTiSaa4xg9doNnBya3clK+TxCsZjY/+SwiFAshlI+z5ts+OEgTg6LWL12A3ON5fnQvHgxAOBLfkDlaVMzLl6NInTyCaV8Hg/Wd3kXEar+1Og9XLwatbUd5QqY/GXGdkzCDwfxYH0XpXgcoVgMz9tbcZQrIMs7VRB3CJHNzOMoV8BOQz1y7a2Apqoq469XL/A+yxMZLE9k1ENiP0Jq8+ogqD3X3oqdhvpyMTLzvJuFY0GS7WFEt9ZQtziLusVZ3uwKjSXqFmcR3Vqz9XHDDwcq42is9A01IMAM8frjn+1u16kTfrj8cBBuLlGcDvKQKl7zAwmdAx48fjjg4NE5xE8ZPhgO+YEOyQGPHj8c0Hh0DrEgQR6ioG6fIA8RbkD4zPKQmhtSejh1+mjkrriSkz//DghV5dCbjP34LQBgf3sPANDSWf71Sh44uLiDY+KAi4ciANeb6nnnIUtD3Y4/3SUHYepQ0Xl8y0P4NuMsDXXXZBCqB5Wf90744aDz5J4z5yHEXGPEaFUoe9BlGQNzG+LqqPjhQCVoohyEMM5D+Mo/bWrG9zt/WYJQLKY2a6FwZ6r+KzHLyK7viiej4oeDCMViQGVnnRwWMfV1B7JsvuSqCYgGu8JY2DxG/5NRAMBL5WT+zBWMfnrTyiVH7wGVLAOA5TSBHINdYWALWNgsf2fw4gCAv/9YQOF2L57fumU73v9kFMsTGWu+hHjJDHaFcZQrACyY4SslMa6ENtnMfE2o49WxsHlsO2EYOlSovzqXo1yhXGyGbcvRFqKO6onwY6bblUgPp05Vh9fx+BeO85xPwOeKuE34p81ZtpMfLj8chJtLFKeDgKgKDeYZgi5QkdA54MHjhwMOHp1D/Njlg+EQqOiQHPDo8cMBjUfnEAsSBEQK6vYJAiLhBoQgIDpbQKS+gVtApPNIDo6bgyCX5PlPAiJUfnIvDXVrAyKTh124g/DiIM49IHJDDW6kcKfhUgRLQ93KiFr8cBBnDohQef7qXTLJDxsxPbOCgbkNbbhDD+A44YdDx7tkUny+DPweYrt2K8lYIpu1Kjwwt2H15ZXlpIdTp0nNwy494RBK+XzN9cs5q0OdD+2mk8OitdDqQzfk0AZEOw31AICX3/RabUdNzYhurdXkE27wgMjL0z8EOQa7wogCmDQ8h8GuMAq3e9GvFHWHtZ9rQKTC+y9PZKynd8YNnv6B4FADI6+O/zUgSnsMcyTO6vBzPgEBZf4BFerpMf0IFM0AAAAASUVORK5CYII="
 


# 설정값
GAME_WIDTH, GAME_HEIGHT = 800, 700 
FRAME_W, FRAME_H = 17, 17
COLS = 4
FRAME_DELAY = 130
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
RED, YELLOW, ORANGE = (220, 50, 50), (240, 200, 0), (255, 140, 0)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1. 초기화 및 사운드
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT), pygame.RESIZABLE)
buffer = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("신호등 복구 작전: 난이도 조절판")
clock = pygame.time.Clock()

try:
    sound_hit = pygame.mixer.Sound("./assets/sounds/hit.wav")
    sound_heal = pygame.mixer.Sound("./assets/sounds/heal.wav")
    sound_levelup = pygame.mixer.Sound("./assets/sounds/level_up.wav")
    sound_victory = pygame.mixer.Sound("./assets/sounds/victory.wav")
    sound_gameover = pygame.mixer.Sound("./assets/sounds/game_over.wav")
    sound_siren = pygame.mixer.Sound("./assets/sounds/siren.wav")
    sound_dash = pygame.mixer.Sound("./assets/sounds/dash.wav")
    sound_car_pass = pygame.mixer.Sound("./assets/sounds/car_pass.wav")
    pygame.mixer.music.load("./assets/sounds/bgm.wav")
    pygame.mixer.music.set_volume(0.3)
    
    # 효과음 볼륨 최적화
    if sound_dash: sound_dash.set_volume(0.8)
    if sound_car_pass: sound_car_pass.set_volume(0.4)
except:
    sound_hit = sound_heal = sound_levelup = sound_victory = sound_gameover = sound_siren = sound_dash = sound_car_pass = None

def make_frames(b64_data, indices):
    try:
        if not b64_data: raise ValueError
        sheet_bytes = base64.b64decode(b64_data)
        img = pygame.image.load(io.BytesIO(sheet_bytes)).convert_alpha()
        return [img.subsurface(pygame.Rect((i % COLS) * FRAME_W, (i // COLS) * FRAME_H, FRAME_W, FRAME_H)) for i in indices]
    except:
        s = pygame.Surface((FRAME_W, FRAME_H)); s.fill((50, 50, 200)); return [s]

UP_WALK = make_frames(SHEET_UP_B64, [2, 6, 10]); DOWN_WALK = make_frames(SHEET_DOWN_B64, [1, 5, 9])
LEFT_WALK = make_frames(SHEET_LEFT_B64, [0, 4, 8]); RIGHT_WALK = make_frames(SHEET_RIGHT_B64, [3, 7, 11])

CAR_COLORS = ["Green", "Red", "Blue", "Black"]
CAR_IMAGES, AMBULANCE_IMAGES, SIGNAL_IMG = {}, {}, None
try:
    for c in CAR_COLORS: CAR_IMAGES[c] = {k: pygame.image.load(f"./assets/sprites/{c}_car_{k}.png").convert_alpha() for k in "udlr"}
    AMBULANCE_IMAGES = {k: pygame.image.load(f"./assets/sprites/Health_{k}.png").convert_alpha() for k in "udlr"}
    SIGNAL_IMG = pygame.image.load(f"./assets/sprites/Signal.png").convert_alpha()
except: pass

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2. 클래스 정의
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
class Player:
    def __init__(self):
        self.rect = pygame.Rect(GAME_WIDTH//2 - 20, GAME_HEIGHT//2 - 20, 40, 40)
        self.hp, self.level = 3, 1
        self.dash_count, self.dash_timer = 3, 0
        self.invincible_timer, self.speed = 0, 5
        self.current_frames = DOWN_WALK
        self.facing, self.is_moving = 'down', False
        self.frame_index, self.frame_timer = 0, 0

    def move(self, keys):
        s = int(self.speed * 2.5) if self.dash_timer > 0 else self.speed
        self.is_moving = False
        dx, dy = 0, 0
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: dx -= s; self.facing = 'left'; self.is_moving = True
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]: dx += s; self.facing = 'right'; self.is_moving = True
        if keys[pygame.K_w] or keys[pygame.K_UP]: dy -= s; self.facing = 'up'; self.is_moving = True
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]: dy += s; self.facing = 'down'; self.is_moving = True
        self.rect.x += dx; self.rect.y += dy
        self.rect.clamp_ip(pygame.Rect(0, 0, GAME_WIDTH, GAME_HEIGHT))

    def update_animation(self, dt):
        if self.is_moving:
            if self.facing == 'up': self.current_frames = UP_WALK
            elif self.facing == 'down': self.current_frames = DOWN_WALK
            elif self.facing == 'left': self.current_frames = LEFT_WALK
            elif self.facing == 'right': self.current_frames = RIGHT_WALK
        else: self.current_frames = [self.current_frames[0]]
        self.frame_timer += dt
        if self.frame_timer >= FRAME_DELAY:
            self.frame_index = (self.frame_index + 1) % len(self.current_frames)
            self.frame_timer = 0

    def draw(self, surface):
        if self.invincible_timer % 10 < 5:
            img = self.current_frames[self.frame_index % len(self.current_frames)]
            surface.blit(pygame.transform.scale(img, (self.rect.width, self.rect.height)), self.rect)

class MovingObject:
    def __init__(self, speed_range, itype=None):
        self.type = itype
        side = random.randint(0, 3)
        speed = random.randint(int(speed_range[0]*1.4), int(speed_range[1]*1.4))
        self.siren_channel, self.passed_sound_played = None, False
        if side == 0: self.dir_key, self.vx, self.vy = "u", 0, speed
        elif side == 1: self.dir_key, self.vx, self.vy = "d", 0, -speed
        elif side == 2: self.dir_key, self.vx, self.vy = "l", speed, 0
        else: self.dir_key, self.vx, self.vy = "r", -speed, 0

        if self.type == "heal":
            img_w, img_h = (90, 120) if self.dir_key in ["u", "d"] else (120, 90)
            self.image = pygame.transform.scale(AMBULANCE_IMAGES[self.dir_key], (img_w, img_h)) if AMBULANCE_IMAGES else None
            if sound_siren: self.siren_channel = sound_siren.play(-1)
            hit_w, hit_h = int(img_w * 0.7), int(img_h * 0.7)
        elif self.type == "lvup":
            img_w, img_h = 55, 75
            self.image = pygame.transform.scale(SIGNAL_IMG, (img_w, img_h)) if SIGNAL_IMG else None
            hit_w, hit_h = img_w, img_h
        else:
            img_w, img_h = (75, 100) if self.dir_key in ["u", "d"] else (100, 75)
            if CAR_IMAGES: self.image = pygame.transform.scale(CAR_IMAGES[random.choice(CAR_COLORS)][self.dir_key], (img_w, img_h))
            else: self.image = None
            hit_w, hit_h = (50, 70) if self.dir_key in ["u", "d"] else (70, 50)
        self.rect = pygame.Rect(0, 0, img_w, img_h)
        if side == 0: self.rect.x, self.rect.y = random.randint(0, GAME_WIDTH-img_w), -img_h
        elif side == 1: self.rect.x, self.rect.y = random.randint(0, GAME_WIDTH-img_w), GAME_HEIGHT
        elif side == 2: self.rect.x, self.rect.y = -img_w, random.randint(0, GAME_HEIGHT-img_h)
        else: self.rect.x, self.rect.y = GAME_WIDTH, random.randint(0, GAME_HEIGHT-img_h)
        self.hitbox = pygame.Rect(0, 0, hit_w, hit_h)
        self.glow_timer = 0.0

    def stop_siren(self):
        if self.siren_channel: self.siren_channel.stop(); self.siren_channel = None
    def update(self):
        self.rect.x += self.vx; self.rect.y += self.vy
        self.hitbox.center = self.rect.center
        self.glow_timer += 0.1
    def draw(self, surface):
        if self.image:
            if self.type in ["heal", "lvup"]:
                pulse = int((math.sin(self.glow_timer) + 1) / 2 * 130)
                g_surf = pygame.Surface((self.rect.width + 40, self.rect.height + 40), pygame.SRCALPHA)
                pygame.draw.ellipse(g_surf, (255, 0, 0, pulse) if self.type == "heal" else (255, 255, 0, pulse), g_surf.get_rect())
                surface.blit(g_surf, (self.rect.x - 20, self.rect.y - 20))
            surface.blit(self.image, self.rect)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3. 유틸리티 함수
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
shake_amount = 0
particles = []

def trigger_shake(amount): global shake_amount; shake_amount = amount
def spawn_particles(x, y):
    for _ in range(15): particles.append({"x": x, "y": y, "vx": random.uniform(-4, 4), "vy": random.uniform(-6, 0), "life": random.randint(20, 40), "color": random.choice([RED, YELLOW, ORANGE])})
def update_particles():
    for p in particles[:]:
        p["x"] += p["vx"]; p["y"] += p["vy"]; p["vy"] += 0.2; p["life"] -= 1
        if p["life"] <= 0: particles.remove(p)

def draw_text(surf, text, x, y, size=30, color=WHITE, center=False):
    font = pygame.font.SysFont("malgungothic", size); txt = font.render(text, True, color)
    rect = txt.get_rect()
    if center: rect.center = (x, y)
    else: rect.topleft = (x, y)
    surf.blit(txt, rect)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 4. 메인 루프
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def main():
    global shake_amount, particles; particles = []
    pygame.mouse.set_visible(False)
    try:
        bg = pygame.image.load("./assets/sprites/DORO.png").convert_alpha()
        bg = pygame.transform.scale(bg, (GAME_WIDTH, GAME_HEIGHT))
    except: bg = None

    p = Player(); enemies, items = [], []
    spawn_timer, item_timer, death_timer = 0, 0, -1
    if not pygame.mixer.music.get_busy(): pygame.mixer.music.play(-1)

    while True:
        dt = clock.tick(60)
        
        # [난이도 재배치 로직]
        # n: 소환 주기 (클수록 쉬움), sp: 적 속도
        conf = [
            {"sp": (3, 5), "n": 40}, # Level 1 (신규 - 아주 쉬움)
            {"sp": (4, 6), "n": 25}, # Level 2 (구 레벨 1)
            {"sp": (5, 7), "n": 18}, # Level 3 (구 레벨 2)
            {"sp": (6, 8), "n": 12}  # Level 4 (구 레벨 3)
        ][min(p.level-1, 3)]

        for e in pygame.event.get():
            if e.type == pygame.QUIT: pygame.quit(); sys.exit()
            if e.type == pygame.VIDEORESIZE: pygame.display.set_mode((e.w, e.h), pygame.RESIZABLE)
            if e.type == pygame.KEYDOWN and e.key in [pygame.K_SPACE, pygame.K_LSHIFT]:
                if p.dash_count > 0 and p.dash_timer <= 0 and death_timer == -1:
                    p.dash_count -= 1; p.dash_timer = 12; sound_dash.play() if sound_dash else None

        if death_timer == -1:
            p.move(pygame.key.get_pressed()); p.update_animation(dt)
            spawn_timer += 1
            if spawn_timer >= conf["n"]: enemies.append(MovingObject(conf["sp"])); spawn_timer = 0
            item_timer += 1
            if item_timer > 150: items.append(MovingObject((4, 6), "heal" if random.random() > 0.7 else "lvup")); item_timer = 0

        update_particles()
        if p.dash_timer > 0: p.dash_timer -= 1
        if p.invincible_timer > 0: p.invincible_timer -= 1

        for en in enemies[:]:
            en.update()
            dist = math.hypot(p.rect.centerx - en.rect.centerx, p.rect.centery - en.rect.centery)
            if dist < 120 and not en.passed_sound_played and not en.type:
                sound_car_pass.play() if sound_car_pass else None; en.passed_sound_played = True
            if not pygame.Rect(0, 0, GAME_WIDTH, GAME_HEIGHT).inflate(300, 300).contains(en.rect): enemies.remove(en)
            elif p.rect.colliderect(en.hitbox) and p.dash_timer <= 0 and p.invincible_timer <= 0 and death_timer == -1:
                p.hp -= 1; trigger_shake(20); spawn_particles(p.rect.centerx, p.rect.centery)
                sound_hit.play() if sound_hit else None
                if p.hp <= 0: death_timer = 45; [it.stop_siren() for it in items]
                else: p.invincible_timer = 60

        for it in items[:]:
            it.update()
            if not pygame.Rect(0, 0, GAME_WIDTH, GAME_HEIGHT).inflate(300, 300).contains(it.rect): it.stop_siren(); items.remove(it)
            elif p.rect.colliderect(it.hitbox) and death_timer == -1:
                it.stop_siren()
                if it.type == "lvup": p.level += 1; p.dash_count = 3; sound_levelup.play() if sound_levelup else None
                else: p.hp = min(3, p.hp + 1); sound_heal.play() if sound_heal else None
                items.remove(it)

        # 1. 버퍼에 그리기
        if bg: buffer.blit(bg, (0,0))
        else: buffer.fill((30, 30, 40))
        for it in items: it.draw(buffer)
        for en in enemies: en.draw(buffer)
        for pt in particles: pygame.draw.circle(buffer, pt["color"], (int(pt["x"]), int(pt["y"])), 4)
        if p.hp > 0: p.draw(buffer)
        
        # UI 좌표 수정 (잘림 방지)
        draw_text(buffer, f"SIGNAL: {p.level - 1}/4", 40, 30, 30, YELLOW) # x: 20 -> 40
        draw_text(buffer, f"HP: {'♥' * max(0, p.hp)}", 260, 30, 30, RED)
        draw_text(buffer, f"DASH: {p.dash_count}", 450, 30, 30, WHITE)

        # 2. 확대 배율 계산 및 중앙 정렬 출력
        screen.fill(BLACK)
        sw, sh = screen.get_size()
        ratio = min(sw / GAME_WIDTH, sh / GAME_HEIGHT)
        new_size = (int(GAME_WIDTH * ratio), int(GAME_HEIGHT * ratio))
        scaled_buffer = pygame.transform.smoothscale(buffer, new_size)
        
        ox, oy = (random.randint(-shake_amount, shake_amount), random.randint(-shake_amount, shake_amount)) if shake_amount > 0 else (0,0)
        shake_amount = max(0, shake_amount - 1)
        
        pos_x = (sw - new_size[0]) // 2 + ox
        pos_y = (sh - new_size[1]) // 2 + oy
        
        screen.blit(scaled_buffer, (pos_x, pos_y))
        pygame.display.flip()

        if death_timer > 0: death_timer -= 1
        elif death_timer == 0:
            if show_end_screen("GAME OVER", RED): main(); return
            else: break
        if p.level >= 5 and death_timer == -1:
            if show_end_screen("VICTORY!", YELLOW): main(); return
            else: break

def show_end_screen(title, color):
    pygame.mouse.set_visible(True); pygame.mixer.music.stop()
    if title == "VICTORY!" and sound_victory: sound_victory.play()
    elif title == "GAME OVER" and sound_gameover: sound_gameover.play()
    while True:
        sw, sh = screen.get_size()
        screen.fill(BLACK)
        draw_text(screen, title, sw//2, sh//2 - 50, 60, color, True)
        draw_text(screen, "Press 'R' to Restart or 'Q' to Quit", sw//2, sh//2 + 50, 25, WHITE, True)
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT: pygame.quit(); sys.exit()
            if e.type == pygame.VIDEORESIZE: pygame.display.set_mode((e.w, e.h), pygame.RESIZABLE)
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r: return True
                if e.key == pygame.K_q: pygame.quit(); sys.exit()

if __name__ == "__main__":
    main()