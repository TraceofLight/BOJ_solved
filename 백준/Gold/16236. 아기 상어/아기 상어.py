# 아기 상어

import sys
from collections import deque

# 공간 너비 input
width = int(sys.stdin.readline())

# 공간 정보 input
matrix = []
for _ in range(width):
    matrix.append(list(map(int, sys.stdin.readline().rstrip('\n').split())))

# 공간 내 물고기 정보 체크
fish = 0
fish_data = deque([])
for y_idx in range(width):
    for x_idx in range(width):
        # 일반 물고기일 경우 리스트에 추가
        if str(matrix[y_idx][x_idx]) in '123456':
            fish_data.append([matrix[y_idx][x_idx], y_idx, x_idx, 0])
            fish += 1
        # 상어 좌표인 경우 스타트 지점으로 지정 후 일반 공간으로 변경
        elif matrix[y_idx][x_idx] == 9:
            start_point = [y_idx, x_idx]
            matrix[y_idx][x_idx] = 0


# 목적지까지 가능 최단경로를 찾는 함수 선언
def bfs_way(start_point, end_point, width):
    # 4방위 1칸 이동 리스트 선언
    directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    # 목적지로 작은 물고기 위치 설정
    now_y, now_x = end_point
    # 방문기록 리스트 선언
    is_visited = [
        [False for _ in range(width)] for _ in range(width)]
    # BFS 초기값 설정
    progress_que = deque([])
    progress_que.append([start_point, 0])
    is_visited[start_point[0]][start_point[1]] = True
    while progress_que:
        [now_point_y, now_point_x], time = progress_que.popleft()
        for direction in directions:
            y_move, x_move = direction
            next_point_y, next_point_x = now_point_y + y_move, now_point_x + x_move
            if (  # 공간 범위를 벗어나지 않고
                next_point_y >= 0 and next_point_y < width and next_point_x >= 0 and next_point_x < width
            ) and (  # 크기가 비슷하거나 작아서 통과할 수 있고
                matrix[next_point_y][next_point_x] <= fish_level
            ) and (  # 지금까지 방문한 적이 없는 경우에 대해서 큐에 추가
                not is_visited[next_point_y][next_point_x]
            ):
                progress_que.append(
                    [[next_point_y, next_point_x], time + 1])
                # 방문 기록 체크
                is_visited[next_point_y][next_point_x] = True
                # 목적지에 도착했다면 시간 반환
                if is_visited[now_y][now_x]:
                    return time + 1
    # 갈 수 없는 상황이라면 inf를 반환
    return float('inf')

# 전체 생선 리스트를 먹는 순서에 적합하도록 정렬하는 함수 선언 (최단 경로 함수를 사용)
def sort_fish(fish_list: deque, point):
    for each_fish in fish_list:
        value, y_index_now, x_index_now, *args = each_fish
        end_point = [y_index_now, x_index_now]
        each_fish[3] = bfs_way(point, end_point, width)
    # 거리, y좌표, x좌표, 크기순으로 정렬
    result = deque(sorted(fish_list, key=lambda x: (x[3], x[1], x[2], x[0])))
    return result


# 전체 걸린 시간 변수 선언
total_second = 0

# 물고기가 처음부터 없다면 0 출력
if not fish:
    print(0)
# 아니라면 과정 수행
else:
    # 초기 변수들 선언
    fish_level = 2
    counter = 0
    extra_fish = deque([])
    last_data = []
    # 남아있는 생선이 있다면 반복
    while fish_data or extra_fish:
        fish_data = fish_data + extra_fish
        extra_fish = deque([])
        # 생선 리스트를 함수를 통해 정렬
        fish_data = sort_fish(fish_data, start_point)
        # 시작점이 바뀌지 않았다면 더 이상 먹을 수 없었다는 것을 의미하므로 종료
        if last_data == start_point:
            break
        # 변화가 있었다면 다음 변화 확인을 위해 시작점 백업
        else:
            last_data = start_point
        while fish_data:
            this_fish = fish_data.popleft()
            value, now_y, now_x, distance = this_fish
            # 현재 크기가 지금 물고기의 크기보다 크거나 같다면 먹을 수 없음
            if value >= fish_level:
                extra_fish.append(this_fish)
                continue
            # 먹을 수 있는 작은 물고기라면 거리 조건을 확인
            else:
                # 이동이 가능한 거리라면 먹고 카운트, 크기가 늘어날 조건이면 카운트 초기화 및 크기 1 추가
                # 도착점을 시작점으로 변경
                if distance != float('inf'):
                    counter += 1
                    if counter == fish_level:
                        fish_level += 1
                        counter = 0
                    start_point = [now_y, now_x]
                    total_second += distance
                    break
                # 먹지 못했다면 아직 먹을 수 없는 리스트에 올려두고 조금 먼 물고기에 대해서 탐색
                else:
                    extra_fish.append(this_fish)
                    continue

    # 결과값 출력
    print(total_second)
