# 0 만들기

import sys

input = sys.stdin.readline


def make_sum_zero(
    result_arr: set,
    target_arr: list,
    last_index: int,
    now_index: int = 0,
    sum_now: int = 0,
    now_calc: int = 0,
    log=[],
) -> None:
    if last_index == now_index:
        if not sum_now + now_calc:
            result_arr.add("".join(log))

    else:
        if not now_index:
            make_sum_zero(
                result_arr,
                target_arr,
                last_index,
                now_index + 1,
                0,
                target_arr[now_index],
                [str(target_arr[now_index])],
            )

        else:
            new_number = target_arr[now_index]

            make_sum_zero(
                result_arr,
                target_arr,
                last_index,
                now_index + 1,
                sum_now + now_calc,
                new_number,
                log + ["+", str(new_number)],
            )
            make_sum_zero(
                result_arr,
                target_arr,
                last_index,
                now_index + 1,
                sum_now + now_calc,
                -new_number,
                log + ["-", str(new_number)],
            )

            if now_calc < 0:
                make_sum_zero(
                    result_arr,
                    target_arr,
                    last_index,
                    now_index + 1,
                    sum_now,
                    10 * now_calc - new_number,
                    log + [" ", str(new_number)],
                )
            else:
                make_sum_zero(
                    result_arr,
                    target_arr,
                    last_index,
                    now_index + 1,
                    sum_now,
                    10 * now_calc + new_number,
                    log + [" ", str(new_number)],
                )


testcase = int(input())
output = []

for _ in range(testcase):
    arr_length = int(input())
    result = set()

    target_arr = [i for i in range(1, arr_length + 1)]
    make_sum_zero(result, target_arr, arr_length)

    sort_result = sorted(list(result), key=lambda x: ascii(x))
    output.append(sort_result)

for idx in range(testcase):
    for element_idx in range(len(output[idx])):
        print(output[idx][element_idx])

    if idx != testcase - 1:
        print("")
