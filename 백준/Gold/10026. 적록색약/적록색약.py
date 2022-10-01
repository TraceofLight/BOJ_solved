# 적록색약

import sys

input = sys.stdin.readline


# 2차원 리스트를 조사하고 영역의 갯수를 반환하는 함수 선언
def check_area(matrix: list, length: int) -> int:

    # 델타 탐색을 위한 리스트 선언
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    # 영역의 갯수를 카운팅할 변수 선언
    area_count = 0

    # 깊이 탐색 진행을 위한 스택 선언
    progress_stack = []

    # 좌표 방문 리스트 선언
    is_visited = [[False for _ in range(length)] for _ in range(length)]

    # 모든 좌표에 대하여 조사
    for y_idx in range(length):
        for x_idx in range(length):

            # 해당 좌표를 이미 방문한 경우 조사하지 않음
            if is_visited[y_idx][x_idx]:
                continue

            # 방문하지 않은 경우 방문 처리 후 깊이 탐색을 진행
            else:

                # 방문 처리 및 큐에 시작점을 추가
                is_visited[y_idx][x_idx] = True
                progress_stack.append([y_idx, x_idx])

                # 조사하는 지점의 색상 체크
                now_color = matrix[y_idx][x_idx]

                # 깊이 탐색
                while progress_stack:

                    # 조사 대상 좌표 pop
                    now_y, now_x = progress_stack.pop()

                    # 주변 좌표에 대해 조사
                    for direction in directions:
                        move_y, move_x = direction

                        # 다음 좌표 변수 선언
                        next_y = now_y + move_y
                        next_x = now_x + move_x

                        # 리스트 범위를 벗어나지 않는 인덱스값에 대해서만 확인
                        if 0 <= next_y < length and 0 <= next_x < length:

                            # 이미 방문한 경우는 조사하지 않음
                            if not is_visited[next_y][next_x]:

                                # 다음 좌표가 같은 색상인 경우에만 방문 처리하고 큐에 추가
                                if matrix[next_y][next_x] == now_color:
                                    is_visited[next_y][next_x] = True
                                    progress_stack.append([next_y, next_x])

                # 깊이 탐색을 전부 진행했다면 영역 갯수 1 추가
                area_count += 1

    # 영역 갯수를 반환
    return area_count


# 그리드의 한 변 길이 입력
width = int(input())

# 정상적인 그림 정보를 담을 리스트 선언
picture = list()

# 그림 정보 입력
for _ in range(width):
    picture.append(list(input().rstrip('\n')))

# 적록색약인 사람이 보게 될 그림 정보를 담을 리스트 선언
wrong_picture = [[None for _ in range(width)] for _ in range(width)]

# 잘못된 그림 정보 입력
for y_idx in range(width):
    for x_idx in range(width):

        # 청색의 경우 그대로 입력
        if picture[y_idx][x_idx] == 'B':
            wrong_picture[y_idx][x_idx] = 'B'

        # 녹색과 적색의 경우 색상 하나로 통일
        else:
            wrong_picture[y_idx][x_idx] = 'G'

# 함수를 호출하여 정상적인 영역의 갯수와 잘못된 영역의 갯수 도출
correct_area = check_area(picture, width)
wrong_area = check_area(wrong_picture, width)

# 결과 출력
print(correct_area, wrong_area)
