import pygame
#게임 초기화
pygame.init()

#창 생성
SCREEN_WIDTH=600
SCREEN_HEIGHT=400
SCREEN_SIZE=(SCREEN_WIDTH,SCREEN_HEIGHT)
win=pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("PYGAME")

#변수 초기화
running =True

#게임 루프
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #그리기
    win.fill('black')
    r1=pygame.Rect(50,50,100,100)
    pygame.draw.rect(win,'aqua',r1)

    #원그리기
    pygame.draw.circle(win,'yellow',(300,300),50)

    #타원 그리기
    pygame.draw.ellipse(win,'red',r1)

    #다각형 그리기
    pygame.draw.polygon(win,'green',[(300,200),(350,150),(250,100)])

    #화면 업데이트
    pygame.display.update()



#게임 종료
pygame.quit()