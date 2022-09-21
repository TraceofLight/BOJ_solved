# 연구소

import sys
from itertools import combinations
from copy import deepcopy

input = sys.stdin.readline

# 가로 및 세로 길이 input
height, width = map(int, input().split())

# 연구소 정보와 빈 공간을 담을 리스트 선언
lab = []
blank_spot = []

# 연구소 정보 input
for row in range(height):
    temp = list(map(int, input().split()))
    for column in range(width):
        if not temp[column]:
            blank_spot.append([row, column])
    lab.append(temp)


# 빈 공간 중 3개를 골라 벽을 채운 연구소 정보를 반환하는 함수 선언
def build_wall(matrix: list, point_list: list):

    # 기존 연구소 정보 input
    new_matrix = deepcopy(matrix)

    # 리스트에 기록된 지점들 전부 1로 변경
    for point in point_list:
        y_point, x_point = point
        new_matrix[y_point][x_point] = 1

    # 새로운 연구소 정보 리스트 반환
    return new_matrix

# 바이러스가 퍼지는 것을 구현하는 함수 선언
def spread_virus(matrix: list, y_range: int, x_range: int):

    # 델타 탐색 리스트 선언
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    # 방문 기록 리스트 선언
    is_visited = [[False for _ in range(x_range)] for _ in range(y_range)]

    # 모든 지점에 대해서 조사
    for y_idx in range(y_range):
        for x_idx in range(x_range):

            # 이미 방문한 지점을 다시 방문하지 않음
            if is_visited[y_idx][x_idx]:
                continue

            # 해당 지점이 바이러스인 경우 움직일 수 있는 데까지 바이러스가 확산
            else:
                if matrix[y_idx][x_idx] == 2:
                    progress_stack = [[y_idx, x_idx]]
                    is_visited[y_idx][x_idx] = True

                    while progress_stack:
                        now_y, now_x = progress_stack.pop()

                        for move_y, move_x in directions:
                            next_y = now_y + move_y
                            next_x = now_x + move_x

                            if next_y >= 0 and next_y < y_range and next_x >= 0 and next_x < x_range:
                                if not matrix[next_y][next_x] or matrix[next_y][next_x] == 2:
                                    if not is_visited[next_y][next_x]:

                                        is_visited[next_y][next_x] = True
                                        matrix[next_y][next_x] = 2
                                        progress_stack.append([next_y, next_x])

# 안전한 좌표의 갯수를 확인하는 함수 선언
def safe_zone(matrix: list, y_range: int, x_range: int):

    # 안전한 지점 카운터 선언
    safe_space = 0

    for y_idx in range(y_range):
        for x_idx in range(x_range):

            # 해당 지점의 정보가 0인 경우 카운터 1 추가
            if not matrix[y_idx][x_idx]:
                safe_space += 1

    # 카운터를 반환
    return safe_space


# 최대 안전 영역 변수 선언
max_safe_zone = 0

# 현재 비어 있는 구간 중에서 임의로 3개 고른 케이스들에 대해 조사
for walls in list(combinations(blank_spot, 3)):

    # 함수들을 호출하여 문제 과정 구현
    lab_upgraded = build_wall(lab, walls)
    spread_virus(lab_upgraded, height, width)
    now_safe_zone = safe_zone(lab_upgraded, height, width)

    # 기존 안전 영역의 최대 갯수를 넘은 경우 갱신
    if max_safe_zone < now_safe_zone:
        max_safe_zone = now_safe_zone

# 결과 출력
print(max_safe_zone)
