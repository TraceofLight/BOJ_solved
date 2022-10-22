# 동전 1

import sys

input = sys.stdin.readline

# 동전 종류 및 목표 가치 합 입력
coin_number, target_price = map(int, input().split())

# 동전 정보 입력
coin_list = []
for _ in range(coin_number):
    coin_list.append(int(input()))

# Dynamic Prgramming

# 목표 가치 이하 가치를 나타낼 수 있는 경우의 수를 담을 리스트 선언
result = [0 for _ in range(target_price + 1)]

# 0의 가치는 1가지로 표현 가능, 초기값 역할로 입력
result[0] = 1

# 모든 동전에 대해 확인
for each_coin in coin_list:

    # 모든 가격에 대해서 조사
    for each_price in range(1, target_price + 1):

        # 해당 동전의 가치를 더하지 않은 가치의 경우의 수만큼 현재 가격을 나타내는 가짓수에 포함
        if each_price - each_coin >= 0:
            result[each_price] += result[each_price - each_coin]

# 목표 가치의 경우의 수 출력
print(result[target_price])
