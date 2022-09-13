# 1로 만들기 2

import sys
from collections import deque

# 시작 숫자 input
init_number = int(sys.stdin.readline())
# 방문 여부 기록 리스트 선언
is_visited = [False for _ in range(init_number + 1)]

# DFS로 최단거리 확인
progress_que = deque([])
# 시작점, 방문 로그, 횟수 카운터를 큐에 투입
progress_que.append([init_number, [init_number], 0])

while progress_que:
    now_number, visited, counter = progress_que.popleft()
    # 1에 가장 빠르게 도달한 값의 카운팅 횟수와 방문 로그를 출력, 반복문은 break
    if now_number == 1:
        print(counter)
        print(*visited)
        break
    # 3으로 나눠질 경우
    if not now_number % 3:
        if not is_visited[now_number // 3]:
            is_visited[now_number // 3] = True
            progress_que.append([now_number // 3, visited + [now_number // 3], counter + 1])
    # 2로 나눠질 경우
    if not now_number % 2:
        if not is_visited[now_number // 2]:
            is_visited[now_number // 2] = True
            progress_que.append([now_number // 2, visited + [now_number // 2], counter + 1])
    # 1 이상인 경우
    if now_number:
        if not is_visited[now_number - 1]:
            is_visited[now_number - 1] = True
            progress_que.append([now_number - 1, visited + [now_number - 1], counter + 1])
