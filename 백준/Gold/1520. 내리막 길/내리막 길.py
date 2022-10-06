# 내리막 길

import sys
from heapq import *

input = sys.stdin.readline

# 가로, 세로 길이 입력
height, width = map(int, input().split())

# 지도 리스트 선언 및 정보 입력
map_info = []
for _ in range(height):
    map_info.append(list(map(int, input().split())))

# 델타 탐색 리스트 선언
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 해당 좌표까지 경우의 수를 확인하는 리스트 선언
move_log = [[None for _ in range(width)] for _ in range(height)]

# 방문 기록 리스트 선언
is_visited = [[False for _ in range(width)] for _ in range(height)]

# 출발 지점 경우의 수 1
move_log[0][0] = 1

# 탐색을 위한 우선순위 큐 선언
priority_que = []

# 높은 지대를 항상 먼저 확인할 수 있도록 입력
heappush(priority_que, (-map_info[0][0], (0, 0)))

# 결과값 변수 선언
route_counter = 0

# 깊이 탐색
while priority_que:

    # 현재 좌표 확인
    now_value, now_coord = heappop(priority_que)

    # 현재 좌표 x, y 성분으로 분리
    now_y, now_x = now_coord

    # 방문하지 않은 경우
    if not is_visited[now_y][now_x]:

        # 방문 처리
        is_visited[now_y][now_x] = True

        # 모든 방위에 대해서 조사
        for direction in directions:

            # 다음 좌표 y, x 값 확인
            move_y, move_x = direction
            next_y = now_y + move_y
            next_x = now_x + move_x

            # 지도 범위 내에서만 조사
            if 0 <= next_y < height and 0 <= next_x < width:

                # 다음 지점이 현 지점보다 작은 값일 경우
                if -now_value > map_info[next_y][next_x]:

                    # 다음 지점을 스택에 추가
                    heappush(priority_que, (-map_info[next_y][next_x], (next_y, next_x)))

                    if move_log[next_y][next_x] is None:
                        move_log[next_y][next_x] = move_log[now_y][now_x]

                    else:
                        move_log[next_y][next_x] += move_log[now_y][now_x]

# 결과 확인
result = move_log[height - 1][width - 1]

# 출력
if result is None:
    print(0)

else:
    print(result)
