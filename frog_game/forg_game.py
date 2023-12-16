import pygame
import os 
import random
##############################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init() 

game_font = pygame.font.Font(None, 40)
# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

game_font=pygame.font.Font(None,40)
# 화면 타이틀 설정
pygame.display.set_caption("frog game") # 게임 이름 

#FPS
clock = pygame.time.Clock()
##################################################################


#1. 사용제 기임 초기화 (배경 화면, 게임 이미지 , 좌표,속도, 폰트 등)
 
current_path = os.path.dirname(__file__)

images_path = os.path.join(current_path,"images")

background = pygame.image.load(os.path.join(images_path,"background.png"))      # 배경


character = pygame.image.load(os.path.join(images_path,"character.png"))        # 캐릭터 
character_size = character.get_rect().size     
character_height = character_size[1]        
character_width = character_size[0]         
characters = [{"character_x_pos":screen_width/2-character_width/2,
               "character_y_pos" : screen_height-character_height}]


seats = []

seat = pygame.image.load(os.path.join(images_path,"seat.png"))

for x in range(5):
    seats.append({"seat_x_pos":150*x,"seat_y_pos":80})

cars = []
for x in range(1,6):
        cars.append({"car_x_pos":random.randint(0,640),"car_y_pos":360+40*(x-1),"car_speed":random.randint(10,15),"car_img_idx":x-1})


car = pygame.image.load(os.path.join(images_path,"car.png"))

car_imgs = [pygame.image.load(os.path.join(images_path,"car1.png")),
            pygame.image.load(os.path.join(images_path,"car2.png")),
            pygame.image.load(os.path.join(images_path,"car3.png")),
            pygame.image.load(os.path.join(images_path,"car4.png")),
            pygame.image.load(os.path.join(images_path,"car5.png"))]

remove_seat = []

logs = []

for x in range(5):
    for y in range(3):
        logs.append({"log_x_pos":0+160*y+30*y,"log_y_pos":120+40*x,"log_speed":(5*(x%2)+10)-(((5*(x%2)+10)*2)*(x%2)),"log_img_idx":x%2})

log_imgs = [pygame.image.load(os.path.join(images_path,"log.png")),pygame.image.load(os.path.join(images_path,"turtle.png"))]
log = pygame.image.load(os.path.join(images_path,"log.png"))

life = 3

to_x = 0
to_y = 0
running = True

is_ride = False

log_speed = 0


total_time =100
start_ticks = pygame.time.get_ticks()

game_result = "game over"

while running:
    dt = clock.tick(15)#게임화면의 초당 프레임 수

    #2.이벤트 처리 (키보드 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
        
        if event.type == pygame.KEYDOWN:#키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:# 캐릭터를 왼쪽으로
                to_x -=20
            elif event.key == pygame.K_RIGHT:#캐릭터를 오른쪽으로
                to_x+=20
            elif event.key == pygame.K_UP:#캐릭터를 위로
                to_y-=20
            elif event.key == pygame.K_DOWN:
                to_y+=20
        if event.type ==pygame.KEYUP:#방향키를 때면 멈춤
            if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x=0
            elif event.key ==pygame.K_UP or event.key == pygame.K_DOWN:
                to_y=0


    # 3. 게임 캐릭터 위치 정의 
    for idx,val in enumerate(characters):

        x_pos = val["character_x_pos"] 
        y_pos = val["character_y_pos"]
        if is_ride == True:
            val["character_x_pos"] += to_x+log_speed
            val["character_y_pos"] += to_y
        else:
            
            val["character_x_pos"] += to_x
            val["character_y_pos"] += to_y

        if  val["character_x_pos"]< 0:
            val["character_x_pos"] = 0
        if  val["character_x_pos"]> screen_width- character_width:
            val["character_x_pos"] = screen_width- character_width
            if is_ride == True:
                is_ride = False
                life-=1
                val["character_x_pos"] = screen_width/2-character_width/2
                val["character_y_pos"] = screen_height-character_height
        if  val["character_y_pos"]< 0:
            val["character_y_pos"] = 0
        if val["character_y_pos"] > screen_height - character_height:
            val["character_y_pos"] = screen_height - character_height

        if 280>=val["character_y_pos"]>=120:
            if is_ride == False:
                life -=1
                val["character_x_pos"] = screen_width/2-character_width/2
                val["character_y_pos"] = screen_height-character_height
    for idx,val in enumerate(cars):

        val["car_x_pos"]=val["car_x_pos"]+val["car_speed"]
        if val["car_x_pos"] > screen_width:
            val["car_x_pos"] = 0-80
    for idx,val in enumerate(logs):

        val["log_x_pos"]=val["log_x_pos"]+val["log_speed"]
        if val["log_x_pos"] > screen_width:
            val["log_x_pos"] = 0-160
        if val["log_x_pos"] < 0-160:
            val["log_x_pos"] = screen_width

    #4.충돌 처리

    for idx,val in enumerate(seats):
        if idx in remove_seat:
            continue
        now_idx = idx
        seat_rect = seat.get_rect()
        seat_rect.left = val["seat_x_pos"]
        seat_rect.top = val["seat_y_pos"]
        
        for idx,val in enumerate(characters):



            
            character_rect = character.get_rect()
            character_rect.left = val["character_x_pos"]
            character_rect.top = val["character_y_pos"]

            if character_rect.colliderect(seat_rect):
                characters.remove(val)
                remove_seat.append(now_idx)
                
                characters.append({"character_x_pos":screen_width/2-character_width/2,
               "character_y_pos" : screen_height-character_height})
                if len(remove_seat)== 5:
                    running = False
                    game_result = "success"
                break
            elif val["character_y_pos"] <= 80:
                life -= 1
                val["character_x_pos"] = screen_width/2-character_width/2
                val["character_y_pos"] = screen_height
    for idx,val in enumerate(cars):
        car_rect = car.get_rect()
        car_rect.left = val["car_x_pos"]
        car_rect.top = val["car_y_pos"]
        for idx,val in enumerate(characters):



            
            character_rect = character.get_rect()
            character_rect.left = val["character_x_pos"]
            character_rect.top = val["character_y_pos"]

            if character_rect.colliderect(car_rect):
                life -= 1
                val["character_x_pos"] = screen_width/2-character_width/2
                val["character_y_pos"] = screen_height-character_height
    for idx,val in enumerate(logs):
        log_rect = log.get_rect()
        log_rect.left = val["log_x_pos"]
        log_rect.top = val["log_y_pos"]
        log_speed = val["log_speed"]

        
        for idx,val in enumerate(characters):



            
            character_rect = character.get_rect()
            character_rect.left = val["character_x_pos"]
            character_rect.top = val["character_y_pos"]

            if character_rect.colliderect(log_rect):
                is_ride = True
                break
            else:
                is_ride = False

        else:
            continue
        break

    if life <= 0:
        running = False
    #5.화면에 그리기
    screen.blit(background,(0,0))
    for idx,val in enumerate(seats):
        if idx in remove_seat:
            screen.blit(character,(val["seat_x_pos"],val["seat_y_pos"]))
            continue

        screen.blit(seat,(val["seat_x_pos"],val["seat_y_pos"]))
    for idx,val in enumerate(cars):
        screen.blit(car_imgs[val["car_img_idx"]],(val["car_x_pos"],val["car_y_pos"]))
    for idx,val in enumerate(logs):
        screen.blit(log_imgs[val["log_img_idx"]],(val["log_x_pos"],val["log_y_pos"]))

    for idx,val in enumerate(characters):
        screen.blit(character,(val["character_x_pos"],val["character_y_pos"]  ))
    lives = game_font.render(f"lives : {life}", True,(255,255,255))
    screen.blit(lives,(10,10))
    elapsed_time = (pygame.time.get_ticks()-start_ticks) / 1000
    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True,(255,255,255))
    screen.blit(timer,(500,10))

    if total_time - elapsed_time <=0:
        game_result = "Time Over"
        running = False
    pygame.display.update()
# pygame 종료


msg = game_font.render(game_result, True,(255,0,0))#노란색
msg_rect = msg.get_rect(center = (int(screen_width/2),int(screen_height/2)))
screen.blit(msg,msg_rect)
pygame.display.update()

pygame.time.delay(2000)

pygame.quit() 

