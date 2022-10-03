# 치킨 배달

import sys
from itertools import combinations

input = sys.stdin.readline


# 두 점의 좌표를 받으면 치킨거리를 반환하는 함수 선언
def chicken_distance(spot1: tuple, spot2: tuple) -> int:
    spot_1_y, spot_1_x = spot1
    spot_2_y, spot_2_x = spot2

    return abs(spot_1_y - spot_2_y) + abs(spot_1_x - spot_2_x)


# INF 선언
INF = 2000000000

# 도시의 길이 및 남길 치킨집 갯수 input
city_side, left_number = map(int, input().split())

# 좌표 정보를 남길 리스트 선언
store_info = []
house_info = []

# 집과 치킨집의 좌표를 기록
for y_idx in range(city_side):

    # 가로 한 줄씩 입력
    row = list(map(int, input().split()))

    # 모든 좌표에 대해 조사
    for x_idx in range(city_side):

        # 집의 위치 기록
        if row[x_idx] == 1:
            house_info.append((y_idx, x_idx))

        # 치킨집의 위치 기록
        elif row[x_idx] == 2:
            store_info.append((y_idx, x_idx))

# 현재 치킨집의 갯수 변수 선언
store_amount = len(store_info)

# 최소 치킨 거리 변수 선언
min_chicken_distance = INF

# 도시의 치킨집 중에서 남길 치킨집 갯수만큼 남긴 조합에 대해서 조사
for store_combination in combinations(store_info, left_number):

    # 치킨거리 합산 변수 선언
    sum_distance = 0

    # 반복문 탈출용 Flag 선언
    is_not_promising = False

    # 각 가정에 대해서 치킨집까지의 최소거리를 구한 후 합산
    for house_point in house_info:

        # 치킨집까지의 최소 거리를 나타내는 변수 선언
        min_distance = INF

        # 모든 치킨집에 대하여 치킨거리를 연산
        for each_store in store_combination:

            # 함수를 호출하여 결과 확인
            now_distance = chicken_distance(house_point, each_store)

            # 기존 최소값보다 작다면 갱신
            if now_distance < min_distance:
                min_distance = now_distance

        # 전체 치킨거리에 합산
        sum_distance += min_distance

        # 이미 기존 최소값을 넘어선 경우 하지 않기 때문에 다음 순회 진행
        if sum_distance > min_chicken_distance:
            is_not_promising = True
            break

    # Flag를 활용하여 다음 순회로 이동
    if is_not_promising:
        continue

    # 기존 최소값보다 작은 경우 갱신
    elif sum_distance < min_chicken_distance:
        min_chicken_distance = sum_distance

# 결과값 출력
print(min_chicken_distance)
