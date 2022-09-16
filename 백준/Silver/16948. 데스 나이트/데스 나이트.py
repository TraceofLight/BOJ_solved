# 데스 나이트

import sys
from collections import deque

input = sys.stdin.readline

# 체스판의 크기 input
chess_side = int(input())

# 출발점과 도착점의 정보 input
start_x, start_y, end_x, end_y = map(int, input().split())

# 나이트의 이동 방향에 대한 리스트 선언
directions_knight = [[-2, -1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]

# BFS를 진행할 큐 선언
progress_que = deque([])

# 방문 리스트 선언
is_visited = [[False for _ in range(chess_side)] for _ in range(chess_side)]

# 초기값 입력 및 방문 처리
progress_que.append([[start_y, start_x], 0])
is_visited[start_y][start_x] = True

# 결과값 변수 선언 (default -1)
result = -1

# BFS 진행
while progress_que:
    now_point, move_counter = progress_que.popleft()
    now_y, now_x = now_point
    for direction in directions_knight:
        # 반복문 탈출을 위한 Flag 생성
        is_got_ans = False
        move_x, move_y = direction
        next_x = now_x + move_x
        next_y = now_y + move_y
        if next_y >= 0 and next_y < chess_side and next_x >= 0 and next_x < chess_side:
            if not is_visited[next_y][next_x]:
                is_visited[next_y][next_x] = True
                progress_que.append([[next_y, next_x], move_counter + 1])
                # 도착점에 방문처리된 것을 확인하면 BFS 종료
                if is_visited[end_y][end_x]:
                    result = move_counter + 1
                    is_got_ans = True
                    break
    if is_got_ans:
        break

# 결과 출력
print(result)
