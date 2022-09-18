# 최소비용 구하기 2

import sys
from heapq import *

input = sys.stdin.readline

# 도시 갯수, 간선 갯수 input
city_number = int(input())
line_number = int(input())

# 그래프 딕셔너리 선언
graph = {idx: [] for idx in range(1, city_number + 1)}

# 간선 정보 input
for _ in range(line_number):
    start_city, end_city, cost = map(int, input().split())
    graph[start_city].append([cost, end_city])

# 출발지, 도착지 정보 input
depart_city, arrive_city = map(int, input().split())

# 최소 비용 리스트 선언 및 매우 큰 수로 초기화
cost = [2000000000 for _ in range(city_number + 1)]

# 시작점 비용 0으로 초기화
cost[depart_city] = 0

# 우선순위 큐 선언 및 출발 지점 input
priority_que = [[0, depart_city, [depart_city]]]

# 최소 비용 변수 선언
min_cost = 2000000000

# 이미 있는 노선의 비용값이 있다면 초기화 (기본값 지정)
for line_info in graph[depart_city]:
    line_cost, destination = line_info
    if destination == arrive_city:
        min_cost = min(min_cost, line_cost)

# 최소 비용 경로 변수 선언 및 기본값 input
short_log = [depart_city, arrive_city]

# 다익스트라 알고리즘을 사용한 최소 비용 체크
while priority_que:
    now_cost, now_city, move_log = heappop(priority_que)
    if now_city == arrive_city and now_cost < min_cost:
        min_cost = now_cost
        short_log = move_log
    for next_point in sorted(graph[now_city]):
        next_cost, next_city = next_point
        if cost[next_city] > cost[now_city] + next_cost:
            cost[next_city] = cost[now_city] + next_cost
            heappush(priority_que, [cost[now_city] + next_cost, next_city, move_log + [next_city]])

# 문제 요구 조건에 따라 결과 출력
print(cost[arrive_city])
print(len(short_log))
print(*short_log)
