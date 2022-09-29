# 이항 계수 3

import sys

input = sys.stdin.readline

total_number, select_k = map(int, input().split())

modular = 1000000007

def factorial_modular(number_dict: dict, target_number: int, modular_number: int) -> int:
    
    if number_dict.get(target_number) is not None:
        return number_dict[target_number]

    else:
        length = len(number_dict.keys())

        for idx in range(length, target_number + 1):
            number_dict[idx] = (number_dict[idx - 1] * idx) % modular_number

        return number_dict[target_number]


def multiply_number(number_dict: dict, target_number: int, count: int, modular_number: int):

    if number_dict.get(count) is not None:
        return number_dict[count]

    else:
        mid = count // 2

        if number_dict.get(mid) is not None:
            number1 = number_dict[mid]
        else:
            number1 = multiply_number(number_dict, target_number, mid, modular_number)

        if number_dict.get(count - mid) is not None:
            number2 = number_dict[count - mid]
        else:
            number2 = multiply_number(number_dict, target_number, count - mid, modular_number)

        result = (number1 * number2) % modular_number
        number_dict[count] = result

        return result

def modular_division(number_1: int, number_2: int, modular_number: int) -> int:
    multiply_dict = {0: 1, 1: number_2 % modular_number}
    inverse_number = multiply_number(multiply_dict, number_2 % modular_number, modular_number - 2, modular_number)
    result = ((number_1 % modular_number) * inverse_number) % modular_number

    return result

factorial_dict = {0: 1, 1: 1}

total_number_factorial = factorial_modular(factorial_dict, total_number, modular)
select_k_factorial = factorial_modular(factorial_dict, select_k, modular)
other_factorial = factorial_modular(factorial_dict, total_number - select_k, modular)

result = modular_division(modular_division(total_number_factorial, select_k_factorial, modular), other_factorial, modular)

print(result)