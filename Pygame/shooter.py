import pygame import random 
from colors import *

pygame.init()
screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode([screen_width,screen_height])
done = False
clock = pygame.time.Clock()
score = 0 
player.rect.y = 370

all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

class Block(pygame.sprite.Sprite):
    def __init__(self.color):
        super().__init__()
        self.image = pygame.Surface([20,15])
        self.image.fill(color)
        self.rect = self.image.get.rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__
        self.image = pygame.Surface([20,20])
        self.image.fill(RED)
        
       self.rect = self.image.get_rect()
       
    def update(self):
        pos = pygame.mouse.get_pos()
        
        self.rect.x = pos[0]

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__
        
        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= 3

for i in range(50):
    block = Block(BLUE)
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(350)
    block_list.add(block)
    all_sprites_list.add(block)

player = Player()
all_sprites_list.add(player)