# 트리의 지름

import sys
from collections import deque

# 노드 갯수 input
node_number = int(sys.stdin.readline())

# 그래프와 라인별 가중치를 기록할 딕셔너리 선언
graph = [[] for _ in range(node_number)]
weight_dict = dict()

# 그래프, 딕셔너리에 정보 input
for _ in range(node_number):
    node_information = deque(list(map(int, sys.stdin.readline().split())))
    parent_node = node_information.popleft()
    parent_node -= 1
    while node_information:
        child_node = node_information.popleft()
        if child_node == -1:
            break
        else:
            weight = node_information.popleft()
            child_node -= 1
            weight_dict[(parent_node, child_node)] = weight
            graph[parent_node].append(child_node)

# 루트로부터 제일 멀리 있는 노드 확인을 위한 변수 선언
max_diameter = [0, 0]

# DFS
progress_stack = []
is_visited = [False for _ in range(node_number)]
# 임의의 노드를 기준으로 가장 먼 거리의 노드 확인
progress_stack.append([0, 0])
is_visited[0] = True
while progress_stack:
    now_point, now_length = progress_stack.pop()
    # 기존 최장 거리보다 현재 길이가 길다면 갱신 후 해당 노드를 기록
    if now_length > max_diameter[0]:
        max_diameter = [now_length, now_point]
    for element in graph[now_point]:
        if not is_visited[element]:
            is_visited[element] = True
            progress_stack.append([element, now_length + weight_dict[(now_point, element)]])

# 가장 멀리 있는 노드 변수 선언
max_half_diameter, max_node = max_diameter

# 지름 변수 선언
diameter = 0

# 지름 확인을 위한 DFS
progress_stack = []
is_visited = [False for _ in range(node_number)]
# 가장 먼 노드에서 출발
progress_stack.append([max_node, 0])
is_visited[max_node] = True
while progress_stack:
    now_point, now_length = progress_stack.pop()
    # 기존 최장 거리보다 현재 길이가 길다면 갱신
    if now_length > diameter:
        diameter = now_length
    for element in graph[now_point]:
        if not is_visited[element]:
            is_visited[element] = True
            progress_stack.append([element, now_length + weight_dict[(now_point, element)]])

# 결과 출력
print(diameter)
