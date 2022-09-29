# 이항 계수 3

import sys

input = sys.stdin.readline

# N, K 변수 선언
total_number, select_k = map(int, input().split())

# 모듈러 상수 선언
modular = 1000000007


# 팩토리얼 값의 모듈러 연산 값을 타뷸레이션 정리하고 값을 반환하는 함수 선언
def factorial_modular(number_dict: dict, target_number: int, modular_number: int) -> int:

    # 이미 딕셔너리에 값이 존재하는 경우 값을 반환
    if number_dict.get(target_number) is not None:
        return number_dict[target_number]

    # 존재하지 않는 경우 기존 값들을 전부 연산하면서 값을 저장
    else:

        # 전체 길이 확인
        length = len(number_dict.keys())

        # 현재 값이 존재하는 이후 범위에 대해 연산
        for idx in range(length, target_number + 1):
            number_dict[idx] = (number_dict[idx - 1] * idx) % modular_number

        # 결과 반환
        return number_dict[target_number]

# 분할 정복을 통해 제곱 수를 빠르게 연산 후 반환하는 함수 선언
def multiply_number(number_dict: dict, target_number: int, count: int, modular_number: int):

    # 딕셔너리에 이미 있는 경우 해당 값을 반환
    if number_dict.get(count) is not None:
        return number_dict[count]

    # 아직 없는 경우 분할 정복으로 연산하면서 값을 저장
    else:

        # 카운트 절반 변수 선언
        mid = count // 2

        # 숫자를 반으로 나눠서 곱연산
        # 이미 있는 수들이면 딕셔너리에서 값을 불러와서 진행

        # 절반에 대한 값 확인
        if number_dict.get(mid) is not None:
            number1 = number_dict[mid]
        else:
            number1 = multiply_number(number_dict, target_number, mid, modular_number)

        # 절반을 뺀 나머지에 대한 값 확인
        if number_dict.get(count - mid) is not None:
            number2 = number_dict[count - mid]
        else:
            number2 = multiply_number(number_dict, target_number, count - mid, modular_number)

        # 두 값을 곱연산 후 모듈러 상수에 대해 정리
        result = (number1 * number2) % modular_number

        # 딕셔너리에 연산 완료된 값 추가 후 반환
        number_dict[count] = result
        return result

# 모듈러 역원을 활용한 나눗셈 연산을 진행하는 함수 선언
def modular_division(number_1: int, number_2: int, modular_number: int) -> int:

    # (상수 - 2)번 제곱 연산을 위한 딕셔너리 선언
    multiply_dict = {0: 1, 1: number_2 % modular_number}

    # 페르마의 소정리를 통해 역원 도출
    inverse_number = multiply_number(multiply_dict, number_2 % modular_number, modular_number - 2, modular_number)

    # 역원 곱연산 진행 후 결과 반환
    result = ((number_1 % modular_number) * inverse_number) % modular_number
    return result


# 팩토리얼 값을 담을 딕셔너리 선언
factorial_dict = {0: 1, 1: 1}

# N!, K!, (N - K)!의 값을 담은 변수를 함수 호출을 통해 값을 얻어 선언
factorial_n = factorial_modular(factorial_dict, total_number, modular)
factorial_k = factorial_modular(factorial_dict, select_k, modular)
factorial_n_k = factorial_modular(factorial_dict, total_number - select_k, modular)

# 나눗셈 연산 함수를 호출하여 연산 진행
result = modular_division(modular_division(factorial_n, factorial_k, modular), factorial_n_k, modular)

# 결과 출력
print(result)
