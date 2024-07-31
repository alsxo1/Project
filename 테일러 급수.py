import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# 심볼릭 변수 x 정의
x = sp.Symbol('x')

def Tayler(fx):
    # 함수 fx의 첫 번째 미분을 계산
    f_prime = sp.diff(fx, x)
    # 사용자로부터 테일러 급수의 차수(depth)를 입력받음
    i = int(input("뎁스를 입력하세요: "))
    # 테일러 급수의 초기 값 gx를 0으로 설정
    gx = 0 * x
    # 사용자로부터 테일러 급수를 전개할 중심점 z 값을 입력받음
    z = int(input("z 값을 입력하세요: "))
    
    # fx가 무한대 또는 정의되지 않은 점을 피하기 위해 z 값을 조정
    while True:
        if str(fx.evalf(subs={x: z}))[-2:] == "oo":  # fx가 무한대일 때
            z += 1
        elif str(fx.evalf(subs={x: z})) == "nan":  # fx가 NaN일 때
            z += 1
        else:
            break
    
    # 테일러 급수의 첫 항은 함수 fx의 z에서의 값
    gx += fx.evalf(subs={x: z})
    for t in range(1, i + 1):
        # z에서의 미분 값 계산
        value = f_prime.evalf(subs={x: z})
        # 테일러 급수의 계수 계산
        c = value / factorial_recursive(t)
        # 테일러 급수의 t차 항을 gx에 추가
        gx += c * (x-z) ** t
        print(gx)
        # 다음 차수의 미분을 계산
        f_prime = sp.diff(f_prime, x)

    # 사용자로부터 비교할 x값을 입력받음
    check = input("비교할 x값을 입력해 주세요: ")

    try:
        # 입력값이 숫자인지 확인
        check = float(check)
    except ValueError:
        # 숫자가 아닌 경우 문자열로 처리
        check = str(check)

    # 비교할 x값에서 원래 함수 fx와 테일러 급수 gx의 값 출력
    print(f"fx : {fx.evalf(subs={x: check})} \ngx : {gx.evalf(subs={x: check})}")

    return gx

def factorial_recursive(n):
    # 팩토리얼을 재귀적으로 계산하는 함수
    return n * factorial_recursive(n - 1) if n > 1 else 1

# gx 계산, 여기서 sp.sin(x)를 사용하는 예시
gx = Tayler(sp.sin(x))
