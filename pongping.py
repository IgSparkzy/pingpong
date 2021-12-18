from pygame import *
from random import randint


background_pic = "plain-blue-background.jpg"

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_mode((win_width, win_height))
background = transform.scale(image.load(background_pic), (800, 600))
speed_x = 3
speed_y = 3

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
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 140:
            self.rect.y += self.speed


class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 140:
            self.rect.y += self.speed




class ball(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()




player_1 = Player('racket.jpg', 5, win_height - 300, 40, 140, 10)
player_2 = Player2('racket.jpg', 655, win_height - 300, 40, 140, 10)
Ball = ball()

finish = False
#основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
   #событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False


    if not finish:

        window.blit(background,(0,0))
 
        player_1.update()
        player_2.update()
#        ball_1.update()
       
        player_1.reset()
        player_2.reset()
#        player_2.draw(window)
#        ball_1.draw(window)
        display.update()
        time.delay(50)