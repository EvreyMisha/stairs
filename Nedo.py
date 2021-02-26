import pygame
import random
clock = pygame.time.Clock()

pygame.init()
height = 300
width = 794
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Крес")

all_sprites = pygame.sprite.Group()
down = pygame.sprite.Group()
up = pygame.sprite.Group()
pt = pygame.sprite.Group()

class Down(pygame.sprite.Sprite):
    image = pygame.Surface([50, 10])

    def __init__(self,pos):
        super().__init__(down)
        self.image.fill((70,70,70))
        self.rect = pygame.Rect(pos[0],pos[1],50,10)
        self.add(down)

class Up(pygame.sprite.Sprite):
    image = pygame.Surface([10, 50])

    def __init__(self,pos):
        super().__init__(up)
        self.image.fill((255,0,0))
        self.rect = pygame.Rect(pos[0],pos[1],10,50)
        self.add(up)
class Landing(pygame.sprite.Sprite):
    image = pygame.Surface([20, 20])

    def __init__(self, pos):
        super().__init__(pt)
        self.image.fill((0,0,255))
        self.rect = pygame.Rect(pos[0],pos[1],20,20)
        self.add(pt)

    def update(self):
        if not (pygame.sprite.spritecollideany(self, down) or pygame.sprite.spritecollideany(self, up)):
            self.rect = self.rect.move(0, 2)
        keys = pygame.key.get_pressed()
        if pygame.sprite.spritecollideany(self, up):
            if keys[pygame.K_w]:
                self.rect = self.rect.move(0, -10)
            if keys[pygame.K_s]:
                self.rect = self.rect.move(0, 10)
        if keys[pygame.K_a]:
            self.rect = self.rect.move(-10, 0)
        if keys[pygame.K_d]:
            self.rect = self.rect.move(10, 0)

run = True
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if pygame.mouse.get_pressed()[0] and keys[pygame.K_LCTRL]:
        Up(pygame.mouse.get_pos())
    elif pygame.mouse.get_pressed()[0]:
        Down(pygame.mouse.get_pos())
    if pygame.mouse.get_pressed()[2]:
        pt.empty()
        Landing(pygame.mouse.get_pos())

    win.fill((0, 0, 0))
    pt.update()
    up.draw(win)
    down.draw(win)
    pt.draw(win)
    clock.tick(10)
    pygame.display.flip()

pygame.quit()
