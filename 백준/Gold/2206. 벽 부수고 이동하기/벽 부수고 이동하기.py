# 벽 부수고 이동하기

import sys
from collections import deque

input = sys.stdin.readline

# INF 설정
INF = 2000000000

# 맵의 가로, 세로 입력
height, width = map(int, input().split())

# 지형 정보 입력
map_info = []
for _ in range(height):
    map_info.append(list(map(lambda x: int(x), input().rstrip('\n'))))

# 최단 경로 변수 선언
result = INF

# 너비 탐색을 위한 큐와 방문 리스트 선언
progress_que = deque()
is_visited =[[[False for _ in range(width)] for _ in range(height)] for _ in range(2)]

# 초기값 입력 및 방문 처리
progress_que.append([0, 0, 0, 1])
is_visited[0][0][0] = True

# 델타 탐색 리스트 선언
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 너비 탐색 진행
while progress_que:

    # 벽 부숨 여부 및 현재 위치, 이동 거리 확인
    is_break, now_y, now_x, counter = progress_que.popleft()

    # 목적지에 도착한 경우 최단거리를 결과값으로 변경
    if now_y == height - 1 and now_x == width - 1:
        result = counter
        break

    # 현재 위치에서 이동 가능한 좌표에 대해 조사
    for direction in directions:

        # 다음 좌표 확인
        move_y, move_x = direction
        next_y, next_x = now_y + move_y, now_x + move_x

        # 맵 범위를 넘지 않는 경우만 확인
        if 0 <= next_y < height and 0 <= next_x < width:

            # 해당 좌표에 벽이 없을 경우
            if not map_info[next_y][next_x]:

                # 아직 방문하지 않았다면 이동 후 재귀함수 호출을 통해 추가 확인
                if not is_visited[is_break][next_y][next_x]:
                    is_visited[is_break][next_y][next_x] = True
                    progress_que.append([is_break, next_y, next_x, counter + 1])

            # 해당 좌표에 벽이 있고 아직 뚫지 않은 경우
            if not is_break and map_info[next_y][next_x]:

                # 아직 방문한 적이 없는 경우 이동 후 재귀함수 호출을 통해 추가 확인
                if not is_visited[1][next_y][next_x]:
                    is_visited[1][next_y][next_x] = True
                    progress_que.append([1, next_y, next_x, counter + 1])

# 도착하지 못한 경우 -1 출력
if result == INF:
    print(-1)

# 도착한 경우 최단거리값을 출력
else:
    print(result)
