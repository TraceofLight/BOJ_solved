# 평범한 배낭 2

import sys
from math import log2, floor

input = sys.stdin.readline

# 물건 갯수, 최대 무게 입력
stuff_number, max_weight = map(int, input().split())

# 현재 무게에 따른 만족도 리스트 선언
weight_satisfaction = [0 for _ in range(max_weight + 1)]

# 물건 정보 입력
stuff_list = []
for _ in range(stuff_number):
    weight, satisfaction, amount = map(int, input().split())

    # 해당 물품에 대하여 낱개의 형태로 변경하되 고르는 경우에 따라서 모든 갯수를 반영할 수 있도록 리스트에 추가 
    while amount:
        now_amount = amount // 2 + amount % 2
        stuff_list.append([weight * now_amount, satisfaction * now_amount])
        amount -= now_amount

# 모든 물건에 대해서 조사
for add_weight, add_satisfaction in stuff_list:

    # 기존값의 중복 반영을 막기 위한 역순 조사
    for now_weight in range(max_weight + 1, -1, -1):

        # 최대 무게를 넘지 않는 경우에 대해서만 확인
        if now_weight + add_weight <= max_weight:

            # 해당 무게를 사용한 기존 만족도보다 지금 확인하는 이 물건을 사용한 경우 만족도가 더 높다면 갱신
            weight_satisfaction[now_weight + add_weight] = max(
                weight_satisfaction[now_weight + add_weight]
                , weight_satisfaction[now_weight] + add_satisfaction
            )

# 최대 무게에서의 만족도를 확인
print(weight_satisfaction[max_weight])
