# 부분수열의 합 2

import sys
from collections import defaultdict

input = sys.stdin.readline

# 숫자 갯수 및 목표합 입력
number_amount, target_sum = map(int, input().split())

# 숫자 정보 입력
number_list = list(map(int, input().split()))

# 중간에서 만나기 알고리즘을 사용

# 길이 절반 변수 선언 및 숫자 절반을 담은 리스트를 추가로 선언
half_number_amount = number_amount // 2
half_number_list = number_list[half_number_amount :]

# 합산값을 기록할 딕셔너리 선언
value_dict = defaultdict(int)

# 결과값 변수 선언
result = 0

# 전반부 부분집합에 대해 조사
for set_number in range(1 << half_number_amount):

    # 현재 합산값 변수 선언
    sum = 0

    # 해당 케이스에 대해 자릿값이 겹치는 경우 값을 합산
    for each_idx in range(half_number_amount):
        if set_number & (1 << each_idx):
            sum += number_list[each_idx]

    # 목표값에서 합산값을 뺀 수를 딕셔너리에 추가, 해당값이 후반부에 출현할 시 카운팅 유도
    value_dict[target_sum - sum] += 1

# 후반부 부분집합에 대해 조사
for other_set_number in range(1 << number_amount - half_number_amount):

    # 현재 합산값 변수 선언
    other_sum = 0

    # 해당 케이스에 대해 자릿값이 겹치는 경우 값을 합산
    for other_each_idx in range(number_amount - half_number_amount):
        if other_set_number & (1 << other_each_idx):
            other_sum += half_number_list[other_each_idx]

    # 해당 합산값을 뺀 어떤 수가 딕셔너리에 존재한다면 해당 부분집합의 갯수만큼 카운팅
    if value_dict.get(other_sum):
        result += value_dict[other_sum]

# 목표합이 0일 경우 공집합 케이스를 배제
if not target_sum:
    result -= 1

# 결과 출력
print(result)
