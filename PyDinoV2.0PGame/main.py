import pygame
from random import randint
from time import sleep
pygame.font.init()
WIDTH = 1000
HEIGHT = 480
FPS = 60
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.LayeredUpdates()
cactosis = pygame.sprite.Group()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
WHITE = (255, 255, 255)
jump = False
jumpMax = 18
jumpCount = 0
coctoses = []
clouds = []
coins = 0
game_process = True
sound1 = pygame.mixer.Sound('jump.wav')
sound2 = pygame.mixer.Sound('death.wav')

class dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_1 = pygame.image.load("dino.png")
        self.image_2 = pygame.image.load("dino1.png")
        self.image_1 = pygame.transform.scale(self.image_1, (100, 100))
        self.image_2 = pygame.transform.scale(self.image_2, (100, 100))
        self.image_1.set_colorkey(WHITE)
        self.image_2.set_colorkey(WHITE)
        self.animation_frame = 1
        self.image = self.image_1
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(WHITE)
        self.radius = 30
        self.rect.x = WIDTH / 2 - 53
        self.rect.y = HEIGHT / 2 - 51
        self._layer = self.rect.bottom
        self.cooldown = 200
        self.last = 0
    def update(self):
        global jump,jumpMax,jumpCount,running,coins,game_process
        pygame.draw.circle(self.image, "red", self.rect.center, self.radius)
        coins += 1
        if jump:
            dino.rect.y -= jumpCount
            if jumpCount > -jumpMax:
                jumpCount -= 1
            else:
                jump = False
        hits = pygame.sprite.spritecollide(dino, cactosis, False, pygame.sprite.collide_circle)
        if hits:
            game_process = False
            sound2.play()
            pygame.draw.circle(self.image, "white", (35,5), 3)
        now = pygame.time.get_ticks()
        if now - self.last >= self.cooldown:
            self.last = now
            self.animation()
    def animation(self):
        if self.animation_frame == 1:
            self.image = self.image_2
            self.animation_frame = 2
        else:
            self.image = self.image_1
            self.animation_frame = 1
class cactos(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = None
        self.image = None
        self.X = 0
        self.Y = dino.rect.y
        self.type = 0
        self.Y_add = 0
        self.radius = 0
        self.type_1_image = pygame.image.load("dino_cactos.png")
        self.type_2_image = pygame.image.load("dino_cactos1.png")
        self.sleep = randint(0,200)
        self.add_int = 0
        self.change_type()
    def update(self):
        global coctoses
        if self.sleep == 0 or self.sleep < 0:
            self.rect.x -= 8
            if self.rect.x < 0:
                self.sleep = randint(100,200)
                self.rect.x = randint(WIDTH+100,WIDTH+1000)
                self.change_type()
        else:
            self.sleep -= randint(1,5)
    def change_type(self):
        self.type = randint(1, 2)
        self.Y_add = 0
        self.radius = 0
        self.add_int = randint(0, 5)
        if self.type == 1:
            self.image = self.type_1_image
            self.image = pygame.transform.scale(self.image, (60+self.add_int, 100))
            self.Y_add = 0
            self.radius = 18
        elif self.type == 2:
            self.image = self.type_2_image
            self.image = pygame.transform.scale(self.image, (52+self.add_int, 80))
            self.Y_add = 24
            self.radius = 14
        self.rect = self.image.get_rect()
        self.rect.x = self.X
        self.rect.y = self.Y
        self.image.set_colorkey(WHITE)
        self.X = randint(WIDTH+200,WIDTH+1000)
        self.rect.y = self.Y + self.Y_add
        #pygame.draw.circle(self.image, "red", (self.image.get_width() / 2, self.image.get_height() / 2), self.radius)
class ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ground.png")
        #self.image = pygame.transform.scale(self.image, (60, 100))
        self.rect = self.image.get_rect()
        self.rect.y = 265
        self._layer = self.rect.bottom
class cloud(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("dino_cloud.png")
        self.image = pygame.transform.scale(self.image, (100, 35))
        self.image.set_colorkey("black")
        self.rect = self.image.get_rect()
        self.add_int = 0
    def update(self):
        if self.rect.x < 0:
            self.add_int = randint(0,20)
            self.image = pygame.transform.scale(self.image, (100+self.add_int, 35+self.add_int))
            self.image.set_colorkey("black")
            self.rect = self.image.get_rect()
            self.rect.x = randint(WIDTH+100, WIDTH + 1000)
            self.rect.y = randint(0,150)
        self.rect.x -= 5
class stone(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("stone.png")
        self.add_int = +randint(0,20)
        self.image = pygame.transform.scale(self.image, (24+self.add_int, 16+self.add_int))
        self.image.set_colorkey("white")
        self.rect = self.image.get_rect()
    def update(self):
        if self.rect.x < 0:
            self.rect.x = randint(WIDTH+100, WIDTH + 1000)
            self.rect.y = randint(315,HEIGHT)
        self.rect.x -= 8
class ground_cactos(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("dino_cactos_ground.png")
        self.add_int = +randint(0,20)
        self.image = pygame.transform.scale(self.image, (50+self.add_int, 94+self.add_int))
        self.image.set_colorkey("white")
        self.rect = self.image.get_rect()
    def update(self):
        if self.rect.x < 0:
            self.add_int = +randint(0, 20)
            self.image = pygame.transform.scale(self.image, (50+self.add_int, 94+self.add_int))
            self.image.set_colorkey("white")
            self.rect = self.image.get_rect()
            self.rect.x = randint(WIDTH+100,WIDTH+1000)
            self.rect.y = randint(315, HEIGHT - 100)
        self.rect.x -= 8
ground = ground()
dino = dino()
def add_cloud():
    cloud_ = cloud()
    clouds.append(cloud_)
    all_sprites.add(cloud_)
def add_cactos():
    cactos_ = cactos()
    coctoses.append(cactos_)
    all_sprites.add(cactos_)
    cactosis.add(cactos_)
def add_stone():
    stone__ = stone()
    all_sprites.add(stone__)
    return stone__
def add_ground_cactos():
    ground_cactos_ = ground_cactos()
    all_sprites.add(ground_cactos_)
    return ground_cactos_
for i in range(3):
    add_cactos()
for i in cactosis:
    all_sprites.change_layer(i, 2)
for i in range(4):
    add_cloud()
for i in range(4):
    stone_ = add_stone()
    all_sprites.change_layer(stone_, 2)
for i in range(2):
    ground_cactos__ = add_ground_cactos()
    all_sprites.change_layer(ground_cactos__, 3)
all_sprites.add(dino,ground)
all_sprites.change_layer(ground,1)
all_sprites.change_layer(dino,2)
# Цикл игры
running = True
X = 0
while running:
    clock.tick(FPS)
    if game_process:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if not jump and event.key == pygame.K_SPACE:
                    jump = True
                    sound1.play()
                    jumpCount = jumpMax
        screen.fill(WHITE)
        text_surface = my_font.render(str(coins), False, (0, 0, 0))
        screen.blit(text_surface, (0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
    if not game_process:
        text_surface = my_font.render("Для начала игры нажмите <ПРОБЕЛ>", False, (0, 0, 0))
        screen.blit(text_surface, (280, 0))
        coins = 0
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_process = True
                    for i in coctoses:
                        i.change_type()
                    for i_ in clouds:
                        i_.rect.x = randint(WIDTH+100, WIDTH + 1000)
    pygame.display.flip()
pygame.quit()