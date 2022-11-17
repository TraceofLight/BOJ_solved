# 적어도 대부분의 배수

import sys
from math import lcm
from itertools import combinations

input = sys.stdin.readline

# 숫자 리스트 입력
number_list = list(map(int, input().split()))

# 최소 공배수의 최소값을 나타낼 변수 선언
min_lcm = 1000000

# 5개의 숫자 중 3개를 고르는 모든 경우에 대해 조사
for numbers in combinations(number_list, 3):

    # 3개의 수의 최소공배수 확인
    lcm_result = lcm(*numbers)

    # 최소공배수가 기존 최소값보다 작다면 갱신
    if min_lcm > lcm_result:
        min_lcm = lcm_result

# 결과값을 출력
print(min_lcm)
