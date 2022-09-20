# 파티

import sys
from heapq import *

input = sys.stdin.readline

node_number, line_number, end_point = map(int, input().split())

graph_dict = {idx: [] for idx in range(1, node_number + 1)}

for _ in range(line_number):
    start_node, end_node, time_cost = map(int, input().split())
    graph_dict[start_node].append([time_cost, end_node])

max_val = 2000000000

distance_from_end_point = [max_val for _ in range(node_number + 1)]

distance_from_end_point[0] = 0
distance_from_end_point[end_point] = 0

for start_point in range(1, node_number + 1):
    if start_point == end_point:
        continue
    else:
        min_time_go = [max_val for _ in range(node_number + 1)]
        min_time_go[start_point] = 0

        priority_que = [[0, start_point]]

        while priority_que:
            now_time, now_point = heappop(priority_que)
            for next_time, next_point in graph_dict[now_point]:
                if min_time_go[next_point] > min_time_go[now_point] + next_time:
                    min_time_go[next_point] = min_time_go[now_point] + next_time
                    heappush(priority_que, [min_time_go[now_point] + next_time, next_point])

        min_time_back = [max_val for _ in range(node_number + 1)]
        min_time_back[end_point] = 0

        priority_que = [[0, end_point]]

        while priority_que:
            now_time, now_point = heappop(priority_que)
            for next_time, next_point in graph_dict[now_point]:
                if min_time_back[next_point] > min_time_back[now_point] + next_time:
                    min_time_back[next_point] = min_time_back[now_point] + next_time
                    heappush(priority_que, [min_time_back[now_point] + next_time, next_point])

        distance_from_end_point[start_point] = min_time_go[end_point] + min_time_back[start_point]

print(max(distance_from_end_point))
