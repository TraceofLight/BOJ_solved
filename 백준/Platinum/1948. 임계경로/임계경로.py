# 임계경로

import sys
from collections import deque

input = sys.stdin.readline

# 도시의 갯수, 간선의 갯수 input
city_number = int(input())
line_number = int(input())

# 위상정렬을 위한 딕셔너리 선언
topology_sort = {idx: 0 for idx in range(1, city_number + 1)}

# 정방향 그래프 및 역방향 그래프 선언
graph = {idx: set() for idx in range(1, city_number + 1)}
reverse_graph = {idx: set() for idx in range(1, city_number + 1)}

# 간선 입력
for idx in range(1, line_number + 1):
    start_city, end_city, time_cost = map(int, input().split())
    topology_sort[end_city] += 1
    graph[start_city].add((time_cost, end_city))
    reverse_graph[end_city].add((time_cost, start_city))

# 출발지점과 목적지 input
start_city, end_city = map(int, input().split())

# 위상 정렬 및 역추적을 위한 큐 선언 및 출발지점 입력
progress_que = deque()
progress_que.append(start_city)

# 해당 지점에 가장 늦게 오는 사람의 시간을 기록할 딕셔너리 선언
last_time = {idx: 0 for idx in range(1, city_number + 1)}

# 너비 탐색
while progress_que:

    # 현재 도시 pop
    now_city = progress_que.popleft()

    # 해당 노드에서 뻗은 간선 제거
    for next_cost, next_city in sorted(list(graph[now_city])):
        topology_sort[next_city] -= 1

        # 현 지점에서 다음 지점까지 걸린 시간이 기록된 시간보다 클 경우 갱신
        if last_time[next_city] < last_time[now_city] + next_cost:
            last_time[next_city] = last_time[now_city] + next_cost

        # 간선이 0개가 되었을 경우 큐에 추가
        if not topology_sort[next_city]:
            progress_que.append(next_city)

# 마지막 지점에 기록된 값 확인
time_lapse = last_time[end_city]

# 가장 오래 걸린 사람들이 이용한 도로 수 카운팅 변수 선언
route_count = 0

# 도착지점에서 시작하여 역추적
progress_que.append(end_city)

# 방문한 지점에 대해서 다시 조사하지 않기 위한 방문 리스트 선언
is_visited = {idx: False for idx in range(1, city_number + 1)}

# 너비 탐색
while progress_que:

    # 현재 도시 pop
    now_city = progress_que.popleft()

    # 출발지에 도착하지 않았을 경우에만 조사
    if now_city != start_city:

        # 현 지점에 도착하는 모든 간선에 대해 조사
        for previous_time, previous_city in reverse_graph[now_city]:

            # 기록된 값에 부합하는 경우 카운팅
            if last_time[previous_city] + previous_time == last_time[now_city]:
                route_count += 1

                # 방문하지 않았던 지점은 큐에 추가
                if not is_visited[previous_city]:
                    progress_que.append(previous_city)
                    is_visited[previous_city] = True

# 결과 출력
print(time_lapse)
print(route_count)
