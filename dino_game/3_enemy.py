import pygame
import os
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
start_ticks = pygame.time.get_ticks()#처음시간
game_font = pygame.font.Font(None, 40)
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
enemy =  pygame.image.load(os.path.join(images_path,"enemy.png"))
enemy_size = enemy.get_rect().size
enemy_hight = enemy_size[1]
enemy_width = enemy_size[0]
enemy_x_pos = screen_width
enemy_y_pos = screen_height- stage_hight-enemy_hight
speed= -15
running = True
jumping = False
enemy_speed = -10
while running:
    dt = clock.tick(15)#게임화면의 초당 프레임 수
    #2.이벤트 처리 (키보드 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if character_y_pos == screen_height - stage_hight - character_hight:
                    speed = -15
                    jumping = True
    # 3. 게임 캐릭터 위치 정의
        
    if jumping == True:
            
        character_y_pos +=speed
        speed+=3                                            
    if character_y_pos >= screen_height - stage_hight - character_hight:
        character_y_pos = screen_height - stage_hight - character_hight
        jumping = False
    enemy_x_pos += enemy_speed
    if enemy_x_pos < 0:
        enemy_x_pos = screen_width
    #4.충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos       
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    if character_rect.colliderect(enemy_rect):
        running = False
    elapsed_time = (pygame.time.get_ticks()- start_ticks) / 100   
    timer = game_font.render(str(int(elapsed_time)),True, (204,0,209))
    #5.화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(stage,(0,screen_height-stage_hight))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    screen.blit(timer, (screen_width-50,0))                
    pygame.display.update()
# pygame 종료
pygame.quit()                 