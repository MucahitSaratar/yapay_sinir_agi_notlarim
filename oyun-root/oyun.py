#!/usr/bin/python
import pygame
import time
import random as R


pg = pygame
pg.init()
screen = pg.display.set_mode([500, 500])

yuksek = 500
genislik = 500

dx = 250

dujminx = R.randint(0,genislik-50)
dujminy = R.randint(0,300)

def clean_screen():
    screen.fill((0, 0, 0))
    pg.draw.rect(screen, (255,0,0), pygame.Rect(dx, 450, 60, 6)) # sag,yukari,genislik,yukseklik
    dusman = pg.draw.rect(screen, (0,0,255), pygame.Rect(dujminx, dujminy, 40, 20))
    pg.display.flip()
    return dusman
#    print("clean dan ciktim")


def fire():
    global dujminx
    global dujminy
    i = 450
    while i >= 0:
        dusmanim = clean_screen()
        atesim = pg.draw.rect(screen, (0,255,0), pygame.Rect(dx+30, i, 6, 6))
        pg.display.flip()
        time.sleep(0.001)
        i -= 2
        if dusmanim.colliderect(atesim):
            dujminx = R.randint(0,genislik-50)
            dujminy = R.randint(0,300)
    clean_screen()
    print("outed fire")

def move(key):
    global dx
    if dx < 440 and key == pygame.K_d:
        dx += 35
    elif dx > 0 and key == pygame.K_a:
        dx -= 35
    clean_screen()


clean_screen()


mainrun = True
while mainrun:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            mainrun = False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fire()
            if event.key == pygame.K_d or event.key == pygame.K_a:
                move(event.key)

pg.quit()

