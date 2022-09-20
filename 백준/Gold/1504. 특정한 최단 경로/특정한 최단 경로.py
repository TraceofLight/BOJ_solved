# 특정한 최단경로

import sys
from heapq import *

input = sys.stdin.readline

node_number, line_number = map(int, input().split())

graph = {idx: [] for idx in range(1, node_number + 1)}

for _ in range(line_number):
    node1, node2, cost = map(int, input().split())
    graph[node1].append([cost, node2])
    graph[node2].append([cost, node1])

max = 2000000000

distance = [max for _ in range(node_number + 1)]
distance2 = [max for _ in range(node_number + 1)]

waypoint1, waypoint2 = map(int, input().split())

# 출발지에서 각 노드까지 최소 이동 거리 (dijkstra)

distance[1] = 0
priority_que = [[0, 1, {1}]]
waypoint_all_path = {waypoint1: max, waypoint2: max}

while priority_que:
    now_cost, now_point, visit_log = heappop(priority_que)
    for next_cost, next_point in sorted(graph[now_point]):
        if distance[next_point] > distance[now_point] + next_cost:
            distance[next_point] = distance[now_point] + next_cost
            heappush(priority_que, [distance[now_point] + next_cost, next_point, visit_log | {next_point}])

            # 경유지의 경우 2개의 점을 동시에 지난 경우가 있는지 체크
            if next_point == waypoint1:
                if waypoint2 in visit_log:
                    if waypoint_all_path[waypoint1] > distance[next_point]:
                        waypoint_all_path[waypoint1] = distance[next_point]
            elif next_point == waypoint2:
                if waypoint1 in visit_log:
                    if waypoint_all_path[waypoint2] > distance[next_point]:
                        waypoint_all_path[waypoint2] = distance[next_point]

# 도착점에서 각 노드까지 최소 이동 거리 측정 (dijkstra)

distance2[node_number] = 0
priority_que = [[0, node_number]]

while priority_que:
    now_cost, now_point = heappop(priority_que)
    for next_cost, next_point in sorted(graph[now_point]):
        if distance2[next_point] > distance2[now_point] + next_cost:
            distance2[next_point] = distance2[now_point] + next_cost
            heappush(priority_que, [distance2[now_point] + next_cost, next_point])

# 도착지가 도달할 수 없는 케이스일 경우
if (
    distance[node_number] == max 
    or distance[waypoint1] == max
    or distance[waypoint2] == max
    or distance2[waypoint1] == max
    or distance2[waypoint2] == max
):
    result = -1

# 도달할 수 있는 경우 케이스 분석
else:

    # 경유지끼리 최소 이동 거리 측정 (dijkstra)

    distance3 = [max for _ in range(node_number + 1)]
    distance3[waypoint1] = 0

    priority_que = [[0, waypoint1]]

    while priority_que:
        now_cost, now_point = heappop(priority_que)
        for next_cost, next_point in sorted(graph[now_point]):
            if distance3[next_point] > distance3[now_point] + next_cost:
                distance3[next_point] = distance3[now_point] + next_cost
                heappush(priority_que, [distance3[now_point] + next_cost, next_point])

    # 경유지끼리 이어지지 못한 경우 결과값 -1
    if distance3[waypoint2] == max:
        result = -1

    # 아니라면 각 경유지를 순서를 거쳐 도착지로 이동하는 경우 중 최소값을 결과값으로 지정
    else:
        result = min(
            distance[waypoint1] + distance2[waypoint2] + distance3[waypoint2]
            , distance[waypoint2] + distance2[waypoint1] + distance3[waypoint2]
        )

# 결과 출력
print(result)
