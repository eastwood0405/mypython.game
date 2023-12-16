import pygame
import os
import random
##############################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init() 

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))


current_path = os.path.dirname(__file__)

images_path = os.path.join(current_path,"images")

background = pygame.image.load(os.path.join(images_path,"background.png"))

character = pygame.image.load(os.path.join(images_path,"character.png"))

character_x_pos = random.randrange(0,410)
character_y_pos = random.randrange(0,570)


# 화면 타이틀 설정
pygame.display.set_caption("게임 이름") # 게임 이름 

#FPS
clock = pygame.time.Clock()
##################################################################


#1. 사용제 기임 초기화 (배경 화면, 게임 이미지 , 좌표,속도, 폰트 등)
 


 
running = True
while running:
    dt = clock.tick(30)#게임화면의 초당 프레임 수

    #2.이벤트 처리 (키보드 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
        


    # 3. 게임 캐릭터 위치 정의 

    #4.충돌 처리
        if event.type == pygame.MOUSEBUTTONDOWN:
            character_rect = character.get_rect()
            character_rect.left = character_x_pos
            character_rect.top = character_y_pos

            if character_rect.collidepoint(event.pos):
                character_x_pos = random.randrange(0,410)
                character_y_pos = random.randrange(0,570)







    #5.화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))

    pygame.display.update()
# pygame 종료
pygame.quit()   