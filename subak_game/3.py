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


# 화면 타이틀 설정
pygame.display.set_caption("수박 게임") # 게임 이름 

#FPS
clock = pygame.time.Clock()
##################################################################


#1. 사용제 기임 초기화 (배경 화면, 게임 이미지 , 좌표,속도, 폰트 등)
current_path = os.path.dirname(__file__) #  현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))


fruits = []
for x in range(3):
    fruits.append({"x_pos":0,"y_pos":0,"width":40+5*x,"height":40+5*x,"bouncement":x+1,"img_idx":x,"is_fallen":False,"to_y":0,"is_screen_blit":False})
fruts_image = []
for x in range(1,12): 
    fruts_image.append(pygame.image.load(os.path.join(image_path, f"fruit{x}.png")))

to_x = 0
to_y = 0
falling = False

fruit_idx = 0

fallen_fruits = []

def Not_fallen_list_update():
    global fruits
    for idx, val in enumerate(fruits):
        if val["is_fallen"] == False:
            continue
        fallen_fruits.append(val)
        del fruits[idx]

running = True
while running:
    dt = clock.tick(30)#게임화면의 초당 프레임 수

    #2.이벤트 처리 (키보드 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fruits[fruit_idx]["is_fallen"] = False
                fruits[fruit_idx]["to_y"] = 0.5
            elif event.key == pygame.K_LEFT:
                to_x = -5
            elif event.key == pygame.K_RIGHT:
                to_x = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
        
    if falling == True:
        to_y +=0.5
        to_x = 0


    # 3. 게임 캐릭터 위치 정의 
    for idx, val in enumerate(fruits):
        if idx == fruit_idx:
            if val["is_fallen"] == False:
                val["to_y"] += 0.5

            val["x_pos"] += to_x
            val["y_pos"] += val["to_y"]
            if val["x_pos"] <= 0:
                val["x_pos"] = 0
            if val["x_pos"] >= screen_width - val["width"]:
                val["x_pos"] = screen_width - val["width"]
            if val["y_pos"] >= screen_height- val["height"]:
                val["y_pos"] = screen_height- val["height"]
                val["to_y"] = 0
                val["is_fallen"] = True


            
                val["is_fallen"] = True
                Not_fallen_list_update()
                fruits.append({"x_pos":0,"y_pos":0,"width":val["width"],"height":val["height"],
                    "bouncement":val["bouncement"],"img_idx":val["img_idx"],"is_fallen":False,"is_screen_blit":False,"to_y":0})
                fruit_idx = random.randrange(0,len(fruits)-1)
        elif val["is_fallen"] == False and val["is_screen_blit"] == True:


            val["y_pos"] += val["to_y"]
            if val["y_pos"] >= screen_height- val["height"]:
                val["y_pos"] = screen_height- val["height"]
                val["to_y"] = 0
                val["is_fallen"] = True

            
                Not_fallen_list_update()
                fruits.append({"x_pos":0,"y_pos":0,"width":val["width"],"height":val["height"],
                    "bouncement":val["bouncement"],"img_idx":val["img_idx"],"is_fallen":False,"is_screen_blit":False,"to_y":0})
                fruit_idx = random.randrange(0,len(fruits)-1)



        

    for idx, val in enumerate(fruits):

        fruit_rect = fruts_image[val["img_idx"]].get_rect()
        fruit_rect.left = val["x_pos"]
        fruit_rect.top = val["y_pos"]
        for  i,v in enumerate(fallen_fruits):

            
            fallen_fruit_rect = fruts_image[v["img_idx"]].get_rect()
            fallen_fruit_rect.left = v["x_pos"]
            fallen_fruit_rect.top = v["y_pos"]
            if fruit_rect.colliderect(fallen_fruit_rect):
                to_y = 0
                falling = False
                print(val["img_idx"],v["img_idx"])


                if val["img_idx"] == v["img_idx"]:
                    print(val["img_idx"],v["img_idx"])
                    val["img_idx"] += 1
                    val["y_pos"] = v["y_pos"]
                    val["is_fallen"] = True
                    Not_fallen_list_update()
                    fallen_fruits.remove(v)
                    if val ["y_pos"]  < screen_height- val["height"]:
                        val["is_fallen"] = False
                        

                else:
                    val["y_pos"] = v["y_pos"] - val["height"]
                    val["is_fallen"] = True
                    Not_fallen_list_update()
                fruits.append({"x_pos":0,"y_pos":0,"width":val["width"],"height":val["height"],"bouncement":val["bouncement"],"img_idx":val["img_idx"],"is_fallen":False,"is_screen_blit":False,"to_y":0})
                fruit_idx = random.randrange(0,len(fruits)-1)
                break
    







    #4.충돌 처리






    #5.화면에 그리기
    screen.blit(background,(0,0))
    for idx, val in enumerate(fruits):
        if idx == fruit_idx :
            screen.blit(fruts_image[val["img_idx"]],(val["x_pos"],val["y_pos"]))
    for idx, val in enumerate(fallen_fruits):
        screen.blit(fruts_image[val["img_idx"]],(val["x_pos"],val["y_pos"]))

    pygame.display.update()
# pygame 종료
pygame.quit()   