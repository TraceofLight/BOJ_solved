# 핸드폰 요금

import sys
from math import ceil

input = sys.stdin.readline

# 통화 갯수 및 통화 시간 입력
call_number = int(input())
call_list = list(map(int, input().split()))

# 각 통화별 요금 청구량 계산
rate_plan_1 = [ceil((each_call + 1) / 30) * 10 for each_call in call_list]
rate_plan_2 = [ceil((each_call + 1) / 60) * 15 for each_call in call_list]

# 요금 합산 변수 선언
sum_plan_1 = sum(rate_plan_1)
sum_plan_2 = sum(rate_plan_2)

# 요금 합산에 비교에 따른 결과 출력
if sum_plan_1 < sum_plan_2:
    print('Y', sum_plan_1)

elif sum_plan_1 > sum_plan_2:
    print('M', sum_plan_2)

else:
    print('Y M', sum_plan_1)
