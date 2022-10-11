# 최솟값과 최댓값

import sys

input = sys.stdin.readline

# INF 설정
INF = 2000000000

def seg_tree_big_number(result_list: list, target_list: list, start: int, end: int, node: int) -> int:
    '''
    해당 그룹에서 가장 큰 숫자를 기록하는 세그먼트 트리
    '''

    # 커서가 1개로 모인 경우
    if start == end:

        # 커서 주소에 위치한 리스트의 값을 기록
        result_list[node] = target_list[start]

    # 커서 범위가 있는 경우
    else:

        # 이분 탐색 알고리즘을 사용
        mid = (start + end) // 2

        # 자식 노드들의 결과값 중 최대값을 기록
        result_list[node] = max(
            seg_tree_big_number(result_list, target_list, start, mid, node * 2),
            seg_tree_big_number(result_list, target_list, mid + 1, end, node * 2 + 1)
        )

    # 부모 노드의 결과값 확인을 위해 결과 반환
    return result_list[node]

def seg_tree_small_number(result_list: list, target_list: list, start: int, end: int, node: int) -> int:
    '''
    해당 그룹에서 가장 큰 숫자를 기록하는 세그먼트 트리
    '''

    # 커서가 1개로 모인 경우
    if start == end:

        # 커서 주소에 위치한 리스트의 값을 기록
        result_list[node] = target_list[start]

    # 커서 범위가 있는 경우
    else:

        # 이분 탐색 알고리즘을 사용
        mid = (start + end) // 2

        # 자식 노드들의 결과값 중 최소값을 기록
        result_list[node] = min(
            seg_tree_small_number(result_list, target_list, start, mid, node * 2),
            seg_tree_small_number(result_list, target_list, mid + 1, end, node * 2 + 1)
        )

    # 부모 노드의 결과값 확인을 위해 결과 반환
    return result_list[node]

def find_max_number(tree_info: list, start: int, end: int, left: int, right: int, node: int) -> int:
    '''
    세그먼트 트리와 범위가 주어졌을 때 범위 내 가장 큰 수를 반환하는 함수
    '''

    # 범위를 벗어난 경우
    if start > right or end < left:

        # 정수 범위 내 최소값을 반환
        return -INF

    # 범위 내에 전부 들어온 경우
    elif start >= left and end <= right:

        # 해당 노드값을 반환
        return tree_info[node]

    # 범위 내 일부만 존재하는 경우
    else:
        
        # 이분 탐색 알고리즘을 사용
        mid = (start + end) // 2

        # 범위를 나누어 조사 후 최대값을 확인
        result = max(
            find_max_number(tree_info, start, mid, left, right, 2 * node),
            find_max_number(tree_info, mid + 1, end, left, right, 2 * node + 1)
        )

        # 최대값을 반환
        return result

def find_min_number(tree_info: list, start: int, end: int, left: int, right: int, node: int) -> int:
    '''
    세그먼트 트리와 범위가 주어졌을 때 범위 내 가장 작은 수를 반환하는 함수
    '''

    # 범위를 벗어난 경우
    if start > right or end < left:

        # 정수 범위 내 최대값을 반환
        return INF

    # 범위 내에 전부 들어온 경우
    elif start >= left and end <= right:

        # 해당 노드값을 반환
        return tree_info[node]

    # 범위 내 일부만 존재하는 경우
    else:

        # 이분 탐색 알고리즘을 사용
        mid = (start + end) // 2

        # 범위를 나누어 조사 후 최소값을 확인
        result = min(
            find_min_number(tree_info, start, mid, left, right, 2 * node),
            find_min_number(tree_info, mid + 1, end, left, right, 2 * node + 1)
        )

        # 최소값을 반환
        return result


# 정수 갯수 및 범위 갯수 입력
number_amount, check_number = map(int, input().split())

# 정수 입력
number_list = [0]
for _ in range(number_amount):
    number_list.append(int(input()))

# 최소, 최대값 정보를 가지는 세그먼트 트리 정보를 담을 리스트 선언
seg_tree_small = [None for _ in range(number_amount * 4 + 1)]
seg_tree_big = [None for _ in range(number_amount * 4 + 1)]

# 함수를 호출하여 세그먼트 트리 생성
seg_tree_small_number(seg_tree_small, number_list, 1, number_amount, 1)
seg_tree_big_number(seg_tree_big, number_list, 1, number_amount, 1)

# 출력 리스트 선언
output = []

for _ in range(check_number):

    # 범위 입력
    range_start, range_end = map(int, input().split())

    # 함수를 호출하여 세그먼트 트리를 활용, 범위 내 최대, 최소를 확인
    min_number = find_min_number(seg_tree_small, 1, number_amount, range_start, range_end, 1)
    max_number = find_max_number(seg_tree_big, 1, number_amount, range_start, range_end, 1)

    # 결과를 출력 리스트에 추가
    output.append([min_number, max_number])

# 출력
for result in output:
    print(*result)
