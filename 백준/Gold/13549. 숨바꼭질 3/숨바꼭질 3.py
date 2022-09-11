# 숨바꼭질 3

import sys
from collections import deque

# 출발점과 도착점 input
start_point, end_point = map(int, sys.stdin.readline().split())

# 방문 여부 체크 리스트 선언
is_visited = [False for _ in range(200001)]

# 최단 시간 변수 선언
min_time = float('inf')

# BFS
progress_que = deque([])
progress_que.append([start_point, 0])
is_visited[start_point] = True

while progress_que:
    now_point, time = progress_que.popleft()
    # 기존 최단 시간보다 작다면 갱신
    if now_point == end_point:
        if min_time > time:
            min_time = time
    # +1, -1, *2에 대해서 방문하지 않았다면 큐에 추가
    # *2 는 시간을 소모하지 않기 때문에 항상 우선진행 후 방문 처리한다.
    if 0 <= now_point * 2 and now_point * 2 <= 200000:
        if not is_visited[now_point * 2]:
            progress_que.append([now_point * 2, time])
            is_visited[now_point * 2] = True
    if 0 <= now_point - 1 and now_point - 1 <= 200000:
        if not is_visited[now_point - 1]:
            progress_que.append([now_point - 1, time + 1])
            is_visited[now_point - 1] = True
    if 0 <= now_point + 1 and now_point + 1 <= 200000:
        if not is_visited[now_point + 1]:
            progress_que.append([now_point + 1, time + 1])
            is_visited[now_point + 1] = True

# 결과 출력
print(min_time)
