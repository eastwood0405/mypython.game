import pygame
import os
import random
##############################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init() 
# 화면 크기 설정
screen_width = 800 # 가로 크기
screen_height = 400 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
# 화면 타이틀 설정
pygame.display.set_caption("공룡 게임 ") # 게임 이름 
#FPS
clock = pygame.time.Clock()
game_font=pygame.font.Font(None,40)
start_ticks = pygame.time.get_ticks()
##################################################################
#1. 사용제 기임 초기화 (배경 화면, 게임 이미지 , 좌표,속도, 폰트 등)
current_path = os.path.dirname(__file__)

images_path = os.path.join(current_path,"images")
                                                                    
background = pygame.image.load(os.path.join(images_path,"background.png"))
                                                                                                                                     
stage = pygame.image.load(os.path.join(images_path,"stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

character =  pygame.image.load(os.path.join(images_path,"character.png"))
character_size = character.get_rect().size     
character_height = character_size[1]        
character_width = character_size[0]         
character_x_pos = 0
character_y_pos = screen_height/2-character_height/2



speed = 0

max_enemy_num = 3


jumping = False

running = True

enemy_speed = -10

text = "Game Over"
while running:
    dt = clock.tick(15)#게임화면의 초당 프레임 수
    #2.이벤트 처리 (키보드 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jumping = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                jumping = False
    # 3. 게임 캐릭터 위치 정의
    if jumping ==True:
        speed = -24
    character_y_pos += speed
    speed+=4
    if character_y_pos > screen_height - stage_height - character_height:
        character_y_pos = screen_height - stage_height - character_height
        running = False

        

    # For 문 종료        
        
    
    #4.충돌 처리

    #5.화면에 그리기

    
    screen.blit(background,(0,0))
    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))

    pygame.display.update()
# pygame 종료


pygame.display.update()


pygame.quit()                 

