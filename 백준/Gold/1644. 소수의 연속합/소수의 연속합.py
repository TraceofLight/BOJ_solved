# 소수의 연속합

import sys
from math import sqrt


input = sys.stdin.readline


# 어떤 숫자까지의 소수 리스트를 반환하는 함수 선언
def make_prime(last_number: int) -> list:

    # 결과 리스트 선언
    result_list = []

    # 기본적인 일부값을 제외하고 에라토스테네스의 체 사용
    for target_number in range(2, last_number + 1):

        # 2 혹은 3은 그냥 추가
        if target_number == 2 or target_number == 3:
            result_list.append(target_number)

        # 3보다 큰 값의 경우는 소수인지 확인
        else:

            # Flag 선언
            is_prime = True

            # 나누어 떨어질 경우 소수가 아님
            for checker in range(2, int(sqrt(target_number)) + 1):
                if not target_number % checker:
                    is_prime = False
                    break

            # 소수라면 리스트에 추가
            if is_prime:
                result_list.append(target_number)

    # 리스트 반환
    return result_list


# 연속합으로 나타낼 숫자 입력
input_number = int(input())

# 해당하는 숫자까지의 소수 리스트를 함수를 호출하여 선언
prime_list = make_prime(input_number)

# 리스트 전체 길이 확인
length = len(prime_list)

# 투 포인터 변수 및 현재 합산값 변수 선언
cursor_1 = 0
cursor_2 = 0
sum_number = 0

# 결과값 변수 선언
result_count = 0

# 투 포인터 알고리즘을 사용하여 합산값과 일치할 경우 카운팅
while cursor_1 < length:

    # 합산값이 입력 받은 숫자보다 작고 2번 커서를 움직일 수 있는 경우
    if sum_number < input_number and cursor_2 < length:

        # 2번을 밀어서 값을 늘림
        sum_number += prime_list[cursor_2]
        cursor_2 += 1

    # 합산값이 입력 받은 숫자보다 작고 2번 커서를 움직일 수 없는 경우
    elif sum_number < input_number and cursor_2 == length:
        break

    # 합산값이 입력 받은 숫자와 같거나 큰 경우
    elif sum_number >= input_number:

        # 1번 커서를 당겨서 값을 줄임
        sum_number -= prime_list[cursor_1]
        cursor_1 += 1

    # 수치가 일치하면 카운트 1
    if sum_number == input_number:
        result_count += 1

# 결과값 출력
print(result_count)
