from pygame import *
from random import randint


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_mode((win_width, win_height))
background = transform.scale(image.load("blue sky image"), (800, 600))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y += self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y -= self.speed


class Enemy(GameSprite):
    def update (self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1
