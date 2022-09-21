# 내려가기

import sys

input = sys.stdin.readline

line_number = int(input())

# 첫 줄 숫자 input
num1, num2, num3 = map(int, input().split())

# 첫 줄 숫자를 기본값으로 한 딕셔너리 형성
get_down_dict = {
    (1, 'maximum'): num1,
    (2, 'maximum'): num2,
    (3, 'maximum'): num3,
    (1, 'minimum'): num1,
    (2, 'minimum'): num2,
    (3, 'minimum'): num3,
}

# 윗 줄까지의 합 중 가능한 범위에서 max값과 min값 중에 가장 크거나 작은 것을 골라 합산
for _ in range(line_number - 1):
    num1, num2, num3 = map(int, input().split())
    result_max1 = max(get_down_dict[(1, 'maximum')], get_down_dict[(2, 'maximum')])
    result_max2 = max(get_down_dict[(1, 'maximum')], get_down_dict[(2, 'maximum')], get_down_dict[(3, 'maximum')])
    result_max3 = max(get_down_dict[(2, 'maximum')], get_down_dict[(3, 'maximum')])
    result_min1 = min(get_down_dict[(1, 'minimum')], get_down_dict[(2, 'minimum')])
    result_min2 = min(get_down_dict[(1, 'minimum')], get_down_dict[(2, 'minimum')], get_down_dict[(3, 'minimum')])
    result_min3 = min(get_down_dict[(2, 'minimum')], get_down_dict[(3, 'minimum')])
    get_down_dict[(1, 'maximum')] = num1 + result_max1
    get_down_dict[(2, 'maximum')] = num2 + result_max2
    get_down_dict[(3, 'maximum')] = num3 + result_max3
    get_down_dict[(1, 'minimum')] = num1 + result_min1
    get_down_dict[(2, 'minimum')] = num2 + result_min2
    get_down_dict[(3, 'minimum')] = num3 + result_min3

# 최대값 및 최소값 변수 선언
max_score = 0
min_score = 1000000

# 갱신 과정
for sum_number in get_down_dict.values():
    if sum_number > max_score:
        max_score = sum_number
    if sum_number < min_score:
        min_score = sum_number

# 출력
print(max_score, min_score)
