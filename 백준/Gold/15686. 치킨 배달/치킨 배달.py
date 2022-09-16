# 치킨 배달

import sys
from itertools import combinations

input = sys.stdin.readline

# 도시의 길이 및 남길 치킨집 갯수 input
city_side, chicken_store = map(int, input().split())

# 좌표 정보를 남길 리스트 선언
store_info = []
house_info = []

# 집과 치킨집의 좌표를 기록
for y_idx in range(city_side):
    row = list(map(int, input().split()))
    for x_idx in range(city_side):
        if row[x_idx] == 1:
            house_info.append([y_idx, x_idx])
        elif row[x_idx] == 2:
            store_info.append([y_idx, x_idx])

# 현재 치킨집의 갯수 변수 선언
store_amount = len(store_info)


# 치킨거리에 대한 함수 선언
def chicken_distance(spot1: list, spot2: list):
    return abs(spot1[0] - spot2[0]) + abs(spot1[1] - spot2[1])


# 최소 치킨 거리 변수 선언
min_chicken_distance = 2000000000

# 도시의 치킨집 중에서 남길 치킨집 갯수만큼 남긴 조합에 대해서 조사
for store_combination in combinations(range(store_amount), chicken_store):
    # 치킨 거리 합산 변수 선언
    sum_distance = 0
    # 반복문 탈출용 Flag 선언
    is_over = False
    # 각 가정에 대해서 치킨집까지의 최소거리를 구한 후 합산
    for house_point in house_info:
        min_distance = 2000000000
        for store_index in store_combination:
            now_distance = chicken_distance(house_point, store_info[store_index])
            if now_distance < min_distance:
                min_distance = now_distance
        sum_distance += min_distance
        # 이미 기존 최소값을 넘어선 경우 유망성이 없으므로 다음 순회 진행
        if sum_distance > min_chicken_distance:
            is_over = True
            break
    # 유망성이 없는 경우 Flag를 활용하여 다음 순회로 이동
    if is_over:
        continue
    # 기존 최소값보다 작은 경우 갱신
    elif sum_distance < min_chicken_distance:
        min_chicken_distance = sum_distance

# 결과값 출력
print(min_chicken_distance)
