import pygame

import sys


from pygame.locals import *


pygame.init() 

clock = pygame.time.Clock()

d_width = 300
d_height = 300

screen = pygame.display.set_mode((d_width, d_height))

back_color = (100, 100, 100)



pygame.mouse.set_visible(0)

pygame.display.set_caption('Sina Ebrahime')

b_img1 = pygame.image.load('1.jpg')
b_img2 = pygame.image.load('2.jpg')
b_img3 = pygame.image.load('3.jpg')
b_img4 = pygame.image.load('4.jpg')
b_img5 = pygame.image.load('5.jpg')
b_img6 = pygame.image.load('6.jpg')
b_img7 = pygame.image.load('7.jpg')
b_img8 = pygame.image.load('8.jpg')
b_img9 = pygame.image.load('9.jpg')
b_img10 = pygame.image.load('10.jpg')
b_img11 = pygame.image.load('11.jpg')
b_img12 = pygame.image.load('12.jpg')
b_img13 = pygame.image.load('13.jpg')
b_img14 = pygame.image.load('14.jpg')
b_img15 = pygame.image.load('15.jpg')


x1, y1 = (0, 0)
x2, y2 = (0, 75)
x3, y3 = (0, 150)
x4, y4 = (0, 225)
x5, y5 = (75, 0)
x6, y6 = (75, 75)
x7, y7 = (75, 150)
x8, y8 = (75, 225)
x9, y9 = (150, 0)
x10, y10 = (150, 75)
x11, y11 = (150, 150)
x12, y12 = (150, 225)
x13, y13 = (225, 0)
x14, y14 = (225, 75)
x15, y15 = (225, 150)


emt, emty = 225, 225

while True:

    clock.tick(60)

    screen.fill(back_color)

    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            x_change = 0
            if event.key == pygame.K_LEFT:
            
                    if (x15-75, y15) == (emty, emt):
                        print(emty)
                        emty = emty+75
                        y_change = -75
                        x15=x15-75
            elif event.key == pygame.K_RIGHT:
                    if (x15+75, y15) == (emty, emt):
                        print(emty)
                        emty = emty-75
                        x_change = 75
                        x15=x15+75
                    else:
                        x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        if event.type == pygame.KEYDOWN:
            y_change = 0
            if event.key == pygame.K_UP:
            
                    if (y15-75, x15) == (emt, emty):
                        print(emt)
                        y_change = -75
                        emt = emt+75
                        y15 = y15-75
            elif event.key == pygame.K_DOWN:
                    if (y15+75, x15) == (emt, emty):
                        emt = emt-75
                        y_change = 75
                        y15 = y15+75
                        print(emt)
                    else:
                        y_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
        if event.type == pygame.KEYDOWN:
            x_change = 0
            if event.key == pygame.K_LEFT:
            
                    if (x14-75, y14) == (emty, emt):
                        print(emty)
                        emty = emty+75
                        y_change = -75
                        x14=x14-75
            elif event.key == pygame.K_RIGHT:
                    if (x14+75, y14) == (emty, emt):
                        print(emty)
                        emty = emty-75
                        x_change = 75
                        x14=x14+75
                    else:
                        x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        if event.type == pygame.KEYDOWN:
            y_change = 0
            if event.key == pygame.K_UP:
            
                    if (y14-75, x14) == (emt, emty):
                        print(emt)
                        y_change = -75
                        emt = emt+75
                        y14 = y14-75
            elif event.key == pygame.K_DOWN:
                    if (y14+75, x14) == (emt, emty):
                        emt = emt-75
                        y_change = 75
                        y14 = y14+75
                        print(emt)
                    else:
                        y_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
        if event.type == pygame.KEYDOWN:
            x_change = 0
            if event.key == pygame.K_LEFT:
            
                    if (x13-75, y13) == (emty, emt):
                        print(emty)
                        emty = emty+75
                        y_change = -75
                        x13=x13-75
            elif event.key == pygame.K_RIGHT:
                    if (x13+75, y13) == (emty, emt):
                        print(emty)
                        emty = emty-75
                        x_change = 75
                        x13=x13+75
                    else:
                        x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        if event.type == pygame.KEYDOWN:
            y_change = 0
            if event.key == pygame.K_UP:
            
                    if (y13-75, x13) == (emt, emty):
                        print(emt)
                        y_change = -75
                        emt = emt+75
                        y13 = y13-75
            elif event.key == pygame.K_DOWN:
                    if (y13+75, x13) == (emt, emty):
                        emt = emt-75
                        y_change = 75
                        y13 = y13+75
                        print(emt)
                    else:
                        y_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0

        if event.type == pygame.KEYDOWN:
            x_change = 0
            if event.key == pygame.K_LEFT:
            
                    if (x12-75, y12) == (emty, emt):
                        print(emty)
                        emty = emty+75
                        y_change = -75
                        x12=x12-75
            elif event.key == pygame.K_RIGHT:
                    if (x12+75, y12) == (emty, emt):
                        print(emty)
                        emty = emty-75
                        x_change = 75
                        x12=x12+75
                    else:
                        x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        if event.type == pygame.KEYDOWN:
            y_change = 0
            if event.key == pygame.K_UP:
            
                    if (y12-75, x12) == (emt, emty):
                        print(emt)
                        y_change = -75
                        emt = emt+75
                        y12 = y12-75
            elif event.key == pygame.K_DOWN:
                    if (y12+75, x12) == (emt, emty):
                        emt = emt-75
                        y_change = 75
                        y12 = y12+75
                        print(emt)
                    else:
                        y_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
        if event.type == pygame.KEYDOWN:
            x_change = 0
            if event.key == pygame.K_LEFT:
            
                    if (x11-75, y11) == (emty, emt):
                        print(emty)
                        emty = emty+75
                        y_change = -75
                        x11=x11-75
            elif event.key == pygame.K_RIGHT:
                    if (x11+75, y11) == (emty, emt):
                        print(emty)
                        emty = emty-75
                        x_change = 75
                        x11=x11+75
                    else:
                        x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        if event.type == pygame.KEYDOWN:
            y_change = 0
            if event.key == pygame.K_UP:
            
                    if (y11-75, x11) == (emt, emty):
                        print(emt)
                        y_change = -75
                        emt = emt+75
                        y11 = y11-75
            elif event.key == pygame.K_DOWN:
                    if (y11+75, x11) == (emt, emty):
                        emt = emt-75
                        y_change = 75
                        y11 = y11+75
                        print(emt)
                    else:
                        y_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
        if event.type == pygame.KEYDOWN:
            x_change = 0
            if event.key == pygame.K_LEFT:
            
                    if (x10-75, y10) == (emty, emt):
                        print(emty)
                        emty = emty+75
                        y_change = -75
                        x10=x10-75
            elif event.key == pygame.K_RIGHT:
                    if (x10+75, y10) == (emty, emt):
                        print(emty)
                        emty = emty-75
                        x_change = 75
                        x10=x10+75
                    else:
                        x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        if event.type == pygame.KEYDOWN:
            y_change = 0
            if event.key == pygame.K_UP:
            
                    if (y10-75, x10) == (emt, emty):
                        print(emt)
                        y_change = -75
                        emt = emt+75
                        y10 = y10-75
            elif event.key == pygame.K_DOWN:
                    if (y10+75, x10) == (emt, emty):
                        emt = emt-75
                        y_change = 75
                        y10 = y10+75
                        print(emt)
                    else:
                        y_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
        if event.type == pygame.KEYDOWN:
            x_change = 0
            if event.key == pygame.K_LEFT:
            
                    if (x9-75, y9) == (emty, emt):
                        print(emty)
                        emty = emty+75
                        y_change = -75
                        x9=x9-75
            elif event.key == pygame.K_RIGHT:
                    if (x9+75, y9) == (emty, emt):
                        print(emty)
                        emty = emty-75
                        x_change = 75
                        x9=x9+75
                    else:
                        x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        if event.type == pygame.KEYDOWN:
            y_change = 0
            if event.key == pygame.K_UP:
            
                    if (y9-75, x9) == (emt, emty):
                        print(emt)
                        y_change = -75
                        emt = emt+75
                        y9 = y9-75
            elif event.key == pygame.K_DOWN:
                    if (y9+75, x9) == (emt, emty):
                        emt = emt-75
                        y_change = 75
                        y9 = y9+75
                        print(emt)
                    else:
                        y_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
        if event.type == pygame.KEYDOWN:
            x_change = 0
            if event.key == pygame.K_LEFT:
            
                    if (x8-75, y8) == (emty, emt):
                        print(emty)
                        emty = emty+75
                        y_change = -75
                        x8=x8-75
            elif event.key == pygame.K_RIGHT:
                    if (x8+75, y8) == (emty, emt):
                        print(emty)
                        emty = emty-75
                        x_change = 75
                        x8=x8+75
                    else:
                        x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        if event.type == pygame.KEYDOWN:
            y_change = 0
            if event.key == pygame.K_UP:
            
                    if (y8-75, x8) == (emt, emty):
                        print(emt)
                        y_change = -75
                        emt = emt+75
                        y8 = y8-75
            elif event.key == pygame.K_DOWN:
                    if (y8+75, x8) == (emt, emty):
                        emt = emt-75
                        y_change = 75
                        y8 = y8+75
                        print(emt)
                    else:
                        y_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
        if event.type == pygame.KEYDOWN:
            x_change = 0
            if event.key == pygame.K_LEFT:
            
                    if (x7-75, y7) == (emty, emt):
                        print(emty)
                        emty = emty+75
                        y_change = -75
                        x7=x7-75
            elif event.key == pygame.K_RIGHT:
                    if (x7+75, y7) == (emty, emt):
                        print(emty)
                        emty = emty-75
                        x_change = 75
                        x7=x7+75
                    else:
                        x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        if event.type == pygame.KEYDOWN:
            y_change = 0
            if event.key == pygame.K_UP:
            
                    if (y7-75, x7) == (emt, emty):
                        print(emt)
                        y_change = -75
                        emt = emt+75
                        y7 = y7-75
            elif event.key == pygame.K_DOWN:
                    if (y7+75, x7) == (emt, emty):
                        emt = emt-75
                        y_change = 75
                        y7 = y7+75
                        print(emt)
                    else:
                        y_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
        if event.type == pygame.KEYDOWN:
            x_change = 0
            if event.key == pygame.K_LEFT:
            
                    if (x6-75, y6) == (emty, emt):
                        print(emty)
                        emty = emty+75
                        y_change = -75
                        x6=x6-75
            elif event.key == pygame.K_RIGHT:
                    if (x6+75, y6) == (emty, emt):
                        print(emty)
                        emty = emty-75
                        x_change = 75
                        x6=x6+75
                    else:
                        x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        if event.type == pygame.KEYDOWN:
            y_change = 0
            if event.key == pygame.K_UP:
            
                    if (y6-75, x6) == (emt, emty):
                        print(emt)
                        y_change = -75
                        emt = emt+75
                        y6 = y6-75
            elif event.key == pygame.K_DOWN:
                    if (y6+75, x6) == (emt, emty):
                        emt = emt-75
                        y_change = 75
                        y6 = y6+75
                        print(emt)
                    else:
                        y_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
        if event.type == pygame.KEYDOWN:
            x_change = 0
            if event.key == pygame.K_LEFT:
            
                    if (x5-75, y5) == (emty, emt):
                        print(emty)
                        emty = emty+75
                        y_change = -75
                        x5=x5-75
            elif event.key == pygame.K_RIGHT:
                    if (x5+75, y5) == (emty, emt):
                        print(emty)
                        emty = emty-75
                        x_change = 75
                        x5=x5+75
                    else:
                        x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        if event.type == pygame.KEYDOWN:
            y_change = 0
            if event.key == pygame.K_UP:
            
                    if (y5-75, x5) == (emt, emty):
                        print(emt)
                        y_change = -75
                        emt = emt+75
                        y5 = y5-75
            elif event.key == pygame.K_DOWN:
                    if (y5+75, x5) == (emt, emty):
                        emt = emt-75
                        y_change = 75
                        y5 = y5+75
                        print(emt)
                    else:
                        y_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0

        if event.type == pygame.KEYDOWN:
            x_change = 0
            if event.key == pygame.K_LEFT:
            
                    if (x4-75, y4) == (emty, emt):
                        print(emty)
                        emty = emty+75
                        y_change = -75
                        x4=x4-75
            elif event.key == pygame.K_RIGHT:
                    if (x4+75, y4) == (emty, emt):
                        print(emty)
                        emty = emty-75
                        x_change = 75
                        x4=x4+75
                    else:
                        x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        if event.type == pygame.KEYDOWN:
            y_change = 0
            if event.key == pygame.K_UP:
            
                    if (y4-75, x4) == (emt, emty):
                        print(emt)
                        y_change = -75
                        emt = emt+75
                        y4 = y4-75
            elif event.key == pygame.K_DOWN:
                    if (y4+75, x4) == (emt, emty):
                        emt = emt-75
                        y_change = 75
                        y4 = y4+75
                        print(emt)
                    else:
                        y_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
    
        if event.type == pygame.KEYDOWN:
            x_change = 0
            if event.key == pygame.K_LEFT:
            
                    if (x3-75, y3) == (emty, emt):
                        print(emty)
                        emty = emty+75
                        y_change = -75
                        x3=x3-75
            elif event.key == pygame.K_RIGHT:
                    if (x3+75, y3) == (emty, emt):
                        print(emty)
                        emty = emty-75
                        x_change = 75
                        x3=x3+75
                    else:
                        x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        if event.type == pygame.KEYDOWN:
            y_change = 0
            if event.key == pygame.K_UP:
            
                    if (y3-75, x3) == (emt, emty):
                        print(emt)
                        y_change = -75
                        emt = emt+75
                        y3 = y3-75
            elif event.key == pygame.K_DOWN:
                    if (y3+75, x3) == (emt, emty):
                        emt = emt-75
                        y_change = 75
                        y3 = y3+75
                        print(emt)
                    else:
                        y_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
        if event.type == pygame.KEYDOWN:
            x_change = 0
            if event.key == pygame.K_LEFT:
            
                    if (x2-75, y2) == (emty, emt):
                        print(emty)
                        emty = emty+75
                        y_change = -75
                        x2=x2-75
            elif event.key == pygame.K_RIGHT:
                    if (x2+75, y2) == (emty, emt):
                        print(emty)
                        emty = emty-75
                        x_change = 75
                        x2=x2+75
                    else:
                        x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        if event.type == pygame.KEYDOWN:
            y_change = 0
            if event.key == pygame.K_UP:
            
                    if (y2-75, x2) == (emt, emty):
                        print(emt)
                        y_change = -75
                        emt = emt+75
                        y2 = y2-75
            elif event.key == pygame.K_DOWN:
                    if (y2+75, x2) == (emt, emty):
                        emt = emt-75
                        y_change = 75
                        y2 = y2+75
                        print(emt)
                    else:
                        y_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
        if event.type == pygame.KEYDOWN:
            x_change = 0
            if event.key == pygame.K_LEFT:
            
                    if (x1-75, y1) == (emty, emt):
                        print(emty)
                        emty = emty+75
                        y_change = -75
                        x1=x1-75
            elif event.key == pygame.K_RIGHT:
                    if (x1+75, y1) == (emty, emt):
                        print(emty)
                        emty = emty-75
                        x_change = 75
                        x1=x1+75
                    else:
                        x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        if event.type == pygame.KEYDOWN:
            y_change = 0
            if event.key == pygame.K_UP:
            
                    if (y1-75, x1) == (emt, emty):
                        print(emt)
                        y_change = -75
                        emt = emt+75
                        y1 = y1-75
            elif event.key == pygame.K_DOWN:
                    if (y1+75, x1) == (emt, emty):
                        emt = emt-75
                        y_change = 75
                        y1 = y1+75
                        print(emt)
                    else:
                        y_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0

    screen.blit(b_img1, (x1, y1))
    screen.blit(b_img2, (x2, y2))
    screen.blit(b_img3, (x3, y3))
    screen.blit(b_img4, (x4, y4))
    screen.blit(b_img5, (x5, y5))
    screen.blit(b_img6, (x6, y6))
    screen.blit(b_img7, (x7, y7))
    screen.blit(b_img8, (x8, y8))
    screen.blit(b_img9, (x9, y9))
    screen.blit(b_img10, (x10, y10))
    screen.blit(b_img11, (x11, y11))
    screen.blit(b_img12, (x12, y12))
    screen.blit(b_img13, (x13, y13))
    screen.blit(b_img14, (x14, y14))
    screen.blit(b_img15, (x15, y15))

    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()


    pygame.display.update()