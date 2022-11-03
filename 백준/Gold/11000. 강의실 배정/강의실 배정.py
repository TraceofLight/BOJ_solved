# 강의실 배정

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

# 강의 갯수 입력
class_number = int(input())

# 강의 정보를 heapque에 입력, 정렬 시간 최소화
class_time_que = []
for _ in range(class_number):
    heappush(class_time_que, list(map(int, input().split())))

# 각 강의실별 종료 시간을 담은 리스트 선언
class_rooms = [0]

# 조건에 따른 기본 강의실 갯수 최소 1개
class_room_count = 1

# 모든 강의에 대해서 체크
while class_time_que:

    # 현재 강의들 중 가장 빨리 시작해서 빨리 끝나는 강의 pop
    start_time, end_time = heappop(class_time_que)

    # 가장 빨리 사용 가능한 강의실 체크 
    now_class_end_time = heappop(class_rooms)

    # 수용할 수 있는 강의실이라면 해당 강의실에 추가
    if now_class_end_time <= start_time:
        heappush(class_rooms, end_time)

    # 현재 강의실에 추가할 수 없다면 강의실을 추가
    else:
        heappush(class_rooms, end_time)
        heappush(class_rooms, now_class_end_time)
        class_room_count += 1

# 결과 출력
print(class_room_count)
