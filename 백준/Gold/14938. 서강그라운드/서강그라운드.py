# 서강그라운드

import sys
from heapq import *

input = sys.stdin.readline

# 지역의 갯수, 수색 범위, 간선 갯수 input
node_number, search_range, line_number = map(int, input().split())

# 각 노드별 아이템 정보 해시화
node_item_list = list(map(int, input().split()))
item_hash_table = {idx: node_item_list[idx - 1] for idx in range(1, node_number + 1)}

# 간선 딕셔너리 선언
graph_dict = {idx: [] for idx in range(1, node_number + 1)}

# 간선 정보 입력
for _ in range(line_number):
    start_node, end_node, distance = map(int, input().split())
    graph_dict[start_node].append([distance, end_node])
    graph_dict[end_node].append([distance, start_node])

# inf value 선언
max_val = 2000000000

# 최대 아이템 갯수 변수 선언
max_item_number = 0

# 모든 지점에 대하여 다익스트라 알고리즘을 통해 최단거리 도출
for start_node in range(1, node_number + 1):

    # 모든 노드에 대한 거리값을 inf로 초기화
    distance = [max_val for _ in range(node_number + 1)]
    # 시작점 거리 0 
    distance[start_node] = 0

    # 우선순위 큐 선언 및 초기값 입력
    priority_que = [[0, start_node]]

    # 갱신할 때마다 거리값 변경 후 큐에 다시 삽입
    while priority_que:
        now_distance, now_point = heappop(priority_que)
        for next_distance, next_point in sorted(graph_dict[now_point]):
            if distance[next_point] > distance[now_point] + next_distance:
                distance[next_point] = distance[now_point] + next_distance
                heappush(priority_que, [distance[next_point], next_point])

    # 한 지점에서 다른 지점까지 거리가 수색 범위 내라면 해당 지점의 아이템 갯수를 합산
    get_item = 0
    for dist_idx in range(1, node_number + 1):
        if distance[dist_idx] <= search_range:
            get_item += item_hash_table[dist_idx]

    # 최대 아이템 갯수를 넘었다면 해당 값으로 갱신
    if get_item > max_item_number:
        max_item_number = get_item

# 결과 출력
print(max_item_number)
