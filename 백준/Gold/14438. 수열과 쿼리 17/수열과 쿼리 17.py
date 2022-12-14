# 수열과 쿼리 17

import sys
from math import ceil, log2

input = sys.stdin.readline


def make_segtree(target_list: list, result_list: list, start: int, end:int, now_node: int) -> int:
    '''
    최소 숫자 정보를 담는 세그먼트 트리를 생성하는 함수
    '''

    # 포인터가 한 곳으로 모인 경우
    if start == end:

        # 해당 노드는 포인터가 가리키는 인덱스의 값과 동일
        result_list[now_node] = target_list[start]

    # 포인터가 범위를 나타내는 경우
    else:

        # Devide and Conquer Algorithm

        # 중간 지점 선언
        mid = (start + end) // 2

        # 중간 지점을 기준으로 구간을 분할하여 최소값으로 갱신
        val_1 = make_segtree(target_list, result_list, start, mid, 2 * now_node)
        val_2 = make_segtree(target_list, result_list, mid + 1, end, 2 * now_node + 1)

        # 두 구간의 최소값을 비교하여 둘 중 최소값을 현재 노드에 기록
        result_list[now_node] = min(val_1, val_2)

    # 현재 노드의 값을 반환
    return result_list[now_node]

def find_min_number(target_tree: list, start: int, end: int, left: int, right: int, now_node: int) -> int:
    '''
    해당 구간의 최소값을 찾는 함수
    '''

    # 범위 내로 포인터가 좁혀진 경우
    if left <= start and right >= end:

        # 현재 노드값을 반환
        return target_tree[now_node]

    # 범위를 아예 벗어난 경우
    elif left > end or right < start:

        # None 값을 반환
        return None

    # 범위가 걸친 경우
    else:

        # Devide and Conquer Algorithm

        # 중간 지점 선언
        mid = (start + end) // 2

        # 중간 지점을 기준으로 구간을 분할하여 값을 확인
        val_1 = find_min_number(target_tree, start, mid, left, right, 2 * now_node)
        val_2 = find_min_number(target_tree, mid + 1, end, left, right, 2 * now_node + 1)

        # 반환된 값들 중 None이 존재하는 경우
        if val_1 is None and val_2 is None:
            return None

        elif val_1 is None:
            return val_2

        elif val_2 is None:
            return val_1

        # None이 없다면
        else:

            # 두 구간의 최소값 중에서 더 작은 값을 반환
            return min(val_1, val_2)

def change_segtree(target_tree: list, start: int, end: int, target_idx: int, target_val: int, now_node: int) -> None:
    '''
    리스트에 생긴 변경점을 트리에 반영하는 함수
    '''
    
    # 포인터가 한 곳으로 모인 경우
    if start == end:

        # 목표로 하는 인덱스랑 동일하다면 변경값을 반영
        if start == target_idx:
            target_tree[now_node] = target_val

    # 포인터가 범위로 주어진 경우
    else:

        # 목표 인덱스가 범위 내에 존재할 경우에만 갱신 가능성 존재
        if start <= target_idx <= end:

            # Devide and Conquer Algorithm

            # 중간 지점 선언
            mid = (start + end) // 2

            # 중간 지점을 기준으로 변경될 수 있는 인덱스를 재조사
            change_segtree(target_tree, start, mid, target_idx, target_val, 2 * now_node)
            change_segtree(target_tree, mid + 1, end, target_idx, target_val, 2 * now_node + 1)

        # 하위 노드들의 갱신이 진행된 이후 현재 노드의 갱신 진행
        target_tree[now_node] = min(target_tree[2 * now_node], target_tree[2 * now_node + 1])


# 수열의 크기 및 수열 정보 입력
target_length = int(input())
target_arr = ['*'] + list(map(int, input().split()))

# 수열의 구간 최소 숫자를 담을 세그먼트 트리 리스트 선언
segtree_arr = [None for _ in range(pow(2, ceil(log2(target_length) + 1)))]

# 함수를 호출하여 트리 생성
make_segtree(target_arr, segtree_arr, 1, target_length, 1)

# 퀴리 갯수 입력 및 출력 리스트 선언
query_number = int(input())
output = []

# 쿼리 실행
for _ in range(query_number):

    # 각 쿼리의 정보
    order_type, num_1, num_2 = map(int, input().split())

    # 타입 1의 경우
    if order_type == 1:

        # 리스트 값을 변경 및 함수를 호출하여 트리에 반영
        target_arr[num_1] = num_2
        change_segtree(segtree_arr, 1, target_length, num_1, num_2, 1)

    # 타입 2의 경우
    elif order_type == 2:

        # 함수를 호출하여 해당 구간의 최소 숫자를 출력 리스트에 추가
        output.append(find_min_number(segtree_arr, 1, target_length, num_1, num_2, 1))

# 결과 출력
for result in output:
    print(result)
