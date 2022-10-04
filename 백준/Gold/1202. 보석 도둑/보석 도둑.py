# 보석 도둑

import sys
from heapq import heappop, heappush

input = sys.stdin.readline


# 보석 갯수 및 가방의 갯수 입력
jewel_number, bag_number = map(int, input().split())

# 보석 정보를 담을 리스트 선언
item_que = []

# 보석 정보 입력
for _ in range(jewel_number):
    heappush(item_que, list(map(int, input().split())))

# 가방 정보를 담을 큐 선언
bag_list = []

# 가방 정보 입력
for _ in range(bag_number):
    bag_list.append(int(input()))

# 가방 크기 정렬
bag_list.sort()

# 남은 가방 갯수 카운터 선언
bag_left = bag_number

# 보석 가격 최댓값 변수 선언
total_price = 0

# 무게 조건을 통과한 보석 정보를 담을 우선순위 큐 선언
values = []

# 모든 가방에 대해 확인
for now_bag_limit in bag_list:

    # 보석이 있는 동안 확인
    while item_que:

        # 최저 무게에서부터 확인
        now_weight, now_price = item_que[0]

        # 현재 한도로 충분하다면 계속 확인하면서 보석 가치 큐에 추가
        if now_bag_limit >= now_weight:
            heappush(values, -now_price)
            heappop(item_que)

        # 그렇지 않다면 큐에 담는 것이 불가능
        else:
            break

    # 담을 보석이 존재한다면 가방에 담고 다음 순회
    if values:
        total_price -= heappop(values)
        continue

# 결과 출력
print(total_price)
