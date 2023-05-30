# 행성 터널

import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def check_union(union_info: list, now_target: int) -> int:
    """
    해당 노드의 현재 유니온을 조회하는 함수
    """

    if union_info[now_target] == -1:
        union_info[now_target] = now_target

    elif union_info[now_target] != now_target:
        union_info[now_target] = check_union(union_info, union_info[now_target])

    return union_info[now_target]


def make_union(union_info: list, target_1: int, target_2: int) -> None:
    """
    두 점이 같은 유니온인지 확인하고 아니라면 합쳐주는 함수
    """
    union_1 = check_union(union_info, target_1)
    union_2 = check_union(union_info, target_2)

    if union_1 == union_2:
        return True

    else:
        if union_1 > union_2:
            union_info[union_1] = union_2
        else:
            union_info[union_2] = union_1

        return False


planet_number = int(input())
coord_list = []

for i in range(planet_number):
    coord_list.append([i] + list(map(int, input().split())))

cost_queue = []

for i in range(1, 4):
    coord_list.sort(key=lambda x: x[i])
    for j in range(planet_number - 1):
        heappush(
            cost_queue,
            (
                coord_list[j + 1][i] - coord_list[j][i],
                (coord_list[j][0], coord_list[j + 1][0]),
            ),
        )

union_info = [-1 for _ in range(planet_number)]

total_length = 0
line_number = 0

while cost_queue:
    if line_number == planet_number - 1:
        break

    now_length, nodes = heappop(cost_queue)
    node_a, node_b = nodes

    if not make_union(union_info, node_a, node_b):
        total_length += now_length
        line_number += 1

print(total_length)
