# Σ

import sys
from math import gcd

input = sys.stdin.readline

# 주사위 갯수 input
dice_amount = int(input())


# 이분탐색을 통한 큰수 제곱 연산 함수 선언
def big_multiple(count_dict: dict, number: int, count: int, modular_var: int):
    if count_dict.get(count) is not None:
        return count_dict[count]
    else:
        if count_dict.get(count // 2) is None:
            var1 = big_multiple(count_dict, number, count // 2, modular_var)
        else:
            var1 = count_dict[count // 2]
        if count_dict.get(count - (count // 2)) is None:
            var2 = big_multiple(count_dict, number, count - (count // 2), modular_var)
        else:
            var2 = count_dict[count - (count // 2)]
        count_dict[count] = (var1 * var2) % modular_var
        return count_dict[count]


# 분모, 분자 변수 선언
denominator = 0
numerator = 0

# 모듈러 변수 선언
modular_number = 1000000007

# 주사위 면 갯수, 주사위 수 전체 합 input 및 분수 합산 진행
for idx in range(dice_amount):

    # 주사위 정보 input
    dice_dimension, sum_dice = map(int, input().split())

    # 초기값 입력
    if not idx:
        denominator = dice_dimension // gcd(dice_dimension, sum_dice)
        numerator = sum_dice // gcd(dice_dimension, sum_dice)

    # 초기값이 아닌 나머지 연산
    else:
        denominator_lcm = (denominator * dice_dimension) % modular_number
        numerator = (sum_dice * denominator + numerator * dice_dimension) % modular_number
        denominator = denominator_lcm

        # 역원 연산의 큰수 제곱 연산을 위한 딕셔너리 선언
        gcd_number = gcd(numerator, denominator)
        abbreviation_dict = {0: 1, 1: gcd_number}

        inverse_gcd = big_multiple(abbreviation_dict, gcd_number, modular_number - 2, modular_number)

        # 기약분수화 (역원 연산)
        denominator = (inverse_gcd * denominator) % modular_number
        numerator = (inverse_gcd * numerator) % modular_number

# 함수를 호출하기 위한 딕셔너리 선언 및 기본값 설정
dice_dict = {0: 1, 1: denominator}

# 함수를 호출하여 결과를 연산
result = (big_multiple(dice_dict, denominator, modular_number - 2, modular_number) * numerator) % modular_number

# 결과 출력
print(result)
