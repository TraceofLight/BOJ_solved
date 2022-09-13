# SWEA_1231 중위순회

from collections import deque

# 테스트 케이스 10회
testcase = 10
# 출력 리스트 선언
output = []

for each_case in range(testcase):
    # 노드 갯수 input
    node_number = int(input())
    # 노드가 의미하는 알파벳과 연결하는 hash dict 선언
    node_dictionary = dict()
    # graph 선언
    graph = [[] for _ in range(node_number)]
    # 노드 관련 정보 입력
    for _ in range(node_number):
        node_info = deque(list(input().split()))
        key_number = int(node_info.popleft())
        value = node_info.popleft()
        node_dictionary[key_number] = value
        while node_info:
            child_node = int(node_info.popleft()) - 1
            graph[key_number - 1].append(child_node)

    # 중위 순회 함수 선언
    def inorder_tree(structure: list, init_node: int, result_list: list, hash_dict: dict):
        child_nodes = structure[init_node]
        if len(child_nodes) == 2:
            inorder_tree(structure, child_nodes[0], result_list, hash_dict)
            result_list.append(hash_dict[init_node + 1])
            inorder_tree(structure, child_nodes[1], result_list, hash_dict)
        elif len(child_nodes) == 1:
            inorder_tree(structure, child_nodes[0], result_list, hash_dict)
            result_list.append(hash_dict[init_node + 1])
        else:
            result_list.append(hash_dict[init_node + 1])

    # 결과 리스트 선언
    result = []

    # 함수 호출 이후 결과값을 출력 리스트에 추가
    inorder_tree(graph, 0, result, node_dictionary)
    output.append(''.join(result))

# 문제의 요구 조건에 맞춰서 출력
for output_idx in range(testcase):
    print(f'#{output_idx + 1} {output[output_idx]}')
