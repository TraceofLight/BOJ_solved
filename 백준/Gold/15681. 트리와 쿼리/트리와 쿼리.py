# 트리와 쿼리

import sys

input = sys.stdin.readline

# 재귀 한도 상향 처리
sys.setrecursionlimit(1000000)


# 자식 노드를 찾고 갯수를 카운팅하는 함수 선언
def find_child(graph_dict: dict, parent_node: int, now_node: int, result_dict: dict) -> None:

    # 현재 노드를 포함하여 기본값 1 설정
    result_dict[now_node] = 1

    # 해당 노드에 연결된 노드들 전수 조사
    for next_node in graph_dict[now_node]:

        # 부모 노드가 아닌 경우에 이어서 조사
        if next_node != parent_node:

            # 다음 노드들에 대해서도 확인
            find_child(graph_dict, now_node, next_node, result_dict)

            # 다음 노드들 값을 현재 노드에 합산
            result_dict[now_node] += result_dict[next_node]

    # 결과 반환
    return result_dict[now_node]


# 노드 숫자, 루트 노드, 쿼리 갯수 입력
node_number, root_node, query_number = map(int, input().split())

# 관계 그래프 딕셔너리 선언
graph = {idx: set() for idx in range(1, node_number + 1)}

# 양방향 그래프 정보 입력
for _ in range(node_number - 1):
    node_1, node_2 = map(int, input().split())
    graph[node_1].add(node_2)
    graph[node_2].add(node_1)

# 서브 트리 노드의 갯수를 담을 딕셔너리 선언
subtree_dict = dict()

# 함수를 호출하여 전체 노드에 대한 서브 트리의 노드 갯수 확인
find_child(graph, -1, root_node, subtree_dict)

# 출력 리스트 선언
output = []

# 쿼리 확인
for _ in range(query_number):

    # 서브트리의 루트 노드 정보 입력
    target_node = int(input())

    # 결과값 출력 리스트에 추가
    output.append(subtree_dict[target_node])

# 출력
for result in output:
    print(result)
