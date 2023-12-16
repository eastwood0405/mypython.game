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
character_y_pos = screen_height- stage_height-character_height



enemy =  pygame.image.load(os.path.join(images_path,"enemy.png"))
enemy_size = enemy.get_rect().size
enemy_height = enemy_size[1]
enemy_width = enemy_size[0]
enemy_x_pos = screen_width
enemy_y_pos = screen_height- stage_height-enemy_height
enemy_speed= -5

speed = -24

jumping = False
running = True
text = "Game Over"
while running:
    dt = clock.tick(15)#게임화면의 초당 프레임 수
    #2.이벤트 처리 (키보드 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if character_y_pos == screen_height - stage_height - character_height:
                    speed = -24
                    jumping = True

    # 3. 게임 캐릭터 위치 정의
    if jumping ==True:
        character_y_pos+=speed
        speed+=4
    if character_y_pos > screen_height - stage_height - character_height:
        character_y_pos = screen_height - stage_height - character_height
        speed = -24
     

    enemy_x_pos += enemy_speed
    if enemy_x_pos < 0:
        enemy_x_pos = screen_width-enemy_width
    #4.충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos       
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos

    enemy_rect.top = enemy_y_pos
    if character_rect.colliderect(enemy_rect):
        running = False
    #5.화면에 그리기
    elapsed_time =(pygame.time.get_ticks()-start_ticks) /100
    timer = game_font.render(f"point:{int(elapsed_time)}",True,(0,170,0))
    if int(elapsed_time) % 100 == 0:
        enemy_speed=enemy_speed*2
    screen.blit(background,(0,0))
    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    screen.blit(timer,(650,0))
    pygame.display.update()
# pygame 종료

msg =game_font.render(text,True,(255,255,0))
msg_rect = msg.get_rect(center = (int(screen_width/2),int(screen_height/2)))
screen.blit(msg,msg_rect)
pygame.display.update()

pygame.time.delay(2000)

pygame.quit()                 