# 숨바꼭질 2

import sys
from collections import deque

input = sys.stdin.readline

# 수빈이와 동생의 위치 input
start_point, end_point = map(int, input().split())

# 깊이 탐색을 위한 큐 선언
progress_que = deque([])
# 수빈이 위치부터 시작하는 초기값 입력
progress_que.append([start_point, 0])

# 방문 리스트 선언
is_visited = [2000000000 for _ in range(200001)]

# 최소시간, 최소 시간 도달 방법 수 변수 선언
min_time = 2000000000
min_way_types = 1

# 깊이 탐색
while progress_que:

    # 현 지점과 지금까지 이동한 거리 확인
    now_point, move_time = progress_que.popleft()

    # 도착 지점에 도달했을 경우
    if now_point == end_point:

        # 최소값을 갱신했다면 최소 시간 도달 방법 수 1로 초기화
        if move_time < min_time:
            min_way_types = 1
            min_time = move_time

        # 아니라면 방법 수 1 카운트
        elif move_time == min_time:
            min_way_types += 1

    # 각 케이스 별로 해당 지점까지 도달하는 최단 시간을 갱신하지 못하면 pruning
    if 2 * now_point >= 0 and 2 * now_point <= 200000:
        if is_visited[2 * now_point] >= move_time:
            is_visited[2 * now_point] = move_time
            progress_que.append([2 * now_point, move_time + 1])

    if now_point + 1 >= 0 and now_point + 1 <= 200000:
        if is_visited[now_point + 1] >= move_time:
            is_visited[now_point + 1] = move_time
            progress_que.append([now_point + 1, move_time + 1])

    if now_point - 1 >= 0 and now_point - 1 <= 200000:
        if is_visited[now_point - 1] >= move_time:
            is_visited[now_point - 1] = move_time
            progress_que.append([now_point - 1, move_time + 1])

# 결과 출력
print(min_time)
print(min_way_types)
