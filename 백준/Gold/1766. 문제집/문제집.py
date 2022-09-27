# 문제집

import sys
from heapq import *

input = sys.stdin.readline

question_number, good_question = map(int, input().split())

topology_sort = {idx: 0 for idx in range(1, question_number + 1)}

graph = {idx: [] for idx in range(1, question_number + 1)}

for _ in range(good_question):
    precede, follow = map(int, input().split())
    topology_sort[follow] += 1
    graph[precede].append(follow)

priority_que = []

for idx in range(1, question_number + 1):
    if not topology_sort[idx]:
        heappush(priority_que, idx)

result_list = []

while priority_que:

    now_question = heappop(priority_que)
    result_list.append(now_question)

    for next_question in sorted(graph[now_question]):
        topology_sort[next_question] -= 1
        if not topology_sort[next_question]:
            heappush(priority_que, next_question)

print(*result_list)