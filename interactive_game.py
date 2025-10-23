import sys     #导入sys模块,使用sys.exit()函数退出程序 内置模块
import pygame  #导入pygame模块,使用pygame模块中的函数  第三方模块
import time 
import random
import math

def show_start_screen(screen, screen_rect):
    font = pygame.font.SysFont(None, 80)
    button_font = pygame.font.SysFont(None, 60)
    title_img = font.render("Shooting game", True, (255,255,255))
    button_img = button_font.render("Start game", True, (0,0,0))
    button_w, button_h = 300, 100 
    button_rect = pygame.Rect(0,0,button_w,button_h)
    button_rect.center = screen_rect.center
    # 操作说明文本
    info_font = pygame.font.SysFont(None, 40)
    instructions = [
        "Q: Quit game",
        "SPACE: Shoot", 
        " A/D: Move left / right",
        "The number of UFOs will increase over time.",
        "Try your best to get a high score!"
    ]
    while True:
        screen.fill((79,142,247))
        screen.blit(title_img, (screen_rect.centerx-title_img.get_width()//2, screen_rect.centery-200))
        pygame.draw.rect(screen, (255,200,0), button_rect)
        screen.blit(button_img, (button_rect.centerx-button_img.get_width()//2, button_rect.centery-button_img.get_height()//2))
        # 显示操作说明
        for i, text in enumerate(instructions):
            info_img = info_font.render(text, True, (255,255,255))
            y = button_rect.bottom + 40 + i*50
            screen.blit(info_img, (screen_rect.centerx-info_img.get_width()//2, y))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return

pygame.init()  #初始化pygame,必须有a
pygame.mixer.init()  #初始化音频模块

# 加载并播放背景音乐（循环播放）
# 注意：请下载音乐文件并放在 assets 文件夹中
try:
    pygame.mixer.music.load("assets/background_music.wav/Audio_MainMenu.WAV")
    pygame.mixer.music.set_volume(0.3)  # 设置音量（0.0-1.0），0.3 比较合适
    pygame.mixer.music.play(-1)  # -1表示无限循环播放
except Exception as e:
    print(f"警告：未找到背景音乐文件 - {e}")


# 爆炸粒子类
class Particle:
    def __init__(self, pos, color=None):
        self.x, self.y = pos
        angle = random.uniform(0, 2 * 3.14159)
        speed = random.uniform(3, 7)
        self.vx = speed * math.cos(angle)
        self.vy = speed * math.sin(angle)
        self.life = random.randint(12, 20)
        self.color = color if color else (255, random.randint(100,255), 0)
        self.radius = random.randint(2, 4)
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vx *= 0.92
        self.vy *= 0.92
        self.life -= 1
        if self.radius > 1:
            self.radius -= 0.1
    def draw(self, surf):
        if self.life > 0:
            pygame.draw.circle(surf, self.color, (int(self.x), int(self.y)), int(self.radius))


bg_color1 = (79,142,247)  #设置背景颜色 RGB颜色模式
bg_color2 = (255,0,0)

bg_color3 = (249,160,63)

# 全屏显示
screen_image = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # 全屏显示
screen_rect = screen_image.get_rect()

# 游戏开始界面
show_start_screen(screen_image, screen_rect)

"Title"
pygame.display.set_caption("airShip Invasion")  #设置窗口标题

# 加载UFO图片并缩小到1/5（放大一倍）
ufo_image_raw = pygame.image.load("ufo.bmp")
ufo_image = pygame.transform.scale(ufo_image_raw, (ufo_image_raw.get_width() // 5, ufo_image_raw.get_height() // 5))
ufo_rect = ufo_image.get_rect()
ufos = pygame.sprite.Group()

# UFO子弹

# UFO子弹类，增加owner属性
class UfoBullet(pygame.sprite.Sprite):
    def __init__(self, start_pos, target_pos, owner=None):
        super().__init__()
        self.rect = pygame.Rect(0,0,4,12)
        self.rect.midtop = start_pos
        self.vx = 0
        self.vy = 4
        self.owner = owner  # 记录发射该子弹的UFO
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

ufo_bullets = pygame.sprite.Group()

#pygame.display.flip()  #更新屏幕内容
#time.sleep(2) #暂停2秒

#screen_image.fill(bg_color2)  
#pygame.display.flip() 
#time.sleep(2)

"Ship"
ship_image = pygame.image.load("airplane.bmp")  #加载图像
ship_rect = ship_image.get_rect()  #获取图像矩形
#ship_image = pygame.transform.scale(ship_image,(100,100))  #调整图像大小
#pygame.image.save(ship_image, "ship_resize.bmp")  #保存调整后的图像
ship_rect.midbottom = screen_rect.midbottom  #设置图像位置为屏幕中央
moving_left = False
moving_right = False

ship_speed = 300  # 飞船移动速度（像素/秒）
# 控制飞船移动频率
ship_move_counter = 0
clock = pygame.time.Clock()  # 帧率控制器

# UFO参数
UFO_EVENT = pygame.USEREVENT + 1
ufo_interval = 800  # 更高频率，0.8秒生成一个
pygame.time.set_timer(UFO_EVENT, ufo_interval)
UFO_BULLET_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(UFO_BULLET_EVENT, 1200)  # UFO发射子弹

# UFO移动参数
UFO_MOVE_SPEED = 2

"bullet"

bullets = pygame.sprite.Group()
explosions = []  # 每个元素是一个粒子列表

#"Text"
#txt_font = pygame.font.SysFont(None, 48)  
#text_image = txt_font.render("Hello, Pygame!", True, bg_color2, bg_color3)  #创建文本图像
#txt_rect = text_image.get_rect()
#txt_rect.x = 500
#txt_rect.y = 20

UFO_MOVE_SPEED = 150  # UFO移动速度（像素/秒）

# 游戏开始时立即生成一个UFO，带有随机左右初始方向和速度
def create_random_ufo():
    ufo = pygame.sprite.Sprite()
    ufo.image = ufo_image
    ufo.rect = ufo_image.get_rect()
    ufo.rect.x = random.randint(0, screen_rect.width - ufo.rect.width)
    ufo.rect.y = random.randint(0, screen_rect.height // 5)  # 只在最上方1/5区域
    ufo.move_dir = random.choice([-1, 1])
    # Increase base speed for higher initial challenge
    elapsed = int(time.time() - start_time) if 'start_time' in globals() else 0
    base_speed = random.randint(180, 320)  # was 80-220, now 180-320
    ufo.move_speed = min(base_speed + elapsed * 2, 500)
    return ufo

ufos.add(create_random_ufo())

start_time = time.time()
font = pygame.font.SysFont(None, 48)

# 积分系统
score = 0
score_font = pygame.font.SysFont(None, 48)

while  True:
    elapsed = int(time.time() - start_time)
    dt = clock.tick(60) / 1000.0  # 每帧耗时（秒），并限制最大帧率为60FPS
    # UFO生成速率恒定，速度随时间递增
    for event in pygame.event.get(): #获取事件
        #print(event)  #打印事件test
        if event.type == pygame.QUIT:  #如果单击关闭窗口,则退出程序
            sys.exit()
        elif event.type == pygame.KEYDOWN:  #如果按下键盘
            if event.key == pygame.K_q:  #按q键退出
                sys.exit()
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_SPACE:
                if len(bullets) < 5:  #限制屏幕上子弹数量
                    new_bullet = pygame.sprite.Sprite()
                    new_bullet.rect = pygame.Rect(0,0,3,15)
                    new_bullet.rect.midbottom = ship_rect.midtop
                    bullets.add(new_bullet)
        elif event.type == UFO_EVENT:
            # 生成更随机的UFO
            ufos.add(create_random_ufo())
        elif event.type == UFO_BULLET_EVENT:
            # UFO发射子弹（只向下）
            for ufo in ufos:
                bullet = UfoBullet(ufo.rect.midbottom, None, owner=ufo)
                ufo_bullets.add(bullet)
        elif event.type == pygame.KEYUP: #松开可以停止
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
                
    # 飞船移动，速度与帧率无关
    move_dist = int(ship_speed * dt)
    if moving_left and ship_rect.left > 0:
        ship_rect.x -= move_dist
        if ship_rect.left < 0:
            ship_rect.left = 0
    if moving_right and ship_rect.right < screen_rect.right:
        ship_rect.x += move_dist
        if ship_rect.right > screen_rect.right:
            ship_rect.right = screen_rect.right

    # UFO移动，速度与帧率无关，每个UFO有独立速度和初始方向
    for ufo in list(ufos):
        if not hasattr(ufo, 'move_dir'):
            ufo.move_dir = random.choice([-1, 1])
        if not hasattr(ufo, 'move_speed'):
            ufo.move_speed = random.randint(80, 220)
        ufo_move_dist = int(ufo.move_speed * dt)
        ufo.rect.x += ufo.move_dir * ufo_move_dist
        # 到达边界反向
        if ufo.rect.left <= 0:
            ufo.rect.left = 0
            ufo.move_dir = 1
        elif ufo.rect.right >= screen_rect.width:
            ufo.rect.right = screen_rect.width
            ufo.move_dir = -1

    # UFO子弹移动（带跟踪）
    for ub in list(ufo_bullets):
        ub.update()
        if ub.rect.top > screen_rect.height or ub.rect.left > screen_rect.width or ub.rect.right < 0:
            ufo_bullets.remove(ub)

    # 检查UFO子弹与飞船碰撞
    for ub in list(ufo_bullets):
        if ship_rect.colliderect(ub.rect):
            # 游戏失败
            print("你被UFO击中了，游戏失败！")
            pygame.quit()
            sys.exit()

    # 检查玩家子弹与UFO碰撞
    for bullet in list(bullets):
        for ufo in list(ufos):
            if ufo.rect.colliderect(bullet.rect):
                # 产生爆炸粒子动画，UFO暂时不消失
                particles = [Particle(ufo.rect.center) for _ in range(18)]
                explosions.append({'particles': particles, 'center': ufo.rect.center})
                ufo.exploding = True
                bullets.remove(bullet)
                score += 5  # 消灭一个UFO加5分
                break
    # 爆炸动画结束后移除UFO，并移除其子弹
    for ufo in list(ufos):
        if hasattr(ufo, 'exploding') and ufo.exploding:
            # 检查是否有爆炸粒子还在ufo位置
            still_exploding = False
            for exp in explosions:
                if (abs(exp['center'][0] - ufo.rect.centerx) < 10 and abs(exp['center'][1] - ufo.rect.centery) < 10):
                    # 只要有粒子还活着
                    if any(p.life > 0 for p in exp['particles']):
                        still_exploding = True
                        break
            if not still_exploding:
                # 移除该UFO发射的所有子弹
                for ub in list(ufo_bullets):
                    if hasattr(ub, 'owner') and ub.owner == ufo:
                        ufo_bullets.remove(ub)
                ufos.remove(ufo)


    #bullet_rect.y -= 1
    #if bullet_rect.bottom < 0:
        #bullet_rect.midbottom = ship_rect.midtop
    
    "Draw"
    screen_image.fill(bg_color1)  #设置背景色
    screen_image.blit(ship_image, ship_rect)  #绘制图像
    # 绘制UFO
    for ufo in ufos:
        if not hasattr(ufo, 'exploding') or not ufo.exploding:
            screen_image.blit(ufo_image, ufo.rect)

    # 绘制计时器（左上角）
    elapsed = int(time.time() - start_time)
    min_sec = f"{elapsed//60:02d}:{elapsed%60:02d}"
    timer_img = font.render(f"Time: {min_sec}", True, (255,255,255))
    screen_image.blit(timer_img, (20, 20))

        # 绘制积分（右上角）
    score_img = score_font.render(f"Score: {score}", True, (255,255,0))
    screen_image.blit(score_img, (screen_rect.width - score_img.get_width() - 30, 20))
    bullet_move_dist = int(800 * dt)  # 子弹速度（像素/秒）
    for bullet in list(bullets):
        pygame.draw.rect(screen_image, bg_color2, bullet.rect) 
        bullet.rect.y -= bullet_move_dist
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

    # 绘制UFO子弹
    for ub in ufo_bullets:
        pygame.draw.rect(screen_image, (0,255,0), ub.rect)
            
    # for bullet_rect in bullets:
    #     pygame.draw.rect(screen_image, bg_color2, bullet_rect) 
    #     bullet_rect.y -= 1
    #     if bullet_rect.bottom < 0:
    #         bullets.remove(bullet_rect)
    

    # 绘制爆炸粒子
    for exp in list(explosions):
        for p in exp['particles']:
            p.update()
            if p.life > 0:
                p.draw(screen_image)
        # 如果所有粒子都消失则移除该爆炸
        if all(p.life <= 0 for p in exp['particles']):
            explosions.remove(exp)

    pygame.display.flip()  #更新屏幕内容