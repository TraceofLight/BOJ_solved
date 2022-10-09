# Strongly Connected Component

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

# 재귀 한도 상향
sys.setrecursionlimit(100001)


def dfs(edge_info: dict, init_vertex: int, result_stack: list, visited: list) -> None:
    '''
    깊이 탐색을 진행하고 완료한 순서대로 스택에 담는 함수
    '''

    # 현 지점 방문 처리
    visited[init_vertex] = True

    # 현 지점에서 갈 수 있는 다음 지점들에 대해 조사
    for next_vertex in edge_info[init_vertex]:

        # 방문하지 않은 지점에 대해서 깊이 탐색 진행
        if not visited[next_vertex]:
            dfs(edge_info, next_vertex, result_stack, visited)

    # 모든 정점에 대해서 진행이 완료된 이후 스택에 추가
    result_stack.append(init_vertex)

def rev_dfs(edge_info: dict, init_vertex: int, result_que: list, visited: list) -> None:
    '''
    역방향 그래프에 대해서 깊이 탐색을 진행하는 함수
    '''

    # 현 정점 방문 처리 및 현 정점을 우선순위 큐에 추가
    visited[init_vertex] = True
    heappush(result_que, init_vertex)

    # 현 지점에서 갈 수 있는 다음 지점들에 대해 조사
    for next_vertex in edge_info[init_vertex]:

        # 방문하지 않은 지점에 대해서 깊이 탐색 진행
        if not visited[next_vertex]:
            rev_dfs(edge_info, next_vertex, result_que, visited)


# 노드 갯수, 간선 갯수 입력
vertex_number, edge_number = map(int, input().split())

# 정방향 및 역방향 유향 그래프 딕셔너리 선언 
graph_dict = {idx: [] for idx in range(1, vertex_number + 1)}
reverse_graph_dict = {idx: [] for idx in range(1, vertex_number + 1)}

# 간선 정보 입력
for _ in range(edge_number):
    start_vertex, end_vertex = map(int, input().split())
    graph_dict[start_vertex].append(end_vertex)
    reverse_graph_dict[end_vertex].append(start_vertex)

# 정방향 방문 리스트 선언 및 깊이 탐색을 위한 스택 선언
is_visited = [False for _ in range(vertex_number + 1)]
progress_stack = []

# 강한 연결 요소 확인을 위한 정방향 깊이 탐색 리스트 선언
scc_stack = []

# 모든 정점에 대해 조사
for now_vertex in range(1, vertex_number + 1):

    # 아직 방문하지 않은 경우
    if not is_visited[now_vertex]:

        # 함수를 호출하여 스택에 탐색 결과 반영
        dfs(graph_dict, now_vertex, scc_stack, is_visited)

# 강한 연결 요소 그룹을 담을 리스트 선언
scc_group = []

# 그룹 갯수를 카운팅할 변수 선언
result_count = 0

# 역방향 방문 리스트 선언
is_visited_rev = [False for _ in range(vertex_number + 1)]

# 스택 내의 정점에 대해 순서대로 확인
while scc_stack:

    # 현재 그룹의 정점 정보를 담을 리스트 선언
    now_group = []

    # 스택 최상단 정점부터 조사
    now_vertex = scc_stack.pop()

    # 아직 해당 정점을 방문하지 않은 경우
    if not is_visited_rev[now_vertex]:

        # 함수를 호출하여 같은 그룹의 정점 역추적
        rev_dfs(reverse_graph_dict, now_vertex, now_group, is_visited_rev)

        # 그룹 갯수 카운팅
        result_count += 1

    # 그룹들을 담는 리스트에 현재 그룹을 추가
    heappush(scc_group, now_group)

# 그룹 갯수 출력
print(result_count)

# 그룹 정보는 조건에 따라 출력
while scc_group:

    # 그룹의 대표 번호가 가장 작은 그룹부터 확인
    each_group = heappop(scc_group)

    # 그룹 내 정점이 존재할 경우만 출력
    if each_group:

        # 모든 원소들을 작은 정점부터 출력
        while each_group:
            print(heappop(each_group), end=' ')

        # 마지막에 -1 출력
        print(-1)
