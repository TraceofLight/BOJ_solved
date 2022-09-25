# 부분합

import sys

input = sys.stdin.readline

number_amount, min_sum = map(int, input().split())
number_list = list(map(int, input().split()))

first_cursor = 0
second_cursor = 0

sum_number = 0
min_length = 2000000000
length = 0
while first_cursor != number_amount - 1:
    if sum_number < min_sum:
        if second_cursor < number_amount:
            sum_number += number_list[second_cursor]
            second_cursor += 1
            length += 1
            if sum_number >= min_sum:
                if min_length > length:
                    min_length = length
        else:
            break

    else:
        sum_number -= number_list[first_cursor]
        first_cursor += 1
        length -= 1
        if sum_number >= min_sum:
            if min_length > length:
                min_length = length

if min_length == 2000000000:
    print(0)
else:
    print(min_length)
