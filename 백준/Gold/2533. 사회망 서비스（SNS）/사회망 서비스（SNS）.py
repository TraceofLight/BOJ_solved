# 사회망 서비스(SNS)

import sys
sys.setrecursionlimit(1100000)

input = sys.stdin.readline

# 정점 갯수 입력
vertex_number = int(input())

# 그래프 리스트 선언
graph = [[] for _ in range(vertex_number + 1)]

# 간선 정보 입력
for _ in range(vertex_number - 1):
    vert_1, vert_2 = map(int, input().split())
    graph[vert_1].append(vert_2)
    graph[vert_2].append(vert_1)

# 방문 기록 리스트 선언 및 루트 노드 방문 처리
is_visit = [False for _ in range(vertex_number + 1)]
is_visit[1] = True

# 최소값 정보를 담을 리스트 선언
result = [[0, 0] for _ in range(vertex_number + 1)]


def low_early_adapter(graph_info: list, is_visited: list, result_list: list, now_node: int = 1):
    '''
    얼리 어답터의 최소 인원을 반환하는 함수
    '''

    # Dynamic Programming

    # 자신이 얼리어답터인 경우 기본 최소값
    result_list[now_node][0] = 1

    # 자신이 얼리어답터가 아닌 경우 기본 최소값
    result_list[now_node][1] = 0

    for next_node in graph_info[now_node]:

        # 방문하지 않은 모든 점들에 대해서 조사
        if not is_visited[next_node]:

            # 방문 처리
            is_visited[next_node] = True

            # 재귀함수의 호출을 통해 하위 노드들 전부 처리
            low_early_adapter(graph_info, is_visited, result_list, next_node)

            # 하위 노드의 최소값들을 합산
            result_list[now_node][0] += min(result_list[next_node][0], result_list[next_node][1])
            result_list[now_node][1] += result_list[next_node][0]

    # 임의로 잡은 루트 노드 (1번 노드) 의 최소값을 반환
    return min(result_list[1])


# 함수를 호출하여 나온 결과를 출력
print(low_early_adapter(graph, is_visit, result))
