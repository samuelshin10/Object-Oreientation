import pygame
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN_SIZE= (SCREEN_WIDTH,SCREEN_HEIGHT)
win = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Pygame")
 #변수 초기화
running = True

#게임루프
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #그리기

    win.fill('black')
    #사각형 그리기
    r1=pygame.Rect(150,200,300,100)
    pygame.draw.rect(win,'white', r1)
    #원 그리기
    pygame.draw.circle(win,'yellow',(400,300),30)
    pygame.draw.circle(win,'yellow',(200,300),30)




    pygame.display.update()

pygame.quit()