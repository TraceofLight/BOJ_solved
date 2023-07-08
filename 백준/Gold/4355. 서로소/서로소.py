# 서로소 

import sys

input = sys.stdin.readline


def euler_phi(number: int) -> int:
    '''
    오일러 피 함수를 활용한 자연수 n과 서로소인 수의 갯수를 구하는 함수
    '''

    checker = 2
    result = number

    while pow(checker, 2) <= number:
        if not number % checker:
            while not number % checker:
                number //= checker

            result -= result // checker

        checker += 1

    if number > 1:
        result -= result // number

    return result


output = []

while True:
    target_number = int(input())

    if not target_number:
        break

    if target_number == 1:
        output.append(0)

    else:
        output.append(euler_phi(target_number))

for result in output:
    print(result)
