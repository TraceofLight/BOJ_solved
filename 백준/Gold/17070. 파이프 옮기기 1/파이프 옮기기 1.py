# 파이프 옮기기 1

import sys

input = sys.stdin.readline

# 이전 이동 방위에 따라 다음 탐색에 변화를 주는 델타 탐색 리스트 선언
directions = {
    (0, 1): [(0, 1), (1, 1)],
    (1, 1): [(1, 0), (0, 1), (1, 1)],
    (1, 0): [(1, 0), (1, 1)],
}

# 집의 크기 input
house_size = int(input())

# 집의 상태 input
matrix = []
for _ in range(house_size):
    matrix.append(list(map(int, input().split())))

# 결과값 변수 선언
result = 0

# 목적지가 막힌 상태면 옮길 수 없음
if matrix[house_size - 1][house_size - 1]:
    print(result)

# 아니라면 탐색
else:
    # DFS를 위한 스택 선언 및 초기값 지정 
    progress_stack = []
    progress_stack.append([(0, 1), (0, 1)])

    # 너비 탐색
    while progress_stack:

        # 현재 위치와 지난 이동 정보 pop
        now_spot, last_movement = progress_stack.pop()

        # 이동할 수 있는 모든 가짓수에 대해 조사
        for direction in directions[last_movement]:
            next_y = now_spot[0] + direction[0]
            next_x = now_spot[1] + direction[1]

            # 집 범위 안에서만 움직여야 함 (위로 이동이 없어 0 체크 x)
            if next_x < house_size and next_y < house_size:

                # 해당 칸으로 움직일 수 있는지 확인
                if not matrix[next_y][next_x]:

                    # 대각선일 경우 주변 빈 칸의 추가 확인이 필요
                    if direction == (1, 1):
                        if not matrix[next_y - 1][next_x] and not matrix[next_y][next_x - 1]:

                            # 도착 지점 도착했다면 결과값 1 추가
                            if next_y == house_size - 1 and next_x == house_size - 1:
                                result += 1

                            # 도착 지점이 아니라면 탐색 속행
                            else:
                                progress_stack.append([(next_y, next_x), direction])

                    # 대각선이 아니라면 추가 확인 필요 없음
                    else:
                        # 도착 지점 도착했다면 결과값 1 추가
                        if next_y == house_size - 1 and next_x == house_size - 1:
                            result += 1

                        # 도착 지점이 아니라면 탐색 속행
                        else:
                            progress_stack.append([(next_y, next_x), direction])

    # 결과 출력
    print(result)
