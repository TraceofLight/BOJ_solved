# 빙산

import sys

input = sys.stdin.readline

height, width = map(int, input().split())

glacier_info = []

for _ in range(height):
    glacier_info.append(list(map(int, input().split())))


def melting_glacier(map_info: list, height: int = height, width: int = width) -> list:
    '''
    빙하가 녹는 것을 반영한 새로운 빙산 정보를 반환하는 함수
    '''

    # 반환할 리스트 및 델타 탐색 리스트 선언
    new_matrix = [[None for _ in range(width)] for _ in range(height)]
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # 모든 좌표에 대해 체크
    for y_idx in range(height):
        for x_idx in range(width):

            # 이미 전부 녹은 지형이라면 그대로 0을 입력
            if not map_info[y_idx][x_idx]:
                new_matrix[y_idx][x_idx] = 0

            # 녹은 지형이 아닐 경우
            else:

                # 녹는 정도를 카운팅할 변수 선언
                year_counter = 0

                # 4방위 전체 조사
                for direction in directions:

                    # 주변에 전부 녹은 지형이 존재한다면 1씩 카운팅
                    move_y, move_x = direction
                    near_y, near_x = y_idx + move_y, x_idx + move_x

                    if 0 <= near_y < height and 0 <= near_x < width:
                        if not map_info[near_y][near_x]:
                            year_counter += 1

                # 현 위치의 지형을 0이 될 때까지 혹은 카운터 갯수만큼 만큼 녹임
                new_matrix[y_idx][x_idx] = max(0, map_info[y_idx][x_idx] - year_counter)

    # 새로운 배열 반환
    return new_matrix

def check_seperate(map_info: list, height: int = height, width: int = width) -> bool:
    '''
    배열 내 빙산의 갯수를 반환하는 함수
    '''

    # 빙산 갯수 카운팅 변수 선언
    glacier_counter = 0

    # 방문 기록 리스트, DFS 진행을 위한 스택, 델타 탐색 리스트 선언
    is_visited = [[False for _ in range(width)] for _ in range(height)]
    progress_stack = []
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # 모든 좌표에 대해서 확인
    for y_idx in range(height):
        for x_idx in range(width):

            # 이미 다 녹았거나 방문한 지형에 대해서는 조사하지 않음
            if not map_info[y_idx][x_idx] or is_visited[y_idx][x_idx]:
                continue

            # 방문하지 않았고 아직 얼음이 남은 경우
            else:

                # 방문 처리 및 스택에 추가
                is_visited[y_idx][x_idx] = True
                progress_stack.append((y_idx, x_idx))

                # Depth First Search

                while progress_stack:
                    now_y, now_x = progress_stack.pop()

                    for direction in directions:

                        move_y, move_x = direction
                        next_y, next_x = now_y + move_y, now_x + move_x

                        if 0 <= next_y < height and 0 <= next_x < width:

                            if not is_visited[next_y][next_x]:
                                if map_info[next_y][next_x]:

                                    is_visited[next_y][next_x] = True
                                    progress_stack.append((next_y, next_x))

                # 깊이 탐색을 통해 연결된 빙하 전부 방문 처리 후 빙하 갯수 카운팅
                glacier_counter += 1

    # 빙하가 2개 이상인 경우 두 덩어리 이상으로 분리되었으므로 True 반환
    if glacier_counter >= 2:
        return True

    # 그렇지 않을 경우 False 반환
    else:
        return False

def is_all_melt(map_info: list, height: int = height, width: int = width) -> bool:
    '''
    빙산이 다 녹았는지 확인 후 T / F를 반환하는 함수
    '''

    # 남은 지형이 하나라도 존재한다면 False 반환
    for y_idx in range(height):
        for x_idx in range(width):

            if map_info[y_idx][x_idx]:
                return False

    # 다 녹았다면 True 반환
    return True


# 빙하가 녹은 시간을 카운팅하는 변수 선언
year_counter = 0

while True:

    # 1 카운팅하면서 함수를 호출하여 반환된 값을 빙하 녹인 값으로 갱신
    glacier_info = melting_glacier(glacier_info)
    year_counter += 1

    # 다 녹았다면 0 출력 후 종료
    if is_all_melt(glacier_info):
        print(0)
        break

    # 아직 다 녹지 않았지만 두 덩어리 이상이 되었다면 카운팅한 값을 출력 후 종료
    elif check_seperate(glacier_info):
        print(year_counter)
        break

    # 다 녹지 않았으며 아직 한 덩어리인 경우 계속 반복
    else:
        continue
