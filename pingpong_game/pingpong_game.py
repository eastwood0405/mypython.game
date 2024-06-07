
import pygame
import os
##############################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init() 

# 화면 크기 설정
screen_width = 900 # 가로 크기
screen_height = 500 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("게임 이름") # 게임 이름 

#FPS
clock = pygame.time.Clock()
##################################################################


#1. 사용제 기임 초기화 (배경 화면, 게임 이미지 , 좌표,속도, 폰트 등)
 
current_path = os.path.dirname(__file__)
images_path = os.path.join(current_path,"images")
background = pygame.image.load(os.path.join(images_path,"background.png"))


gukhim = pygame.image.load(os.path.join(images_path,"gukhim.png"))
gukhim_size = gukhim.get_rect().size  
gukhim_height = gukhim_size[1]        
gukhim_width = gukhim_size[0]         
gukhim_x_pos = 0
gukhim_y_pos = screen_height/2-gukhim_height/2

gukhim_to_y = 0


minjudang= pygame.image.load(os.path.join(images_path,"minjudang.png"))
minjudang_size = minjudang.get_rect().size  
minjudang_height = minjudang_size[1]        
minjudang_width = minjudang_size[0]         
minjudang_x_pos = screen_width - minjudang_width
minjudang_y_pos = screen_height/2-minjudang_height/2

minjudang_to_y = 0

ball= pygame.image.load(os.path.join(images_path,"ball.png"))
ball_size = ball.get_rect().size  
ball_height = ball_size[1]        
ball_width = ball_size[0]         
ball_x_pos = screen_width/2 -ball_width/2
ball_y_pos = screen_height/2-ball_height/2

ball_to_x = 10
ball_to_y = 10



 
running = True
while running:
    dt = clock.tick(30)#게임화면의 초당 프레임 수

    #2.이벤트 처리 (키보드 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                minjudang_to_y = -10
            elif event.key == pygame.K_DOWN:
                minjudang_to_y = 10
            if  event.key == pygame.K_w:
                gukhim_to_y = -10
            elif event.key == pygame.K_s:
                gukhim_to_y = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                minjudang_to_y = 0

            if event.key == pygame.K_w or event.key == pygame.K_s:
                gukhim_to_y = 0

        


    # 3. 게임 캐릭터 위치 정의 
    gukhim_y_pos += gukhim_to_y
    minjudang_y_pos += minjudang_to_y
    ball_x_pos += ball_to_x
    ball_y_pos += ball_to_y
    if gukhim_y_pos <= 0:
        gukhim_y_pos = 0
    if gukhim_y_pos >= screen_height - gukhim_height:
        gukhim_y_pos = screen_height - gukhim_height
    if minjudang_y_pos <= 0:
        minjudang_y_pos = 0
    if minjudang_y_pos >= screen_height - minjudang_height:
        minjudang_y_pos = screen_height - minjudang_height
    
        

    #4.충돌 처리
    ball_rect = ball.get_rect()
    ball_rect.left = ball_x_pos
    ball_rect.top = ball_y_pos

    gukhim_rect = gukhim.get_rect()
    gukhim_rect.left = gukhim_x_pos
    gukhim_rect.top = gukhim_y_pos

    
    minjudang_rect = minjudang.get_rect()
    minjudang_rect.left = minjudang_x_pos
    minjudang_rect.top = minjudang_y_pos
    if ball_rect.colliderect(gukhim_rect):
        ball_to_x *= -1
        ball_to_y *= -1
    elif ball_rect.colliderect(minjudang_rect):
        ball_to_x *= -1
        ball_to_y *= -1



    #5.화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(gukhim,(gukhim_x_pos,gukhim_y_pos))
    screen.blit(minjudang,(minjudang_x_pos,minjudang_y_pos))
    screen.blit(ball,(ball_x_pos,ball_y_pos))
    pygame.display.update()
# pygame 종료
pygame.quit()   