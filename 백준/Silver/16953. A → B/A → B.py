# A → B

import sys
from collections import deque

# 시작점, 도착점 input
start_number, end_number = map(int, sys.stdin.readline().split())
# 끝점에 도달했는지 확인하는 Flag 선언
is_got_ans = False

# 도착점과 연산횟수를 큐에 추가
progress_que = deque([])
progress_que.append([end_number, 1])

# BFS 
# 역산 시 케이스가 갈라지지 않고 1개의 경우마다 1개의 케이스가 input
# 따로 방문 기록 리스트가 필요하지 않고 시작점보다 밑으로 가면 불가능한 케이스 
while progress_que:
    now_number, counter = progress_que.popleft()
    # 일의 자리가 1일 때
    if now_number % 10 == 1:
        # 오른쪽에서 1을 제거한 값에 대하여 조사
        if now_number // 10 > start_number:
            progress_que.append([now_number // 10, counter + 1])
        # 시작점에 도달했다면 출력 후 반복문 break
        elif now_number // 10 == start_number:
            is_got_ans = True
            print(counter + 1)
            break
    # 일의 자리가 1이 아닐 때
    else:
        # 1이 아닌 홀수인 경우 배제
        if not now_number % 2:
            # 2로 나눈 값에 대하여 조사
            if now_number // 2 > start_number:
                progress_que.append([now_number // 2, counter + 1])
            # 시작점에 도달했다면 출력 후 반복문 break
            elif now_number // 2 == start_number:
                is_got_ans = True
                print(counter + 1)
                break

# 도달하지 못했다면 -1 출력
if not is_got_ans:
    print(-1)
