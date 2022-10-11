# 구간 곱 구하기

import sys
from math import ceil, log2

input = sys.stdin.readline


def seg_tree_multiply(result_list: list, target_list: list, start: int, end: int, node: int = 1) -> int:
    '''
    구간의 곱을 기록하는 세그먼트 트리
    '''

    # 커서가 1개로 모인 경우
    if start == end:

        # 커서 주소에 위치한 리스트의 값을 기록
        result_list[node] = target_list[start]

    # 커서 범위가 있는 경우
    else:

        # 이분 탐색 알고리즘을 사용
        mid = (start + end) // 2

        # 자식 노드들의 곱을 기록
        result_list[node] = (
            seg_tree_multiply(result_list, target_list, start, mid, node * 2)
            * seg_tree_multiply(result_list, target_list, mid + 1, end, node * 2 + 1)
        ) % 1000000007

    # 부모 노드의 결과값 확인을 위해 결과 반환
    return result_list[node]

def find_multiply(tree_info: list, start: int, end: int, left: int, right: int, node: int = 1) -> int:
    '''
    세그먼트 트리와 범위가 주어졌을 때 해당 구간의 곱을 반환하는 함수
    '''

    # 범위를 벗어난 경우
    if start > right or end < left:

        # 곱셈의 항등원을 반환
        return 1

    # 범위 내에 전부 들어온 경우
    elif start >= left and end <= right:

        # 해당 노드값을 반환
        return tree_info[node]

    # 범위 내 일부만 존재하는 경우
    else:

        # 이분 탐색 알고리즘을 사용
        mid = (start + end) // 2

        # 범위를 나누어 조사 후 해당 값들을 곱연산
        result = (
            find_multiply(tree_info, start, mid, left, right, 2 * node)
            * find_multiply(tree_info, mid + 1, end, left, right, 2 * node + 1)
        ) % 1000000007

        # 최소값을 반환
        return result

def modify_seg_tree(tree_info: list, start: int, end: int, index: int, val: int, node: int = 1) -> None:
    '''
    리스트의 값이 변화했을 때 세그먼트 트리를 수정하는 함수
    '''

    # 인덱스가 범위 바깥에 존재하는 경우
    if start > index or end < index:

        # 종료
        return 

    # 포인터가 1개 주소를 나타내는 경우
    elif start == end:

        # 값 변경
        tree_info[node] = val

    # 포인터가 범위로 존재하는 경우
    else:

        # 이분 탐색 알고리즘을 활용
        mid = (start + end) // 2

        # 범위를 분할하여 재귀 함수를 호출, 트리를 반복 수정
        modify_seg_tree(tree_info, start, mid, index, val, node * 2)
        modify_seg_tree(tree_info, mid + 1, end, index, val, node * 2 + 1)

        # 현재 노드값 변경
        tree_info[node] = (tree_info[node * 2] * tree_info[node * 2 + 1]) % 1000000007


# 정수 갯수 및 범위 갯수 입력
number_amount, change_order, multiply_number = map(int, input().split())

# 정수 입력
number_list = [0]
for _ in range(number_amount):
    number_list.append(int(input()))

# 구간곱 정보를 담을 세그먼트 트리 리스트 선언
seg_tree_multi = [0 for _ in range(1 << ceil(log2(number_amount)) + 1)]

# 함수를 호출하여 세그먼트 트리 생성
seg_tree_multiply(seg_tree_multi, number_list, 1, number_amount)

# 출력 리스트 선언
output = []

for _ in range(change_order + multiply_number):

    # 명령 형태 및 입력값 2개 확인
    order_type, input_1, input_2 = map(int, input().split())

    # 리스트 숫자 변경의 경우
    if order_type == 1:

        # 리스트 변경 및 트리 변경
        number_list[input_1] = input_2
        modify_seg_tree(seg_tree_multi, 1, number_amount, input_1, input_2)

    # 구간곱의 경우
    elif order_type == 2:

        # 함수를 호출하여 세그먼트 트리를 활용, 범위 내 최소값을 확인
        min_number = find_multiply(seg_tree_multi, 1, number_amount, input_1, input_2)

        # 결과를 출력 리스트에 추가
        output.append(min_number)

# 출력
for result in output:
    print(result)
