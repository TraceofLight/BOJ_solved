# 줄 세우기

import sys
from collections import deque

input = sys.stdin.readline

student_number, compare_count = map(int, input().split())

count_line = {idx: 0 for idx in range(1, student_number + 1)}

connection_graph = {idx: set() for idx in range(1, student_number + 1)}

for _ in range(compare_count):
    lower_height, upper_height = map(int, input().split())
    connection_graph[lower_height].add(upper_height)
    count_line[upper_height] += 1

topology_sort = deque()


for student in range(1, student_number + 1):
    if not count_line[student]:
        topology_sort.append(student)

make_line = []

while topology_sort:
    now_student = topology_sort.popleft()
    make_line.append(now_student)

    for next_student in connection_graph[now_student]:
        count_line[next_student] -= 1

        if not count_line[next_student]:
            topology_sort.append(next_student)

print(*make_line)
