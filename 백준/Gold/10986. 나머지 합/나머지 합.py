# 나머지 합

import sys

input = sys.stdin.readline

# 수의 갯수, 나누는 수 input
number_amount, divide_number = map(int, input().split())

# 숫자 리스트 input
number_list = list(map(int, input().split()))

# 누적합을 나머지에 대해 분류할 리스트 선언
remainder_list = [0 for _ in range(divide_number)]

# 누적 제일 처음부터 진행할 경우에 대하여 카운팅
remainder_list[0] += 1

# 누적합 변수 선언
sum_number = 0

# 해당하는 index까지 누적합을 구해서 나머지를 리스트에 추가
for idx in range(number_amount):
    sum_number += number_list[idx]
    sum_number %= divide_number
    remainder_list[sum_number] += 1

# 결과값 변수 선언
answer = 0

# 누적합에서 나머지가 같은 것들을 2개 골라 빼면 나머지가 0이 됨
# 해당 가짓수만큼 결과값 카운트
for idx in range(divide_number):
    if remainder_list[idx]:
        temp = remainder_list[idx]
        answer += temp * (temp - 1) // 2

# 결과 출력
print(answer)
