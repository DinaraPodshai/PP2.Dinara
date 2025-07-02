import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((1440, 1080)) #игровое окно размером 1440×1080 пикселей.
clock = pygame.time.Clock() #управления частотой кадров (FPS).

bg = pygame.image.load('clock.jpeg')

lf = pygame.image.load('sec.png')
rg = pygame.image.load('min.png')


def blitRotate(image, pos, angle,wh,hh):  #Это ключевая функция: она поворачивает стрелку относительно нужной точки
#image — изображение стрелки. pos — координаты центра часов. angle — угол поворота. wh, hh — размеры изображения стрелки.

    box = [pygame.math.Vector2(p) for p in [(0, 0), (wh, 0), (wh, -hh), (0, -hh)]]

    box_rotate = [p.rotate(angle) for p in box]

    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    origin = (pos[0] + min_box[0], pos[1] - max_box[1])

    rotated_image = pygame.transform.rotate(image, angle)
    screen.blit(rotated_image, origin)


w, h = lf.get_size()
w2, h2 = rg.get_size() #ширину и высоту

angle = 0
done = False
while not done: #Цикл, пока программа не завершится.
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                 done = True
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True #авершает
    angle = datetime.datetime.now().second/60 * 360
    ang = datetime.datetime.now().minute/60 * 360 #угол

    pos = (screen.get_width()/2, screen.get_height()/2)
    
    
    screen.blit(bg,(0,0)) #фон
    blitRotate(lf, pos, -angle +145,w,h)
    blitRotate(rg, pos, -ang +145,w2,h2)#вращаем стрелки
    angle += 1

    
    
    pygame.draw.circle(screen, (232,34,51), pos, 20, 0)

    pygame.display.flip()#обновляем экран
    
pygame.quit()
exit()