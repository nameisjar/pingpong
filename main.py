from pygame import *

back = (0, 0, 0)
win_width = 500
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('game pingpong')
window.fill(back)
clock = time.Clock()

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
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
        

racket_l = GameSprite('racket_left.png', 20, 200, 65, 65, 4)
racket_r = GameSprite('racket_right.png', 400, 300, 65, 65, 4)
ball = GameSprite('ball.png', 250, 200, 40, 40, 3)
speed_x = 3
speed_y = 3
run = True
finish = False
while run:
    if not finish:
        window.fill(back)
        racket_l.reset()
        racket_l.update_l()
        racket_r.reset()
        racket_r.update_r()
        ball.reset()
        # membuat bola bergerak
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    # memantulkan bola disisi samping
    if ball.rect.y > win_height - 50 or ball.rect.y < 0:
        speed_y *= -1
    # membuat kalah disisi kiri
    if ball.rect.x < 0:
        lose = transform.scale(image.load('lose.png'), (200, 200))
        window.blit(lose, (150, 150))
        finish = True
    
    # membuat kalah disisi kanan
    if ball.rect.x > win_width - 50:
        lose = transform.scale(image.load('lose.png'), (200, 200))
        window.blit(lose, (150, 150))
        finish = True
    # memantulkan bola di racket kiri dan kanan
    if (sprite.collide_rect(racket_l, ball) 
        or sprite.collide_rect(racket_r, ball)):
        speed_x *= -1
    
    for e in event.get():
        if e.type == QUIT:
            run = False
            
    clock.tick(60)
    display.update()
display.update()


