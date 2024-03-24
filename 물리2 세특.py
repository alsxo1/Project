import pygame
import asyncio
import math
#상수 설정
middle_x = 600
middle_y = 500
G = 6.6726 * (10)

# 초기화, 세팅
pygame.init()
black = (0, 0, 0)
clock = pygame.time.Clock()

# 화면 설정
width, height = 1200, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("민유인력과 힘의 합력 및 분력을 활용한 행성 공전 시뮬레이션")

central_ob = pygame.image.load("C:/Users/cmt06/OneDrive/practice/pygame_basic/central_ob.png")
central_ob_size = central_ob.get_rect().size
central_ob_width = central_ob_size[0]
central_ob_height = central_ob_size[1]
central_ob_x = 450
central_ob_y = 350

statellite_ob = pygame.image.load("C:/Users/cmt06/OneDrive/practice/pygame_basic/statellite_ob.png")
statellite_ob_size = statellite_ob.get_rect().size
statellite_ob_width = statellite_ob_size[0]
statellite_ob_height = statellite_ob_size[1]
statellite_ob_x = 900
statellite_ob_y = 900

#물체의 질량 (Kg)

central_ob_weight = 1000000
satellite_ob_weight = 10

#statellite_ob의 방향 및 속도 설정 (N), ()

vector_x = -6.5
vector_y = 0

# satellite_ob의 운동에너지 및 방향을 실시간으로 계산하는 비동기함수
async def physics(central_ob_weight, statellite_ob_weight, central_ob_x, central_ob_y):
    global statellite_ob_x
    global statellite_ob_y
    global vector_x
    global vector_y
    x, y = statellite_ob_x - 15.5, statellite_ob_y - 15.5

    Rx, Ry = statellite_ob_x - central_ob_x, statellite_ob_y - central_ob_y
    r = ((central_ob_x - statellite_ob_x) ** 2 + (central_ob_y - statellite_ob_y) ** 2) ** 1 / 2
    degree = math.atan2(Ry, Rx) * 180 / math.pi # atan2 로 구한 두 점 사이의 각도
    F = ((G * central_ob_weight * statellite_ob_weight) / r ** 2) # 두 물체 사이 작용하는 인력
    #1사분면
    if  x > middle_x and y < middle_y:
        vector_x -= math.cos(math.pi * (degree / 180)) * F
        vector_y += math.sin(math.pi * (degree / 180)) * F
    #2사분면
    if x < middle_x and y < middle_y:
        degree = 180 - abs(degree)
        vector_x += math.cos(math.pi * (degree / 180)) * F
        vector_y += math.sin(math.pi * (degree / 180)) * F
    #3사분면
    if x < middle_x and y > middle_y:
        degree = 180 - degree
        vector_x += math.cos(math.pi * (degree / 180)) * F
        vector_y -= math.sin(math.pi * (degree / 180)) * F
    #4사분면
    if x > middle_x and y > middle_y:
        vector_x -= math.cos(math.pi * (degree / 180)) * F
        vector_y -= math.sin(math.pi * (degree / 180)) * F
    print(vector_x, vector_y)

running = True

while running:

    screen.fill(black)

    screen.blit(screen, (0, 0))
    screen.blit(central_ob, (central_ob_x, central_ob_y))
    screen.blit(statellite_ob, (statellite_ob_x, statellite_ob_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False    
        else:
            continue

    statellite_ob_x += vector_x
    statellite_ob_y += vector_y

    asyncio.run(physics(central_ob_weight, satellite_ob_weight, central_ob_x, central_ob_y))

    clock.tick(60)

    pygame.display.update()
