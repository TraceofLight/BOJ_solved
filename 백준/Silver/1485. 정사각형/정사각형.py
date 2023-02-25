# 정사각형

import sys
from math import sqrt, isclose
from itertools import combinations

input = sys.stdin.readline


def distance(coord_1: list, coord_2: list) -> int:
    return sqrt(pow(coord_1[0] - coord_2[0], 2) + pow(coord_1[1] - coord_2[1], 2))


testcase = int(input())

output = []

for _ in range(testcase):

    is_square = True

    coord_info = []

    for _ in range(4):
        coord_info.append(list(map(int, input().split())))

    edge_info = []

    for edge_distance in combinations(coord_info, 2):
        edge_info.append(distance(edge_distance[0], edge_distance[1]))

    edge_info.sort()

    for idx in range(1, 4):
        if not isclose(edge_info[0], edge_info[idx]):
            is_square = False
            break

    if is_square:
        for idx in range(4, 6):
            if not isclose(pow(edge_info[0], 2) * 2, pow(edge_info[idx], 2)):
                is_square = False
                break

    if is_square:
        output.append(1)

    else:
        output.append(0)

for result in output:
    print(result)
