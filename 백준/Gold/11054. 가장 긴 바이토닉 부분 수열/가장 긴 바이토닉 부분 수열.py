# 가장 긴 바이토닉 부분 수열

import sys

input = sys.stdin.readline

number_amount = int(input())

number_list = list(map(int, input().split()))

number_dict = {idx: [number_list[idx], 1] for idx in range(number_amount)}

for idx in range(number_amount):
    number_dict_value = list(number_dict.values())
    for last_idx in range(idx):
        last_number, length = number_dict_value[last_idx]
        if last_number < number_list[idx]:
            next_number, next_length = number_dict[idx]
            if next_length < length + 1:
                number_dict[idx] = [next_number, length + 1]

rev_number_list = list(reversed(number_list))

rev_number_dict = {idx: [rev_number_list[idx], 1] for idx in range(number_amount)}

for idx in range(number_amount):
    rev_number_dict_value = list(rev_number_dict.values())
    for last_idx in range(idx):
        last_number, length = rev_number_dict_value[last_idx]
        if last_number < rev_number_list[idx]:
            next_number, next_length = rev_number_dict[idx]
            if next_length < length + 1:
                rev_number_dict[idx] = [next_number, length + 1]

max_length_list = [element[1] for element in number_dict.values()] 
rev_max_length_list = [element[1] for element in rev_number_dict.values()] 

bitonic_arr = []

for idx in range(number_amount):
    bitonic_arr.append(max_length_list[idx] + rev_max_length_list[number_amount - idx - 1])

print(max(bitonic_arr) - 1)
