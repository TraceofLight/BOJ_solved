# 치즈

import sys

input = sys.stdin.readline

# 모눈종이 가로, 세로 길이 input
height, width = map(int, input().split())

# 치즈 정보를 기록할 리스트 선언
cheese_spot = []

# 치즈가 위치한 좌표 정보 input
for y_idx in range(height):
    cheese_spot.append(list(map(int, input().split())))


# 바깥 공기를 전부 2로 변경하는 함수 선언
def change_air(matrix:list, y_length: int, x_length: int):
    # 델타 탐색 4방위 리스트 선언
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    # DFS 활용
    progress_stack = []
    progress_stack.append((0, 0))
    is_visited = [[False for _ in range(x_length)] for _ in range(y_length)]
    matrix[0][0] = 2
    is_visited[0][0] = True
    while progress_stack:
        now_point = progress_stack.pop()
        now_y, now_x = now_point
        for direction in directions:
            move_y, move_x = direction
            next_y = now_y + move_y
            next_x = now_x + move_x
            # 행렬 내에서 맞닿은 0을 2로 변경하는 과정
            if next_y >= 0 and next_y < y_length and next_x >= 0 and next_x < x_length:
                if not is_visited[next_y][next_x]:
                    if not matrix[next_y][next_x]:
                        matrix[next_y][next_x] = 2
                    if matrix[next_y][next_x] == 2:
                        is_visited[next_y][next_x] = True
                        progress_stack.append((next_y, next_x))

# 바깥 공기의 접촉이 많아지면 녹이는 함수 선언
def melting_cheese(matrix:list, y_length: int, x_length: int):
    # 델타 탐색 4방위 리스트 선언
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    # 녹은 지점을 기록할 리스트 선언
    melting_spot = []
    for now_y in range(y_length):
        for now_x in range(x_length):
            if matrix[now_y][now_x] == 1:
                check_counter = 0
                for direction in directions:
                    move_y, move_x = direction
                    next_y = now_y + move_y
                    next_x = now_x + move_x
                    if matrix[next_y][next_x] == 2:
                        check_counter += 1
                        if check_counter >= 2:
                            break
                # 맞닿은 바깥 공기면이 2개 이상이라면 녹은 지점
                if check_counter >= 2:
                    melting_spot.append([now_y, now_x])
    # 녹은 지점에 대해 바깥 공기로 일괄 변경
    for spot in melting_spot:
        spot_y, spot_x = spot
        matrix[spot_y][spot_x] = 2

# 치즈가 남았는지 확인하는 함수 선언
def left_cheese(matrix:list, y_length: int, x_length: int):
    for y_index in range(y_length):
        for x_index in range(x_length):
            if matrix[y_index][x_index] == 1:
                return True
    return False


# 초기 바깥 공기 설정
change_air(cheese_spot, height, width)

# 소요 시간 변수 선언
melt_time = 0

while True:
    # 남은 치즈가 없다면 break
    if not left_cheese(cheese_spot, height, width):
        break
    # 치즈가 남아있다면 바깥 공기랑 접촉이 많은 치즈를 녹임
    else:
        melt_time += 1
        melting_cheese(cheese_spot, height, width)
        # 안쪽 공기와 바깥 공기가 만났다면 바깥쪽 공기로 갱신
        change_air(cheese_spot, height, width)

# 결과 출력
print(melt_time)
