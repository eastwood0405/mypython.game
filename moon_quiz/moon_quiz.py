import pygame
import os
import random
##############################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init() 
game_font = pygame.font.Font(None, 40)
game_font2 = pygame.font.Font(None, 80)
# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("you can click images") # 게임 설명

game_result = "game over"
#FPS
clock = pygame.time.Clock()
##################################################################


#1. 사용제 기임 초기화 (배경 화면, 게임 이미지 , 좌표,속도, 폰트 등)
current_path = os.path.dirname(__file__) #  현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))      #배경

hint = pygame.image.load(os.path.join(image_path,"hint.png"))   #힌트
hint_x_pos = 0
hint_y_pos = 0

moons = []

moon_images = [pygame.image.load(os.path.join(image_path, "moon1w.png")),           #달 그림들
               pygame.image.load(os.path.join(image_path, "moon2w.png")),
               pygame.image.load(os.path.join(image_path, "moon3w.png")),
               pygame.image.load(os.path.join(image_path, "moon4w.png")),
               pygame.image.load(os.path.join(image_path, "moon5w.png")),
               pygame.image.load(os.path.join(image_path, "moon6w.png")),
               pygame.image.load(os.path.join(image_path, "moon7w.png")),
               pygame.image.load(os.path.join(image_path, "moon8w.png")),]

moons.append({"moon_x_pos":96,"moon_y_pos":screen_height/2-20,"moon_img_idx":random.randint(0,7)})

for x in range(1,4):
    moons.append({"moon_x_pos":96+40*x+96*x,"moon_y_pos":screen_height/2-20,"moon_img_idx":random.randint(0,7)})
text = ""
for x in range(1,5):
    text += str(random.randint(1,8))

use_hint = 0

total_time =100
start_ticks = pygame.time.get_ticks() # 시작 시간 정의






running = True
while running:
    dt = clock.tick(30)#게임화면의 초당 프레임 수

    #2.이벤트 처리 (키보드 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for idx,val in enumerate(moons):
                moon_x_pos = val["moon_x_pos"]
                moon_y_pos = val["moon_y_pos"]
                moon_img_idx = val["moon_img_idx"]

                moon_rect = moon_images[moon_img_idx].get_rect()
                moon_rect.left = moon_x_pos
                moon_rect.top = moon_y_pos

                if moon_rect.collidepoint(event.pos):
                    val["moon_img_idx"]+=1
                    if val["moon_img_idx"] >7:
                        val["moon_img_idx"] = 0
            hint_rect = hint.get_rect()#힌트를 눌렀는지 확인
            hint_rect.left = hint_x_pos
            hint_rect.top = hint_y_pos


            
            if hint_rect.collidepoint(event.pos):#힌트를 보여줌
                    hint = pygame.image.load(os.path.join(image_path,"hint_result.png"))
                    use_hint = 1
                    

    # 3. 게임 캐릭터 위치 정의 
    for x in range(4):#달그림과 번호 맞는지 확인
        if moons[x]["moon_img_idx"] + 1 != int(text[x]):
            
            break
        if x !=3:
            continue
        running = False
        game_result = "succes"#성공시 출력 메세지(수정 가능)


    #4.충돌 처리






    #5.화면에 그리기
    screen.blit(background,(0,0))
    for idx,val in enumerate(moons):
        screen.blit(moon_images[val["moon_img_idx"]],(val["moon_x_pos"],val["moon_y_pos"]))
    msg = game_font.render(text, True,(255,255,255))
    msg_rect = msg.get_rect(center = (int(screen_width/2),int(screen_height/2-80)))
    screen.blit(msg,msg_rect)
    screen.blit(hint,(hint_x_pos,hint_y_pos))#힌트 그리기(삭제해도 가능)
    elapsed_time = (pygame.time.get_ticks()-start_ticks) / 1000
    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True,(255,255,255))
    screen.blit(timer,(500,10))

    if total_time - elapsed_time <=0:
        game_result = "Time Over"
        running = False
    pygame.display.update()
# pygame 종료


msg2 = game_font2.render(game_result, True,(255,255,255))#노란색
msg_rect2 = msg2.get_rect(center = (int(screen_width/2),int(screen_height/2)))
screen.blit(msg2,msg_rect2)

if use_hint == 1:#힌트를 썼으면 보여주는 내용
    msg3 = game_font.render("you used a hint", True,(255,255,255))#노란색
    msg_rect3 = msg3.get_rect(center = (int(screen_width/2),int(screen_height/2+80)))
    screen.blit(msg3,msg_rect3)


pygame.display.update()

pygame.time.delay(2000)
pygame.quit()