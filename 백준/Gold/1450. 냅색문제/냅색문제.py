# 냅색문제

import sys
from collections import defaultdict
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

# 물건 갯수, 최대 무게 입력
stuff_number, max_weight = map(int, input().split())

# 물건 목록 입력
stuff_list = list(map(int, input().split()))

# 최대 무게가 0이라면 안 담는 경우 1가지만 존재
if not max_weight:
    print(1)

# 최대 무게가 0이 아닐 경우
else:

    # 부분집합의 무게 종류 집합 선언
    weight_types = set()

    # 길이 절반 변수 선언
    half_length = stuff_number // 2

    # 물건 리스트 반으로 분할
    half_stuff = stuff_list[: stuff_number // 2]
    other_half_stuff = stuff_list[stuff_number // 2 :]

    # 기본값이 0으로 정해진 합산값을 넣을 딕셔너리 선언
    sum_dict = defaultdict(int)

    # 비트마스킹을 활용한 부분집합 체크
    for combination in range(1 << half_length):

        # 합산값 변수 선언
        now_sum = 0

        # 모든 원소들에 대해 조사
        for now_idx in range(half_length):

            # 해당 부분집합에 포함이라면 합산
            if combination & (1 << now_idx):
                now_sum += half_stuff[now_idx]

        # 최대 무게 이하라면 해당값을 딕셔너리에 카운팅
        if now_sum <= max_weight:
            sum_dict[now_sum] += 1
            weight_types.add(now_sum)

    # 나머지 반의 부분집합 합산값을 담을 리스트 선언
    other_sum_list = []

    # 나머지 절반에 대해서 부분집합 체크
    for other_combination in range(1 << stuff_number - half_length):

        # 합산값 변수 선언
        other_sum = 0

        # 남은 절반에 대해서도 부분집합 조사
        for now_idx in range(stuff_number - half_length):

            # 해당 부분집합에 포함된 원소라면 합산
            if other_combination & (1 << now_idx):
                other_sum += other_half_stuff[now_idx]

        # 최대 무게 이하일 경우 리스트에 추가
        if other_sum <= max_weight:
            other_sum_list.append(other_sum)

    # 전체 결과 변수 선언
    case_result = 0

    # 첫 절반 무게 종류 리스트 정렬
    weight_types = sorted(list(weight_types))
    
    # 나머지 절반 무게 리스트 정렬
    other_sum_list.sort()

    # 나올 수 있는 모든 무게 경우의 수에 대해 조사
    for first_weight in weight_types:

        # 이분탐색을 통해 최대 무게 한도까지 경우의 수 확인
        count_case = bisect_right(other_sum_list, max_weight - first_weight)

        # 첫 번째 무게가 한도에 도달한 경우 break
        if not count_case:
            break

        # 해당 인덱스 범위에 대해 전체 합산
        case_result += sum_dict[first_weight] * count_case

    # 결과 출력
    print(case_result)
