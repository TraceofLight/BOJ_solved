# 수열과 쿼리 16

import sys
from math import log2, ceil

input = sys.stdin.readline


def make_seg_tree(tree_result: list, target_list: list, start: int, end: int, node: int = 1) -> int:
    '''
    리스트를 기반으로 범위 내 최소값을 가지는 인덱스를 값으로 하는 세그먼트 트리를 만드는 함수
    '''

    # 포인터가 겹친 경우
    if start == end:

        # 트리에 인덱스 입력
        tree_result[node] = start

        # 해당 인덱스를 반환
        return start

    # 포인터가 범위로 주어진 경우
    else:

        # 이분 탐색 알고리즘을 사용
        mid = (start + end) // 2

        # 자식 노드들의 최소값 인덱스 확인
        idx_1 = make_seg_tree(tree_result, target_list, start, mid, 2 * node)
        idx_2 = make_seg_tree(tree_result, target_list, mid + 1, end, 2 * node + 1)

        # 값이 크거나 작은 경우 해당 인덱스를 반환
        if target_list[idx_1] < target_list[idx_2]:
            tree_result[node] = idx_1
            return idx_1

        elif target_list[idx_1] > target_list[idx_2]:
            tree_result[node] = idx_2
            return idx_2

        # 값이 동일한 경우 인덱스 자체가 작은 값을 반환
        else:
            if idx_1 < idx_2:
                tree_result[node] = idx_1
                return idx_1

            else:
                tree_result[node] = idx_2
                return idx_2

def find_min(tree_info: list, target_list: list, start: int, end: int, left: int, right: int, node: int = 1) -> int:
    '''
    범위가 주어졌을 때 해당 범위 내 최소값 인덱스가 몇 번인지 확인하는 함수
    '''

    # 범위를 벗어난 경우 INF값으로 통하는 해시값 반환
    if start > right or end < left:
        return 0

    # 범위를 전부 포함하는 경우 노드의 값을 반환
    elif start >= left and end <= right:
        return tree_info[node]

    # 범위를 일부만 포함하는 경우
    else:

        # 이분 탐색 알고리즘을 사용
        mid = (start + end) // 2

        # 자식들의 최소값 조사
        idx_1 = find_min(tree_info, target_list, start, mid, left, right, node * 2)
        idx_2 = find_min(tree_info, target_list, mid + 1, end, left, right, node * 2 + 1)

        # 크기에 따라 최소 인덱스를 반환
        if target_list[idx_1] < target_list[idx_2]:
            return idx_1

        elif target_list[idx_1] > target_list[idx_2]:
            return idx_2

        # 크기가 동일할 경우 인덱스 자체값이 작은 경우를 반환
        else:
            if idx_1 < idx_2:
                return idx_1
            else:
                return idx_2

def mod_min(tree_info: list, target_list: list, start: int, end: int, index:int, node: int = 1) -> None:
    '''
    리스트 값이 변경되었을 때 트리의 결과를 동기화하는 함수
    '''

    # 범위를 벗어난 경우 작업하지 않음
    if start > index or end < index:
        return

    # 포인터가 모인 경우도 마찬가지로 변경사항 없음
    elif start == end:

        return

    # 그 외의 경우 조사
    else:

        # 이분 탐색 알고리즘을 사용
        mid = (start + end) // 2

        # 재귀 함수를 호출하여 자손 노드들에 대해서 먼저 반영 진행
        mod_min(tree_info, target_list, start, mid, index, node * 2)
        mod_min(tree_info, target_list, mid + 1, end, index, node * 2 + 1)

        # 최소값이 전부 반영되었다면 결과값을 갱신
        if target_list[tree_info[node * 2]] < target_list[tree_info[node * 2 + 1]]:
            tree_info[node] = tree_info[node * 2]

        elif target_list[tree_info[node * 2]] > target_list[tree_info[node * 2 + 1]]:
            tree_info[node] = tree_info[node * 2 + 1]

        else:
            if tree_info[node * 2] < tree_info[node * 2 + 1]:
                tree_info[node] = tree_info[node * 2]

            else:
                tree_info[node] = tree_info[node * 2 + 1]


# INF 지정
INF = 2000000000

# 숫자 갯수 입력
number_amount = int(input())

# 숫자 정보 입력
number_list = [INF] + list(map(int, input().split()))

# 쿼리 갯수 입력
query_number = int(input())

# 세그먼트 트리 리스트 선언 및 0 인덱스 0으로 초기화
seg_tree = [None for _ in range(1 << ceil(log2(number_amount)) + 1)]
seg_tree[0] = 0

# 함수를 호출하여 세그먼트 트리 구성
make_seg_tree(seg_tree, number_list, 1, number_amount)

# 출력 리스트 선언
output = []

for _ in range(query_number):

    # 쿼리 및 입력값 정보 입력
    query_type, input_1, input_2 = map(int, input().split())

    # 리스트 원소를 바꾸는 쿼리일 경우
    if query_type == 1:

        # 리스트 변경 후 함수를 호출하여 트리 갱신
        number_list[input_1] = input_2
        mod_min(seg_tree, number_list, 1, number_amount, input_1)

    # 범위 내 크기가 가장 작은 값의 인덱스를 출력하는 쿼리일 경우
    elif query_type == 2:

        # 함수를 호출하여 결과값을 출력 리스트에 추가
        output.append(find_min(seg_tree, number_list, 1, number_amount, input_1, input_2))

# 출력
for result in output:
    print(result)
