# 2023년이 기대되는 이유

import sys

input = sys.stdin.readline


def pow_target(target_num: int, exponent: int) -> int:

    result = 0

    now_number = target_num

    while now_number:
        result += pow((now_number % 10), exponent)
        now_number //= 10

    return result


testcase = int(input())
result_dict = dict()
output = []

for _ in range(testcase):

    target_number = input().rstrip('\n')

    if result_dict.get(target_number) is not None:
        output.append(result_dict[target_number])

    else:

        is_under_limit = True

        for each_element in list(target_number):
            if int(each_element) > 1:
                is_under_limit = False
                break

        if is_under_limit:
            result_dict[target_number] = 'Hello, BOJ 2023!'
            output.append('Hello, BOJ 2023!')
            continue

        length = len(target_number)

        check_list = []
        check_list.append(int(target_number))

        for i in range(1, 1 << length):

            calc_result = 0

            now_start = 0
            now_end = 0

            for j in range(length):

                if i & (1 << j):
                    now_end = j
                    if now_end:
                        calc_result += int(target_number[now_start : now_end])
                    now_start = now_end
                    
            calc_result += int(target_number[now_start : length + 1])

            if calc_result not in check_list:
                check_list.append(calc_result)

        else:
            result = 0

            check_amount = len(check_list)
            check_list.sort()

            max_value = check_list[-1]
            pointer = 0
            counter = 1

            while pointer < check_amount:
                now_result = pow_target(int(target_number), counter)

                # 종료 조건 1
                if now_result > max_value:
                    break

                while pointer < check_amount and now_result > check_list[pointer]:
                    pointer += 1

                # 종료 조건 2
                if pointer >= check_amount:
                    break

                if now_result == check_list[pointer]:
                    result += 1

                counter += 1

            result_dict[target_number] = result
            output.append(result)

for result in output:
    print(result)
