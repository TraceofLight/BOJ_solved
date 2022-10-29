# 합분해

import sys

input = sys.stdin.readline

# 목표 숫자 및 합산에 사용한 숫자 갯수 입력
target_number, integer_used = map(int, input().split())

# Dynamic Programming

# 합산 횟수별 각 숫자를 만드는 경우의 수를 담을 리스트 선언
arr_dp = [[0 for _ in range(target_number + 1)] for _ in range(integer_used + 1)]

# 1개의 숫자를 사용하여 숫자를 만드는 방법은 1가지
for idx in range(target_number + 1):
    arr_dp[1][idx] = 1

# 2개 이상의 숫자를 사용하는 모든 경우 대해서 조사
for used_count in range(2, integer_used + 1):

    # 모든 숫자에 대해 확인
    for now_target in range(target_number + 1):

        # 합이 해당 숫자보다 작은 이전 모든 숫자에서 1회의 추가 합산을 한다면 현재의 숫자를 만들 수 있음
        for last_number in range(now_target + 1):
            arr_dp[used_count][now_target] += arr_dp[used_count - 1][last_number]

            # 문제 조건에 따른 모듈로 연산
            arr_dp[used_count][now_target] %= 1000000000

# 목표횟수로 목표값을 만드는 경우의 수 결과값을 출력
print(arr_dp[integer_used][target_number])
