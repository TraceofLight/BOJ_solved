# 서버실

import sys
from bisect import bisect_left

input = sys.stdin.readline

server_room_size = int(input())
server_rack = pow(server_room_size, 2)

stack_list = []
total_computer = 0

for _ in range(server_room_size):
    temp = list(map(int, input().split()))

    for idx in range(server_room_size):
        stack_list.append(temp[idx])
        total_computer += temp[idx]

stack_list.sort()

half_activate = (total_computer + 1) // 2
now_activate = 0
min_counter = 0

while now_activate < half_activate:
    min_counter += 1
    now_activate += server_rack - bisect_left(stack_list, min_counter)

print(min_counter)
