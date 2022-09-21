# 검문

import sys
from math import gcd

input = sys.stdin.readline

# 수의 갯수 input
number_amount = int(input())

# 수를 기록할 리스트 선언
number_list = []

# 계산 편의를 위해 나중에 추가할 첫번째 값 변수 선언 및 추가
first_init = int(input())
number_list.append(first_init)

# 마지막값까지 기록
for _ in range(number_amount - 1):
    temp = int(input())
    number_list.append(temp)

# 마지막에 첫번째 값을 다시 추가
number_list.append(first_init)

# 나머지를 전부 제거한 수를 얻어내어 리스트에 추가
sub_list = []
for idx in range(number_amount):
    sub_list.append(abs(number_list[idx] - number_list[idx + 1]))

# 해당 값들의 최대공약수 확인
gcd_result = gcd(*sub_list)

# 최대공약수의 모든 약수가 정답이므로 출력
if gcd_result >= 2:
    for number in range(2, gcd_result + 1):
        if not gcd_result % number:
            print(number, end=' ')
