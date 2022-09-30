# 부분수열의 합

import sys

input = sys.stdin.readline

# 숫자 갯수 및 목표합 입력
number_amount, target_sum = map(int, input().split())

# 숫자 정보 입력
number_list = list(map(int, input().split()))

# 결과값 변수 선언
result = 0

# 공집합을 제외한 부분집합에 대해 조사
for set_number in range(1, 1 << number_amount):

    # 현재 합산값 변수 선언
    sum = 0

    # 해당 케이스에 대해 자릿값이 겹치는 경우 값을 합산
    for each_idx in range(number_amount):
        if set_number & (1 << each_idx):
            sum += number_list[each_idx]

    # 합산값이 목표합과 일치한다면 카운팅
    if sum == target_sum:
        result += 1

# 결과 출력
print(result)
