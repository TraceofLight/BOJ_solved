# 알고리즘 수업 - 깊이 우선 탐색 1

import sys 

input = sys.stdin.readline

# 노드 갯수, 간선 갯수, 시작 노드 input
node_number, line_number, start_node = map(int, input().split())

# 그래프 딕셔너리 선언
graph_dict = {idx: set() for idx in range(1, node_number + 1)}

# 간선 정보 딕셔너리에 기록
for _ in range(line_number):
    depart, arrive = map(int, input().split())
    graph_dict[depart].add(arrive)
    graph_dict[arrive].add(depart)

# 방문 기록 리스트 선언
is_visited = [False for _ in range(node_number + 1)]

# DFS 진행할 리스트 선언 및 시작 노드 input
progress_stack = []
progress_stack.append(start_node)
is_visited[start_node] = True

# 방문 순서 기록 리스트 선언 및 시작 노드 기록
result_list = [start_node]
result_set = {start_node}

# 문제 조건에 맞도록 DFS 진행
while progress_stack:
    now_index = progress_stack.pop()
    is_visited[now_index] = True
    if now_index not in result_set:
        result_list.append(now_index)
        result_set.add(now_index)
    for next_index in reversed(sorted(list(graph_dict[now_index]))):
        if not is_visited[next_index]:
            progress_stack.append(next_index)

# 순서를 확인할 수 있도록 hash 선언 및 정보 입력
result_dict = {result_list[idx]: idx + 1 for idx in range(len(result_list))}

# 해시 정보에 따라 결과를 출력
for each_node in range(1, node_number + 1):
    if result_dict.get(each_node) is not None:
        print(result_dict[each_node])
    else:
        print(0)
