# 건너 아는 사이

import sys
from math import sqrt, ceil

input = sys.stdin.readline


def prime_graph(last_target: int, prime_list: list = [2]) -> int:
    '''
    건너 아는 사이의 음식값의 최소값을 반환하는 함수
    '''

    # 반환할 결과 변수 선언
    result_sum = 0

    # 2부터 목표까지의 모든 수에 대해서 확인
    for target_number in range(2, last_target + 1):

        # 짝수는 2에 연결하면 항상 최소값
        if not target_number % 2:
            result_sum += 2

        # 짝수가 아닌 경우
        else:

            # 소수 리스트의 인덱스 변수 선언
            idx_counter = 0

            # 소수 연산 Flag 선언
            is_divided = False

            # 에라토스테네스의 체
            for divide_number in range(2, ceil(sqrt(target_number)) + 1):

                # Pruning
                # 그 수의 제곱근 이전의 소수들에 대해서만 체크
                if prime_list[idx_counter] == divide_number:

                    # 소수로 나누어졌다면 최소한 소수가 아니므로 나눌 수 있는 가장 작은 소수와 연결하면 최소값
                    if not target_number % divide_number:
                        is_divided = True
                        result_sum += divide_number
                        break

                    # 나눌 대상 소수를 변경
                    else:           
                        idx_counter += 1

            # 나누어지지 않았다면 소수이므로 리스트에 추가하고 해당 소수를 합산
            if not is_divided:
                prime_list.append(target_number)
                result_sum += target_number

    # 결과값 반환
    return result_sum


# 사람 수 입력
people_number = int(input())

# 함수를 호출하여 결과 출력
print(prime_graph(people_number))
