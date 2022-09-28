# SWEA_1249 보급로

from heapq import *

# 테스트 횟수 및 출력 리스트 선언
testcase = int(input())
output = []

# 델타 탐색 리스트 선언
directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

# INF 변수 선언
INF = 2000000000

for each_case in range(testcase):

    # 지도의 크기 input
    space_range = int(input())

    # 지도 정보 input
    matrix = []
    for _ in range(space_range):
        matrix.append([int(element) for element in list(input())])

    # 좌표 해시 테이블 선언
    coord_hash = {(y_idx, x_idx): y_idx * space_range + x_idx + 1 
                for y_idx in range(space_range) 
                for x_idx in range(space_range)}

    # 그래프 딕셔너리 선언
    graph_dict = {idx: [] for idx in range(1, space_range ** 2 + 1)}

    # 모든 좌표에 대해서 그래프 정보 입력
    for now_y in range(space_range):
        for now_x in range(space_range):

            # 4방위 델타탐색
            for direction in directions:
                move_y, move_x = direction
                next_y = now_y + move_y
                next_x = now_x + move_x

                # 지도의 범위를 벗어나지 않는 경우에 대해서만 체크
                if 0 <= next_x < space_range and 0 <= next_y < space_range:

                    # 해당 좌표에서 다음 좌표로 이동했을 때 걸리는 복구 시간에 대한 정보와 다음 좌표를 입력
                    graph_dict[coord_hash[(now_y, now_x)]].append([matrix[next_y][next_x], coord_hash[(next_y, next_x)]])

    # 거리 정보를 담을 딕셔너리 선언
    time_cost = {idx: INF for idx in range(1, space_range ** 2 + 1)}

    # 초기 지점의 거리값 해당 지점의 복구 시간으로 초기화
    time_cost[1] = matrix[0][0]

    # 우선 순위 큐 선언 및 초기값 입력
    priority_que = []
    heappush(priority_que, [matrix[0][0], 1])

    # 다익스트라 알고리즘에 따라서 최소 시간 갱신
    while priority_que:

        # 현재 소모 시간과 현재 좌표 pop
        now_time_cost, now_coord = heappop(priority_que)

        # 현 지점에서 갈 수 있는 모든 지점에 대해 조사
        for next_time_cost, next_coord in graph_dict[now_coord]:

            # 현 지점을 경유해서 가는 것이 더 시간이 짧게 걸릴 경우 갱신
            if time_cost[next_coord] > time_cost[now_coord] + next_time_cost:
                time_cost[next_coord] = time_cost[now_coord] + next_time_cost

                # 갱신된 지점에 대한 확인이 필요하므로 큐에 갱신 지점 추가
                heappush(priority_que, [time_cost[next_coord], next_coord])

    # 도착 지점까지 걸린 최소 시간을 출력 리스트에 추가
    output.append(time_cost[space_range ** 2])

# 문제 조건에 따라서 출력
for output_idx in range(testcase):
    print(f'#{output_idx + 1} {output[output_idx]}')
