# 소수

import sys

input = sys.stdin.readline


def find_target_degit(denominator, numerator, target_digit):
    """
    나눗셈을 실행했을 때, 소숫점 아래 N번째 자릿수를 구하는 함수
    """

    # 정수 부분 우선 처리
    denominator %= numerator

    # 카운팅 변수 선언
    counter = 0

    # 목표 자릿수까지 반복
    while counter <= target_digit:

        # 나눌 수 없는 경우 자릿수 추가 제공 및 카운팅
        while counter <= target_digit and denominator < numerator:
            denominator *= 10
            counter += 1

            # 나눌 수 없는 상태에서 목표 자릿수에 도달했다면 0 반환
            if counter == target_digit and denominator < numerator:
                return 0

        # 목표 자릿수에 도달한 경우 나눈 몫을 반환
        if counter == target_digit:
            result = denominator // numerator
            return result

        # 도달하지 않은 경우 나눠준 후 다시 반복
        else:
            denominator %= numerator


# 피제수, 제수, 목표 자릿수 입력
input_1, input_2, input_3 = map(int, input().split())

# 결과 출력
print((find_target_degit(input_1, input_2, input_3)))
