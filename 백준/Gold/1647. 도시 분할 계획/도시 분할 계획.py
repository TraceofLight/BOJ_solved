# 도시 분할 계획

import sys
from heapq import *

input = sys.stdin.readline

# 집의 갯수, 간선의 갯수 input
house_number, line_number = map(int, input().split())

# 간선 정보를 담을 우선순위 큐 선언
priority_line = []

# 간선 정보 input
for _ in range(line_number):
    house_a, house_b, cost = map(int, input().split())
    heappush(priority_line, [cost, house_a, house_b])

# 유니온 파인드 알고리즘 사용을 위한 딕셔너리 선언
city_division = {idx: idx for idx in range(1, house_number + 1)}


# 해당 노드가 포함된 집합을 확인하는 함수 선언
def find_node(node_dict: dict, init_node: int) -> int:
    if node_dict[init_node] == init_node:
        return init_node
    else:
        node_dict[init_node] = find_node(node_dict, node_dict[init_node])
        return node_dict[init_node]

# 집합 내에 포함되지 않은 경우 집합을 하나로 만들어주는 함수 선언
def union_node(node_dict: dict, node_1: int, node_2: int) -> bool:
    result_1, result_2 = find_node(node_dict, node_1), find_node(node_dict, node_2)
    if result_1 == result_2:
        return False
    node_dict[result_2] = node_dict[result_1]
    return True


# 간선 갯수 카운팅 변수 선언
line_counter = 0

# 유지비 변수 선언
min_cost = 0

# 유지비가 가장 많이 드는 길의 유지비를 기록할 변수 선언
max_each_cost = 0

# 최소 스패닝 트리가 될 때까지 진행
while line_counter < house_number - 1:

    # 우선순위 큐에서 최소값을 기준으로 하나씩 체크
    now_cost, now_start, now_end = heappop(priority_line)

    # 크루스칼 알고리즘 기준, 사이클을 형성하지 않는다면 집합에 포함 및 유지비 합산
    if union_node(city_division, now_start, now_end):
        min_cost += now_cost
        line_counter += 1
    
        # 유지비가 가장 높은 길보다 큰 값이라면 변수 갱신
        if max_each_cost < now_cost:
            max_each_cost = now_cost

# 해당 경로를 하나 제거하는 것을 마을이 2개로 분리
result = min_cost - max_each_cost

# 결과 출력
print(result)
