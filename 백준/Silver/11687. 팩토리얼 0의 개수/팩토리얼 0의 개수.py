# 팩토리얼 0의 개수

import sys

input = sys.stdin.readline


def factorial_zero(target_number: int) -> int:
    '''
    팩토리얼 내 5의 갯수를 확인하여 0의 갯수를 카운팅하는 함수
    '''

    # 카운터 선언
    count_five = 0

    # 초기값 설정
    check_number = target_number

    # 0이 될 때까지 나누고 합산 반복
    while check_number:
        check_number //= 5
        count_five += check_number

    # 카운터 반환
    return count_five

def binary_search_factorial(target_number: int, start: int, end: int) -> int:
    '''
    이분탐색을 통해 해당 0의 갯수를 가지는 팩토리얼 최솟값을 반환하는 함수
    '''

    # 좌우 범위값 선언
    left = start
    right = end

    # 좌우값이 같아질 때까지 진행
    while left != right:

        # 중앙값 선언
        mid = (left + right) // 2

        # 해당값의 0의 갯수 확인
        check_result = factorial_zero(mid)

        # 목표치보다 많거나 같게 가지고 있다면 상방을 내림
        if check_result >= target_number:
            right = mid

        # 목표치보다 적다면 하방을 올림
        else:
            left = mid + 1

    # 탐색된 값이 목표치와 같다면 해당 포인터의 값을 반환
    if factorial_zero(left) == target_number:
        return left

    # 아니라면 -1을 반환
    else:
        return -1


# 가장 끝 0의 갯수 입력
zero_number = int(input())

# 함수를 호출하여 결과 확인 후 출력
print(binary_search_factorial(zero_number, 1, 1000000000))
