# 피리 부는 사나이

import sys

input = sys.stdin.readline

# 지도의 높이, 너비 입력
height, width = map(int, input().split())

# 지도 탐색 방향 딕셔너리 선언
direction = {
    'U': [-1, 0],
    'D': [1, 0],
    'L': [0, -1],
    'R': [0, 1],
}

# 지도 리스트 선언 및 정보 입력
map_info = []
for _ in range(height):
    map_info.append(list(input()))

# 방문 리스트 선언
is_visited = [[False for _ in range(width)] for _ in range(height)]

# 결과값 변수 선언
safe_zone_number = 0

# 모든 좌표에 대해 조사
for y_idx in range(height):
    for x_idx in range(width):

        # 이미 조사한 값들의 경우 pass
        if is_visited[y_idx][x_idx]:
            continue

        else:

            # 시작 지점 방문 처리
            is_visited[y_idx][x_idx] = True
            
            # 깊이 탐색을 위한 스택 선언 및 초기값 입력
            progress_stack = []
            progress_stack.append(((y_idx, x_idx), set((y_idx, x_idx))))

            # 탐색 진행
            while progress_stack:

                # 이동 경로 및 현재 지점 정보 확인
                now_idx, move_log = progress_stack.pop()

                # 현재 좌표 및 다음 이동값 x, y 성분으로 분리
                now_y, now_x = now_idx
                move_y, move_x = direction[map_info[now_y][now_x]]

                # 다음 이동 좌표를 x, y 성분으로 확인
                next_y, next_x = now_y + move_y, now_x + move_x

                # 지도를 벗어나지 않는 경우
                if 0 <= next_y < height and 0 <= next_x < width:

                    # 방문하지 않은 지점이라면
                    if not is_visited[next_y][next_x]:

                        # 방문 처리 후 경로 기록 및 스택에 추가
                        is_visited[next_y][next_x] = True
                        progress_stack.append(((next_y, next_x), move_log | {(now_y, now_x)}))

                    else:

                        # 싸이클을 돌게 된 경우라면 세이프 존 하나 추가
                        if (next_y, next_x) in move_log:
                            safe_zone_number += 1

                        # 싸이클이 아니라면 다른 세이프 존에 합류 가능
                        break

                # 만약 벗어난다면 해당 지점에서 마무리
                else:
                    safe_zone_number += 1
                    break

# 결과 출력
print(safe_zone_number)
