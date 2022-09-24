# 타임머신

import sys

input = sys.stdin.readline

city_number, line_number = map(int, input().split())


graph = {idx: [] for idx in range(1, city_number + 1)}

for _ in range(line_number):
    start_city, end_city, time_cost = map(int, input().split())
    graph[start_city].append([time_cost, end_city])

max_val = 2000000000

time_lapse = {idx: max_val for idx in range(1, city_number + 1)}

time_lapse[1] = 0

for count in range(city_number - 1):
    for way_point in range(1, city_number + 1):
        for next_cost, end_city in graph[way_point]:
            if time_lapse[way_point] != max_val:
                if time_lapse[end_city] >= time_lapse[way_point] + next_cost:
                    time_lapse[end_city] = time_lapse[way_point] + next_cost

shortest_path = list(time_lapse.values())[:]

for way_point in range(1, city_number + 1):
    for next_cost, end_city in graph[way_point]:
        if time_lapse[way_point] != max_val:
            if time_lapse[end_city] >= time_lapse[way_point] + next_cost:
                time_lapse[end_city] = time_lapse[way_point] + next_cost

if shortest_path == list(time_lapse.values()):
    for idx in range(1, city_number):
        if shortest_path[idx] == max_val:
            print(-1)
        else:
            print(shortest_path[idx])

else:
    print(-1)
