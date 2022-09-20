# 미세먼지 안녕!

import sys

input = sys.stdin.readline

# 방의 넓이, 시간 input
height, width, time = map(int, input().split())

# 방의 구조를 담을 리스트와 공기청정기 위치를 담은 리스트 선언
room = []
air_con = []

# 방 정보 input, 만약 열에 공기청정기가 있다면 해당 열을 리스트에 기록
for row in range(height):
    temp = list(map(int, input().split()))
    if temp[0] == -1:
        air_con.append(row)
    room.append(temp)

# 델타 탐색용 리스트 선언
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]


# 먼지를 확산시키는 함수 선언
def spread_dust(matrix: list, y_range, x_range, air_conditioner):

    # 새로 정보를 담을 2차원 리스트 선언
    new_matrix = [[0 for _ in range(x_range)] for _ in range(y_range)]

    # 공기청정기 위치 지정
    for y_con in air_conditioner:
        new_matrix[y_con][0] = -1

    # 전체 지점에 대해서 델타 탐색
    for y_index in range(height):
        for x_index in range(width):
            dust_amount = matrix[y_index][x_index]

            # 먼지가 없거나 공기청정기 좌표인 경우 다음 순회
            if not dust_amount or dust_amount == -1:
                continue

            # 아닐 경우 먼지의 확산
            else:
                counter = 0
                for direction in directions:
                    move_y, move_x = direction
                    next_y = y_index + move_y
                    next_x = x_index + move_x

                    # 범위 내에서 공식에 따라 확산
                    if next_y >= 0 and next_y < y_range and next_x >= 0 and next_x < x_range:
                        if new_matrix[next_y][next_x] != -1:
                            new_matrix[next_y][next_x] += dust_amount // 5
                            counter += 1

                # 확산 이후 남은 양이 기존 위치에 잔존
                new_matrix[y_index][x_index] += dust_amount - counter * (dust_amount // 5)

    # 완성된 2차원 리스트 반환
    return new_matrix

# 먼지가 바람 흐름에 따라 이동하는 함수 선언
def clear_air(matrix: list, y_range, x_range, air_conditioner):

    # 새로 정보를 담을 2차원 리스트 선언
    new_matrix = [[0 for _ in range(x_range)] for _ in range(y_range)]

    # 공기청정기 위치 지정 및 바로 앞 0 + 밀어내기
    for y_con in air_conditioner:
        new_matrix[y_con][0] = -1
        new_matrix[y_con][1] = 0
        for x_index in range(2, x_range):
            new_matrix[y_con][x_index] = matrix[y_con][x_index - 1]

    # 첫 가로줄 및 마지막 가로줄 당기기
    for x_idx in range(1, x_range):
        new_matrix[0][x_idx - 1] = matrix[0][x_idx]
    for x_idx in range(1, x_range):
        new_matrix[y_range - 1][x_idx - 1] = matrix[y_range - 1][x_idx]

    # 0번 세로줄 흡입
    for y_idx in range(1, y_range - 1):
        if y_idx < sorted(air_conditioner)[0]:
            new_matrix[y_idx][0] = matrix[y_idx - 1][0]
        if y_idx > sorted(air_conditioner)[1]:
            new_matrix[y_idx][0] = matrix[y_idx + 1][0]

    # 마지막 세로줄 상하이동
    for y_idx in range(0, sorted(air_conditioner)[0]):
        new_matrix[y_idx][x_range - 1] = matrix[y_idx + 1][x_range - 1]
    for y_idx in range(sorted(air_conditioner)[1], y_range - 1):
        new_matrix[y_idx + 1][x_range - 1] = matrix[y_idx][x_range - 1]

    # 변동 없는 칸들 그대로 잔존
    for y_idx in range(y_range):
        for x_idx in range(x_range):
            if y_idx and new_matrix[y_idx][0] != -1 and y_idx != y_range - 1:
                if x_idx != 0 and x_idx != x_range - 1:
                    new_matrix[y_idx][x_idx] = matrix[y_idx][x_idx]

    # 완성된 2차원 리스트 반환
    return new_matrix

# 전체 먼지를 합산하는 함수 선언
def sum_dust(space: list):

    # 공기 청정기 반영 기본값 2 설정
    result = 2

    # 열 합산값 가산
    for row in space:
        result += sum(row)
    
    # 결과 반환
    return result


# 선언한 함수들을 호출하여 방에 있는 미세먼지를 이동시킴
counter = 0
while counter < time:
    room = spread_dust(room, height, width, air_con)
    room = clear_air(room, height, width, air_con)
    counter += 1

# 합산 함수를 호출하여 결과 출력
print(sum_dust(room))
