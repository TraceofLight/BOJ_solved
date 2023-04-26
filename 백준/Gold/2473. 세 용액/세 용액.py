# 세 용액

import sys

input = sys.stdin.readline

solution_number = int(input())
solution_list = list(map(int, input().split()))

solution_list.sort()
characteristic_value = 3000000000

for idx in range(solution_number):

    pointer_1 = 0
    pointer_2 = solution_number - 1

    while pointer_1 < pointer_2:

        if pointer_1 == idx:
            pointer_1 += 1
        if pointer_2 == idx:
            pointer_2 -= 1

        if pointer_1 >= pointer_2:
            break

        now_value = sum([solution_list[idx], solution_list[pointer_1], solution_list[pointer_2]])

        if abs(now_value) < characteristic_value:
            characteristic_value = abs(now_value)
            result = [solution_list[idx], solution_list[pointer_1], solution_list[pointer_2]]

            if not characteristic_value:
                break

        if now_value < 0:
            pointer_1 += 1
        elif now_value > 0:
            pointer_2 -= 1

    if not characteristic_value:
        break

result.sort()

print(*result)
