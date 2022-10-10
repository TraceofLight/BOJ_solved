# 구간 합 구하기

import sys

input = sys.stdin.readline


def make_seg_tree(result_list: list, target_list: list, start: int, end: int, node: int) -> int:
    '''
    주어진 리스트를 기반으로 구간합 세그먼트 트리를 만들어주는 함수
    '''

    # 커서가 1개로 조여진 경우
    if start == end:

        # 리스트의 값을 노드값으로 지정
        result_list[node] = target_list[start]

    # 커서가 범위를 나타내는 경우
    else:

        # 이분 탐색 알고리즘을 사용
        mid = (start + end) // 2
        
        # 자식 노드들의 합을 해당 노드의 값으로 지정
        result_list[node] = (
            make_seg_tree(result_list, target_list, start, mid, node * 2)
            + make_seg_tree(result_list, target_list, mid + 1, end, node * 2 + 1)
        )

    # 노드의 값을 반환하여 재귀에 활용
    return result_list[node]

def sum_seg_tree(tree_info: list, start: int, end: int, left: int, right: int, node: int) -> int:
    '''
    구간 범위와 세그먼트 트리가 주어졌을 때 구간합을 반환하는 함수
    '''

    # 찾는 구간이 범위에 없는 경우
    if left > end or right < start:

        # 0을 반환
        return 0

    # 전 구간이 범위에 들어온 경우
    elif left <= start and end <= right:

        # 해당 값을 그대로 반환
        return tree_info[node]

    # 일부 구간만 범위에 존재하는 경우
    else:

        # 이분 탐색 알고리즘을 사용
        mid = (start + end) // 2

        # 구간을 세분화하여 합산
        result = (
            sum_seg_tree(tree_info, start, mid, left, right, 2 * node)
            + sum_seg_tree(tree_info, mid + 1, end, left, right, 2 * node + 1)
        )

        # 합산값을 반환
        return result

def mod_seg_tree(tree_info: list, start: int, end: int, index: int, val: int, node: int) -> None:
    '''
    세그먼트 트리의 값을 변경하는 함수
    '''

    # 찾는 인덱스가 범위에 없는 경우
    if index < start or end < index:

        # 그대로 종료
        return

    # 찾는 인덱스가 구간에 존재하는 경우
    else:

        # 해당 노드에 변경값을 반영
        tree_info[node] += val

        # 커서가 1개로 조여지지 않은 경우
        if start != end:

            # 이분 탐색 알고리즘을 사용
            mid = (start + end) // 2

            # 자식 노드들에 대해서 재귀 함수를 호출하여 조사
            mod_seg_tree(tree_info, start, mid, index, val, node * 2)
            mod_seg_tree(tree_info, mid + 1, end, index, val, node * 2 + 1)


# 출력 리스트 선언
output = []

# 숫자 입력 갯수, 변경 및 합산 명령 횟수 입력
number_amount, change_amount, sum_amount = map(int, input().split())

# 숫자 정보 입력
number_list = [0]
for _ in range(number_amount):
    number_list.append(int(input()))

# 세그먼트 트리 리스트 선언
seg_tree = [None for _ in range(number_amount * 4 + 1)]

# 주어진 정보를 바탕으로 함수를 호출하여 세그먼트 트리 생성
make_seg_tree(seg_tree, number_list, 1, number_amount, 1)

# 명령 입력
for _ in range(change_amount + sum_amount):

    # 명령문 종류 및 입력값 2개 확인
    order_type, input_1, input_2 = map(int, input().split())

    # 숫자를 변경하는 명령의 경우
    if order_type == 1:

        # 기존 숫자와의 차이를 확인 및 리스트에 반영
        mod_val = input_2 - number_list[input_1]
        number_list[input_1] = input_2

        # 세그먼트 트리에 변경된 숫자 반영
        mod_seg_tree(seg_tree, 1, number_amount, input_1, mod_val, 1)

    # 구간합을 구하는 명령의 경우
    elif order_type == 2:

        # 함수를 호출하여 구간합 결과를 출력 리스트에 추가
        output.append(sum_seg_tree(seg_tree, 1, number_amount, input_1, input_2, 1))

# 출력
for result in output:
    print(result)
