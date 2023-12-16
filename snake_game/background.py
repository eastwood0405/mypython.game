import pygame
import os 
import random
##############################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init() 

# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 640 # 세로 크기
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
character = pygame.image.load(os.path.join(images_path,"character.png"))
character_size = character.get_rect().size     
character_height = character_size[1]        
character_width = character_size[0]         
character_x_pos = 0
character_y_pos = 0

character_body = []
for num in range(3,0,-1):
    character_body.append({"character_body_x_pos":character_x_pos - num* character_width,
                   "character_body_y_pos":character_y_pos})
character_body.append({"character_body_x_pos":character_x_pos,
                       "character_body_y_pos":character_y_pos})



apple =pygame.image.load(os.path.join(images_path,"apple.png"))
apple_size = apple.get_rect().size
apple_height = apple_size[1]
apple_width = apple_size[0]
apple_x_pos = random.randrange(0,640-apple_width+1,40)
apple_y_pos = random.randrange(0,640-character_height+1,40)

to_x = 0
to_y = 0
running = True
while running:
    dt = clock.tick(15)#게임화면의 초당 프레임 수

    #2.이벤트 처리 (키보드 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:# 캐릭터를 왼쪽으로
                if to_x == 0:
                    to_x = character_width * -1
                to_y = 0
            elif event.key == pygame.K_RIGHT:#캐릭터를 오른쪽으로
                if to_x == 0:
                    to_x = character_width
                to_y = 0
            elif event.key == pygame.K_UP:#캐릭터를 위로
                if to_y== 0:
                    to_y = character_height * -1
                to_x = 0
            elif event.key == pygame.K_DOWN:
                if to_y== 0:
                    to_y = character_height
                to_x = 0
    # 3. 게임 캐릭터 위치 정의 
    character_x_pos += to_x
    character_y_pos += to_y
    for idx,val in enumerate(character_body):
        if idx != len(character_body)-1:
            
            character_body[idx]["character_body_x_pos"] = character_body[idx+1]["character_body_x_pos"]
            character_body[idx]["character_body_y_pos"] = character_body[idx+1]["character_body_y_pos"]

    character_body[len(character_body)-1]["character_body_x_pos"] = character_x_pos
    character_body[len(character_body)-1]["character_body_y_pos"] = character_y_pos
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos =  screen_width - character_width
    #세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    #4.충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    apple_rect = apple.get_rect()
    apple_rect.left = apple_x_pos
    apple_rect.top = apple_y_pos
    if character_rect.colliderect(apple_rect):
        if character_body[0]["character_body_x_pos"] == character_x_pos:
            if character_body[0]["character_body_y_pos"] > character_y_pos:
                character_body.insert(len(character_body)-1,{"character_body_x_pos":character_x_pos,
                                       "character_body_y_pos": character_body[0]["character_body_y_pos"]+character_height})
            if character_body[0]["character_body_y_pos"] < character_y_pos:
                character_body.insert(len(character_body)-1,{"character_body_x_pos":character_x_pos,
                                       "character_body_y_pos": character_body[0]["character_body_y_pos"]-character_height})
        elif character_body[0]["character_body_y_pos"] == character_y_pos:
            if character_body[0]["character_body_x_pos"] > character_x_pos:
                character_body.insert(len(character_body)-1,{"character_body_x_pos":character_body[0]["character_body_x_pos"]+character_width,
                                       "character_body_y_pos":character_y_pos})
            if character_body[0]["character_body_x_pos"] < character_x_pos:
                character_body.insert(len(character_body)-1,{"character_body_x_pos":character_body[0]["character_body_x_pos"]-character_width,
                                       "character_body_y_pos":character_y_pos})

    #5.화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(apple,(apple_x_pos,apple_y_pos))
    for idx,val in enumerate(character_body):
        if idx == len(character_body)-1:
            continue
        screen.blit(character,(val["character_body_x_pos"],val["character_body_y_pos"]))
    pygame.display.update()
# pygame 종료
pygame.quit()   