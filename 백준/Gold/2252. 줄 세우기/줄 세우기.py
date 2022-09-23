# 줄 세우기

import sys
from collections import deque

input = sys.stdin.readline

# 학생 숫자, 비교 횟수 input
student_number, compare_count = map(int, input().split())

# 도착 노드로 이어진 간선 갯수 카운팅 딕셔너리 선언
count_line = {idx: 0 for idx in range(1, student_number + 1)}

# 관계도 그래프 선언
connection_graph = {idx: set() for idx in range(1, student_number + 1)}

# 간선 정보 input
for _ in range(compare_count):
    lower_height, upper_height = map(int, input().split())
    connection_graph[lower_height].add(upper_height)
    count_line[upper_height] += 1

# 위상 정렬을 위한 큐 선언
topology_sort = deque()

# 간선의 도착점이 아닌 노드들만 큐에 추가
for student in range(1, student_number + 1):
    if not count_line[student]:
        topology_sort.append(student)

# 줄 세우는 리스트 선언
make_line = []

# 위상 정렬
while topology_sort:

    # 간선이 정리된 순으로 줄 세우기
    now_student = topology_sort.popleft()
    make_line.append(now_student)

    # 간선 제거
    for next_student in connection_graph[now_student]:
        count_line[next_student] -= 1

        # 간선 갯수가 0이 된 경우 큐에 추가
        if not count_line[next_student]:
            topology_sort.append(next_student)

# 결과 출력
print(*make_line)
