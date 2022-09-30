# 완전 이진 트리

import sys

input = sys.stdin.readline


# 완전 이진 트리를 만드는 함수 선언
def make_binary_tree(node_number: int) -> dict:

    # 자식 노드를 가지는 마지막 노드 번호 확인
    last_parent = node_number // 2

    # 결과 딕셔너리 생성
    result_dict = {idx: [] for idx in range(1, node_number + 1)}

    # 자식 노드 추가
    for root_node in range(1, last_parent + 1):
        result_dict[root_node].append(root_node * 2)
        result_dict[root_node].append(root_node * 2 + 1)

    # 완성된 완전 이진 트리를 반환
    return result_dict

# 완전 이진 트리의 중위 순회 함수 선언
def inorder(target_dict: dict, root: int) -> None:

    # 결과값을 담을 리스트
    global result_inorder

    # 자식이 있는 경우 중위 순회 진행 및 루트 추가
    if target_dict[root]:
        child1, child2 = target_dict[root]
        inorder(target_dict, child1)
        result_inorder.append(root)
        inorder(target_dict, child2)

    # 자식이 없는 경우 루트 자기 자신만 추가
    else:
        result_inorder.append(root)


# 계층 수 및 노드 정보 input
stage_number = int(input())
node_number_list = list(map(int, input().split()))

# 전체 노드 갯수 확인
total_node_number = (2 ** stage_number) - 1

# 2의 제곱수 노드 번호 리스트 선언

last_stage_node_list = [(2 ** idx) - 1 for idx in range(1, stage_number)]

# 중위 순회 값을 담을 리스트 선언
result_inorder = []

# 함수를 호출하여 완전 이진 트리 기본형의 중위 순회를 진행
inorder(make_binary_tree(total_node_number), 1)

# 완전 이진 트리 기본형 자리에 대응하는 input 값과 연결된 해시 테이블 제작
hash_table = {result_inorder[idx]: node_number_list[idx] for idx in range(total_node_number)}

# 계층에 따라서 출력
for node in range(1, total_node_number + 1):

    # 계층의 마지막 노드일 경우 줄바꿈
    if node in last_stage_node_list:
        print(hash_table[node])

    # 아닐 경우 줄바꿈 없이 이어서 출력
    else:
        print(hash_table[node], end=' ')
