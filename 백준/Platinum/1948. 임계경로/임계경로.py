# 임계경로

import sys
from collections import deque

input = sys.stdin.readline

city_number = int(input())
line_number = int(input())

topology_sort = {idx: 0 for idx in range(1, city_number + 1)}

graph = {idx: set() for idx in range(1, city_number + 1)}
reverse_graph = {idx: set() for idx in range(1, city_number + 1)}

for idx in range(1, line_number + 1):
    start_city, end_city, time_cost = map(int, input().split())
    topology_sort[end_city] += 1
    graph[start_city].add((time_cost, end_city))
    reverse_graph[end_city].add((time_cost, start_city))

start_city, end_city = map(int, input().split())

progress_que = deque()

max_time = {idx: 0 for idx in range(1, city_number + 1)}

progress_que.append(start_city)

while progress_que:

    now_city = progress_que.popleft()

    for next_cost, next_city in sorted(list(graph[now_city])):
        topology_sort[next_city] -= 1

        if max_time[next_city] < max_time[now_city] + next_cost:
            max_time[next_city] = max_time[now_city] + next_cost

        if not topology_sort[next_city]:
            progress_que.append(next_city)

result1 = max_time[end_city]

result2 = 0

progress_que.append(end_city)
is_visited = {idx: False for idx in range(1, city_number + 1)}

while progress_que:

    now_city = progress_que.popleft()

    if now_city != start_city:

        for last_time, last_city in reverse_graph[now_city]:
            if max_time[last_city] + last_time == max_time[now_city]:
                result2 += 1
                if not is_visited[last_city]:
                    progress_que.append(last_city)
                    is_visited[last_city] = True

print(result1)
print(result2)