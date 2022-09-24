# 타임머신

import sys

input = sys.stdin.readline

# 도시 갯수 및 간선 갯수 input
city_number, line_number = map(int, input().split())

# 관계도 딕셔너리 선언
graph = {idx: [] for idx in range(1, city_number + 1)}

# 간선 정보 input
for _ in range(line_number):
    start_city, end_city, time_cost = map(int, input().split())
    graph[start_city].append([time_cost, end_city])

# INF 변수 선언
max_val = 2000000000

# 출발지로부터 목적지까지의 시간을 기록할 딕셔너리 선언 및 INF 값으로 초기화
time_lapse = {idx: max_val for idx in range(1, city_number + 1)}

# 출발지 자신까지의 도달 시간 0
time_lapse[1] = 0

# 벨만 - 포드 알고리즘을 통한 목적지까지의 시간 계산
for count in range(city_number - 1):
    for way_point in range(1, city_number + 1):
        for next_cost, end_city in graph[way_point]:
            if time_lapse[way_point] != max_val:
                if time_lapse[end_city] >= time_lapse[way_point] + next_cost:
                    time_lapse[end_city] = time_lapse[way_point] + next_cost

# N - 1 번 반복한 기록을 저장
shortest_path = list(time_lapse.values())[:]

# N 번째 순회 진행
for way_point in range(1, city_number + 1):
    for next_cost, end_city in graph[way_point]:
        if time_lapse[way_point] != max_val:
            if time_lapse[end_city] >= time_lapse[way_point] + next_cost:
                time_lapse[end_city] = time_lapse[way_point] + next_cost

# 변화가 존재하지 않는다면 음의 사이클이 존재하지 않았다는 것
if shortest_path == list(time_lapse.values()):

    # 도달하지 못하는 지점은 -1 출력, 나머지는 소요 시간을 출력
    for idx in range(1, city_number):
        if shortest_path[idx] == max_val:
            print(-1)
        else:
            print(shortest_path[idx])

# 변화가 있다면 음의 사이클이 존재한다는 것으로 -1 출력
else:
    print(-1)
