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

game_font=pygame.font.Font(None,40)
# 화면 타이틀 설정
pygame.display.set_caption("snake game") # 게임 이름 

#FPS
clock = pygame.time.Clock()
##################################################################


#1. 사용제 기임 초기화 (배경 화면, 게임 이미지 , 좌표,속도, 폰트 등)
 
current_path = os.path.dirname(__file__)

images_path = os.path.join(current_path,"images")

background = pygame.image.load(os.path.join(images_path,"background.png"))      # 배경

character = pygame.image.load(os.path.join(images_path,"character.png"))        # 캐릭터 머리
character_size = character.get_rect().size     
character_height = character_size[1]        
character_width = character_size[0]         
character_x_pos = 0
character_y_pos = 0


character_body_img =  pygame.image.load(os.path.join(images_path,"character_body.png"))  # 캐릭터 몸통
character_body = []
for num in range(3,0,-1):
    character_body.append({"character_body_x_pos":character_x_pos - num* character_width,
                   "character_body_y_pos":character_y_pos})
character_body.append({"character_body_x_pos":character_x_pos,
                       "character_body_y_pos":character_y_pos})


apple_num = 0       # 사과 수

apple =pygame.image.load(os.path.join(images_path,"apple.png"))        # 사과
apple_size = apple.get_rect().size
apple_height = apple_size[1]
apple_width = apple_size[0]
apple_x_pos = random.randrange(0,640-apple_width+1,40)
apple_y_pos = random.randrange(0,640-character_height+1,40)

text = "Game Over"
to_x = 0
to_y = 0
running = True
while running:
    dt = clock.tick(10)#게임화면의 초당 프레임 수

    #2.이벤트 처리 (키보드 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:# 캐릭터를 왼쪽으로
                if to_x == 0:#오른쪽 후 바로 왼쪽 x
                    if character_x_pos !=0 or character_y_pos != 0:
                        to_x = character_width * -1
                to_y = 0
            elif event.key == pygame.K_RIGHT:#캐릭터를 오른쪽으로
                if to_x == 0:#왼쪽 후 바로 오른쪽 x
                    to_x = character_width
                to_y = 0
            elif event.key == pygame.K_UP:#캐릭터를 위로
                if to_y== 0:#아래 후 바로 위 x
                    if character_x_pos !=0 or character_y_pos !=0:
                        to_y = character_height * -1
                to_x = 0
            elif event.key == pygame.K_DOWN:
                if to_y== 0:#위 후 바로 아래 x
                    to_y = character_height
                to_x = 0
                
    # 3. 게임 캐릭터 위치 정의 
    character_x_pos += to_x
    character_y_pos += to_y
    if to_x != 0 or to_y != 0:
        for idx,val in enumerate(character_body):#몸통 좌표를 한칸씩 앞으로
            if idx != len(character_body)-1:
            
                character_body[idx]["character_body_x_pos"] = character_body[idx+1]["character_body_x_pos"]
                character_body[idx]["character_body_y_pos"] = character_body[idx+1]["character_body_y_pos"]

    character_body[len(character_body)-1]["character_body_x_pos"] = character_x_pos
    character_body[len(character_body)-1]["character_body_y_pos"] = character_y_pos
    #가로 경계값 처리
    if character_x_pos < 0 :
        running = False
    elif character_x_pos > screen_width - character_width:
        running = False
    #세로 경계값 처리
    if character_y_pos < 0:
        running = False
    elif character_y_pos > screen_height - character_height:
        running = False
    if len(character_body) == int(256/3):#캐릭터 넓이가 화면 넓이의 1/3이면 성공
        text = "Mission Complete"
        running = False

    #4.충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    apple_rect = apple.get_rect()
    apple_rect.left = apple_x_pos
    apple_rect.top = apple_y_pos
    if character_rect.colliderect(apple_rect):#사과 충돌

        character_body.insert(0,{"character_body_x_pos":character_x_pos-to_x,
                                       "character_body_y_pos":character_y_pos-to_y})
        apple_num+=1
            
        apple_x_pos = random.randrange(0,640-apple_width+1,40)
        apple_y_pos = random.randrange(0,640-character_height+1,40)
        for idx,val in enumerate(character_body):#몸통 충돌 처리
            val_rect = character_body_img.get_rect()
            val_rect.left = val["character_body_x_pos"]
            val_rect.top = val["character_body_y_pos"]
            apple_rect = apple.get_rect()
            apple_rect.left = apple_x_pos
            apple_rect.top = apple_y_pos
            if apple_rect.colliderect(val_rect):
                apple_x_pos = random.randrange(0,640-apple_width+1,40)
                apple_y_pos = random.randrange(0,640-character_height+1,40)
                continue

    for idx,val in enumerate(character_body):#몸통 충돌 처리
        if idx == len(character_body)-1:
            continue
        val_rect = character_body_img.get_rect()
        val_rect.left = val["character_body_x_pos"]
        val_rect.top = val["character_body_y_pos"]
        if character_rect.colliderect(val_rect):
            running = False 
    apple_count = game_font.render(f"apple:{apple_num}",True,(200,0,0))
    #5.화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(apple_count,(500,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(apple,(apple_x_pos,apple_y_pos))
    for idx,val in enumerate(character_body):
        if idx == len(character_body)-1:
            continue
        screen.blit(character_body_img,(val["character_body_x_pos"],val["character_body_y_pos"]))
    pygame.display.update()


msg =game_font.render(text,True,(255,255,0))
msg_rect = msg.get_rect(center = (int(screen_width/2),int(screen_height/2)))#text
screen.blit(msg,msg_rect)
pygame.display.update()

pygame.time.delay(2000)
print(f"최종 사과 수 : {apple_num}")
# pygame 종료
pygame.quit()   