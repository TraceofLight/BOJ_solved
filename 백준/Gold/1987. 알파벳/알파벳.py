# 알파벳

import sys

input = sys.stdin.readline

# 가로, 세로 정보 입력
height, width = map(int, input().split())

# 보드 리스트 선언 및 아스키 값으로 환산된 정보 입력
board = []
for _ in range(height):
    board.append(list(map(lambda x: ord(x) - 65, input())))

# 결과값 변수 선언
result = 0

# 델타 탐색 리스트 선언
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 깊이 탐색을 진행할 스택 선언
progress_stack = []

# 초기값 입력
progress_stack.append(((0, 0), 1, [False for _ in range(26)]))

while progress_stack:

    # 현재 지점 정보 pop
    now_idx, now_moved, now_alphabet = progress_stack.pop()
    now_y, now_x = now_idx

    # 기존 최대치보다 크다면 갱신
    if result < now_moved:
        result = now_moved

    # 현재 알파벳 지나감 처리
    now_alphabet[board[now_y][now_x]] = True

    # 다음 좌표에 대해서 조사
    for direction in directions:

        # x, y 성분 분해 후 다음 좌표 반영
        move_y, move_x = direction
        next_y = move_y + now_y
        next_x = move_x + now_x

        # 리스트 범위를 벗어나지 않는 경우에 한해서만 조사
        if 0 <= next_y < height and 0 <= next_x < width:

            # 처음 지나가는 알파벳의 경우
            if not now_alphabet[board[next_y][next_x]]:

                # 알파벳 정보 복사
                next_alphabet = now_alphabet[:]

                # 다음 좌표 스택에 추가
                progress_stack.append(((next_y, next_x), now_moved + 1, next_alphabet))

# 출력
print(result)
