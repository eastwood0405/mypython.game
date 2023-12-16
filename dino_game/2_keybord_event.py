import pygame
import os
import time
##############################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init() 

# 화면 크기 설정
screen_width = 800 # 가로 크기
screen_height = 400 # 세로 크기
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
stage = pygame.image.load(os.path.join(images_path,"stage.png"))
stage_size = stage.get_rect().size
stage_hight = stage_size[1]
character =  pygame.image.load(os.path.join(images_path,"character.png"))
character_size = character.get_rect().size
character_hight = character_size[1]
character_width = character_size[0]
character_x_pos = 0
character_y_pos = screen_height- stage_hight-character_hight

speed= 0
running = True
jumping = False
while running:
    dt = clock.tick(30)#게임화면의 초당 프레임 수

    #2.이벤트 처리 (키보드 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if character_y_pos == screen_height - stage_hight - character_hight:
                    jumping = True

    # 3. 게임 캐릭터 위치 정의
        if jumping == True:
            if character_y_pos >= screen_height - stage_hight - character_hight-35:
                character_y_pos -=35
            elif character_y_pos==  screen_height - stage_hight - character_hight -70:
                character_y_pos +=70
        if character_y_pos >= screen_height - stage_hight - character_hight:
            character_y_pos = screen_height - stage_hight - character_hight
            jumping = False
        print(character_y_pos)



    #4.충돌 처리






    #5.화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(stage,(0,screen_height-stage_hight))
    screen.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update()
# pygame 종료
pygame.quit()   