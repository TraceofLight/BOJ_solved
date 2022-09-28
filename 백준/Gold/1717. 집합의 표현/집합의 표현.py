# 집합의 표현

import sys

input = sys.stdin.readline

# 재귀 한도 변경
sys.setrecursionlimit(1000000)

# 해당 노드의 집합을 확인하는 함수 선언
def find_node(node_dict: dict, target_node: int) -> int:
    if node_dict[target_node] == target_node:
        return target_node
    else:
        node_dict[target_node] = find_node(node_dict, node_dict[target_node])
        return node_dict[target_node]

# 두 분리 집합을 합쳐주는 함수 선언
def union_node(node_dict: dict, node_1: int, node_2: int) -> bool:
    set_number_1, set_number_2 = find_node(node_dict, node_1), find_node(node_dict, node_2)
    if set_number_1 == set_number_2:
        return False
    else:
        if set_number_1 > set_number_2:
            node_dict[set_number_1] = set_number_2
        else:
            node_dict[set_number_2] = set_number_1
        return True

# 분리 집합인지 아닌지 확인하는 함수 선언
def check_union(node_dict: dict, node_1: int, node_2: int) -> bool:
    set_number_1, set_number_2 = find_node(node_dict, node_1), find_node(node_dict, node_2)
    if set_number_1 == set_number_2:
        return True
    else:
        return False


# 마지막 노드 번호, 명령문 횟수 input
last_node_number, order_amount = map(int, input().split())

# 출력 리스트 선언
output = []

# 각 노드의 집합 정보를 담을 딕셔너리 선언
set_dict = {idx: idx for idx in range(last_node_number + 1)}

for _ in range(order_amount):

    # 명령문의 종류 및 노드 정보 input
    order_type, set_node_1, set_node_2 = map(int, input().split())

    # order type이 0일 경우
    if not order_type:

        # 함수를 호출하여 각 노드의 집합을 합침
        union_node(set_dict, set_node_1, set_node_2)

    # order tyoe이 1일 경우
    elif order_type:

        # 함수를 호출하여 한 집합인지 체크
        is_union_now = check_union(set_dict, set_node_1, set_node_2)

        # 결과값에 따라서 출력 리스트에 문구를 추가
        if is_union_now:
            output.append('YES')
        else:
            output.append('NO')

# 출력
for result in output:
    print(result)
