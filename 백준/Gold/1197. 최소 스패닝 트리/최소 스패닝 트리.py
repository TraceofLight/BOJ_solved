# 최소 스패닝 트리

import sys
from heapq import *

input = sys.stdin.readline

# 노드 갯수 및 간선 갯수 input
node_number, line_number = map(int, input().split())

# 간선 정보 우선순위 큐에 입력
priority_que = []
for _ in range(line_number):
    start_node, end_node, weight = map(int, input().split())
    heappush(priority_que, [weight, start_node, end_node])

# 유니온 파인드 알고리즘 사용을 위한 딕셔너리 선언
union_find = {idx: idx for idx in range(1, node_number + 1)}


# 파인드 함수 선언
def find_node(union_dict: dict, check_node: int):
    if union_dict[check_node] == check_node:
        return check_node
    else:
        union_dict[check_node] = find_node(union_dict, union_dict[check_node])
        return union_dict[check_node]

# 유니온 함수 선언 (해당 함수를 통해 노드 집합을 합친다)
def union_node(union_dict: dict, node_1, node_2):
    result1, result2 = find_node(union_dict, node_1), find_node(union_dict, node_2)
    if result1 == result2:
        return False
    else:
        union_dict[result1] = result2
        return True


# 결과값 변수 선언
min_spanning_tree = 0

# 라인 갯수만큼 크루스칼 알고리즘을 통해 진행하면서 스패닝 트리 구축
for _ in range(line_number):
    now_weight, now_start, now_end = heappop(priority_que)

    # 같은 집합 안에 없는 경우 추가하면서 결과값 변수에 가중치 합산
    if union_node(union_find, now_start, now_end):
        min_spanning_tree += now_weight

# 결과 출력
print(min_spanning_tree)
