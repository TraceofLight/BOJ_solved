# 두 용액

import sys

input = sys.stdin.readline

liquid_number = int(input())
liquid_list = list(map(int, input().split()))

sorted_list = sorted(liquid_list)

first_cursor = 0
second_cursor = liquid_number - 1

min_sum = 2000000000
two_liquid = None

while first_cursor != second_cursor:
    result = sorted_list[first_cursor] + sorted_list[second_cursor]
    if min_sum > abs(result):
        min_sum = abs(result)
        two_liquid = [sorted_list[first_cursor], sorted_list[second_cursor]]
        if not result:
            break
    if result > 0:
        second_cursor -= 1
    elif result < 0:
        first_cursor += 1

print(*two_liquid)
