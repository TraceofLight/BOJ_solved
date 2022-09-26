# 최소 스패닝 트리

import sys
from heapq import *

input = sys.stdin.readline

node_number, line_number = map(int, input().split())

line_list = []

for _ in range(line_number):
    start_node, end_node, weight = map(int, input().split())
    heappush(line_list, [weight, start_node, end_node])

union_find = {idx: idx for idx in range(1, node_number + 1)}

min_spanning_tree = 0


def find_node(union_dict: dict, check_node: int):
    if union_dict[check_node] == check_node:
        return check_node
    else:
        union_dict[check_node] = find_node(union_dict, union_dict[check_node])
        return union_dict[check_node]

def union_node(union_dict: dict, node_1, node_2):
    result1, result2 = find_node(union_dict, node_1), find_node(union_dict, node_2)
    if result1 == result2:
        return False
    else:
        union_dict[result1] = result2
        return True


for _ in range(line_number):
    now_weight, now_start, now_end = heappop(line_list)
    if union_node(union_find, now_start, now_end):
        min_spanning_tree += now_weight

print(min_spanning_tree)
