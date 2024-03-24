import pygame
import asyncio
import math
#상수 설정
middle_x = 600 # 중심
middle_y = 500 # 중심
G = 6.6726 * (10) # 만유인력 상수

# 초기화, 세팅
pygame.init() # 초기화
black = (0, 0, 0) # 색 설정
clock = pygame.time.Clock() # frame 설정

# 화면 설정
width, height = 1200, 1000 # 가로, 세로
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("민유인력과 힘의 합력 및 분력을 활용한 행성 공전 시뮬레이션")

central_ob = pygame.image.load("C:/Users/cmt06/OneDrive/practice/pygame_basic/central_ob.png")
central_ob_size = central_ob.get_rect().size
central_ob_width = central_ob_size[0]
central_ob_height = central_ob_size[1]
central_ob_x = 450 # 중심 물체의 x
central_ob_y = 350 # 중심 물체의 y

statellite_ob = pygame.image.load("C:/Users/cmt06/OneDrive/practice/pygame_basic/statellite_ob.png")
statellite_ob_size = statellite_ob.get_rect().size
statellite_ob_width = statellite_ob_size[0]
statellite_ob_height = statellite_ob_size[1]
statellite_ob_x = 900 # 위성 물체의 x
statellite_ob_y = 900 # 위성 물체의 y

#물체의 질량 (Kg)

central_ob_weight = 1000000
satellite_ob_weight = 10

#statellite_ob의 방향 및 속도 설정 (N), ()

vector_x = -6.5 # -는 왼쪽, +는 오른쪽
vector_y = 0

# satellite_ob의 운동에너지 및 방향을 실시간으로 계산하는 비동기함수
async def physics(central_ob_weight, statellite_ob_weight, central_ob_x, central_ob_y):
    global statellite_ob_x
    global statellite_ob_y
    global vector_x
    global vector_y
    x, y = statellite_ob_x - 15.5, statellite_ob_y - 15.5

    Rx, Ry = statellite_ob_x - central_ob_x, statellite_ob_y - central_ob_y
    r = ((central_ob_x - statellite_ob_x) ** 2 + (central_ob_y - statellite_ob_y) ** 2) ** 1 / 2 # 중심 물체와 위성 물체의 거리
    degree = math.atan2(Ry, Rx) * 180 / math.pi # atan2 로 구한 두 점 사이의 각도
    F = ((G * central_ob_weight * statellite_ob_weight) / r ** 2) # 두 물체 사이 작용하는 인력
    #1사분면시 작용하는 힘의 방향 및 크기
    if  x > middle_x and y < middle_y:
        vector_x -= math.cos(math.pi * (degree / 180)) * F
        vector_y += math.sin(math.pi * (degree / 180)) * F
    #2사분면 작용하는 힘의 방향 및 크기
    if x < middle_x and y < middle_y:
        degree = 180 - abs(degree)
        vector_x += math.cos(math.pi * (degree / 180)) * F
        vector_y += math.sin(math.pi * (degree / 180)) * F
    #3사분면 작용하는 힘의 방향 및 크기
    if x < middle_x and y > middle_y:
        degree = 180 - degree
        vector_x += math.cos(math.pi * (degree / 180)) * F
        vector_y -= math.sin(math.pi * (degree / 180)) * F
    #4사분면 작용하는 힘의 방향 및 크기
    if x > middle_x and y > middle_y:
        vector_x -= math.cos(math.pi * (degree / 180)) * F
        vector_y -= math.sin(math.pi * (degree / 180)) * F
    print(vector_x, vector_y)

running = True

while running: # 실행

    screen.fill(black)

    screen.blit(screen, (0, 0)) # 스크린 그리기
    screen.blit(central_ob, (central_ob_x, central_ob_y)) # 중심물체 그리기
    screen.blit(statellite_ob, (statellite_ob_x, statellite_ob_y)) # 위성 물체 그리기

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False    
        else:
            continue

    statellite_ob_x += vector_x # x축 방향으로 이동
    statellite_ob_y += vector_y # y축 방향으로 이동

    asyncio.run(physics(central_ob_weight, satellite_ob_weight, central_ob_x, central_ob_y)) # 위 함수 실행

    clock.tick(60) # 1초에 60번 위 코드를 실행

    pygame.display.update()
