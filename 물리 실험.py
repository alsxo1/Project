import pygame
import sys
import math

# 초기화
pygame.init()

# 화면 설정
width, height = 800, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("파동 간섭 시뮬레이션")

# 색깔 정의
white = (255, 255, 255)
black = (0, 0, 0)

# 파동 변수 초기화
frequency = 5
wave_speed = 0.5

amplitude1 = 0

amplitude2 = 0

running_annual = True
running_auto = False

# 메인 루프
while True:
    if running_annual == True:
        while running_annual:

            amplitude_interferenced = amplitude1 + amplitude2

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(amplitude_interferenced)
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        amplitude1 -= 10
                    elif event.key == pygame.K_a:
                        amplitude2 -= 10
                    elif event.key == pygame.K_w:
                        amplitude1 += 10
                    elif event.key == pygame.K_s:
                        amplitude2 += 10
                    elif event.key == pygame.K_SPACE:
                        running_auto = True
                        running_annual = False

            screen.fill(black)

            # x축 그리기
            pygame.draw.line(screen, white, (0, height // 2), (width, height // 2), 2)
            pygame.draw.line(screen, white, (0, 750), (width, 750), 2)
            pygame.draw.line(screen, white, (0, 250), (width, 250), 2)

            # 파동 생성 및 렌더링
            for x in range(width):
                y = int(height / 2 + amplitude_interferenced * math.sin(2 * math.pi * frequency * x / width - wave_speed * pygame.time.get_ticks() / 1000))
                y1 = int(height / 2 + amplitude1 * math.sin(2 * math.pi * frequency * x / width - wave_speed * pygame.time.get_ticks() / 1000))
                y2 = int(height / 2 + amplitude2 * math.sin(2 * math.pi * frequency * x / width - wave_speed * pygame.time.get_ticks() / 1000))
                pygame.draw.circle(screen, white, (x, y), 2)
                pygame.draw.circle(screen, white, (x, y1 - 250), 2)
                pygame.draw.circle(screen, white, (x, y2 + 250), 2)

            pygame.display.flip()
    else:
        while running_auto:

            amplitude_interferenced = amplitude1 + amplitude2

            amplitude2 = -amplitude1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(amplitude_interferenced)
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        amplitude1 -= 10
                    elif event.key == pygame.K_w:
                        amplitude1 += 10
                    elif event.key == pygame.K_SPACE:
                        running_annual = True
                        running_auto = False


            screen.fill(black)

            # x축 그리기
            pygame.draw.line(screen, white, (0, height // 2), (width, height // 2), 2)
            pygame.draw.line(screen, white, (0, 750), (width, 750), 2)
            pygame.draw.line(screen, white, (0, 250), (width, 250), 2)

            # 파동 생성 및 렌더링
            for x in range(width):
                y = int(height / 2 + amplitude_interferenced * math.sin(2 * math.pi * frequency * x / width - wave_speed * pygame.time.get_ticks() / 1000))
                y1 = int(height / 2 + amplitude1 * math.sin(2 * math.pi * frequency * x / width - wave_speed * pygame.time.get_ticks() / 1000))
                y2 = int(height / 2 + amplitude2 * math.sin(2 * math.pi * frequency * x / width - wave_speed * pygame.time.get_ticks() / 1000))
                pygame.draw.circle(screen, white, (x, y), 2)
                pygame.draw.circle(screen, white, (x, y1 - 250), 2)
                pygame.draw.circle(screen, white, (x, y2 + 250), 2)

            pygame.display.flip()

        
