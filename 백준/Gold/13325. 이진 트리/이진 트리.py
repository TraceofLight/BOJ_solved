# 이진 트리

import sys

input = sys.stdin.readline

tree_height = int(input())
node_number = pow(2, tree_height + 1)

edges = [0] + list(map(int, input().split()))
edge_sum = sum(edges)

now_start = node_number // 2 - 1
now_end = node_number - 1

while now_end:

    for i in range((now_end - now_start) // 2):

        child_edge = now_start + (2 * i)
        next_node = child_edge // 2

        edges[next_node] += max(edges[child_edge], edges[child_edge + 1])
        edge_sum += abs(edges[child_edge] - edges[child_edge + 1])

    now_end = now_start
    now_start = now_start // 2

print(edge_sum)
