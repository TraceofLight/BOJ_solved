# ゾロ目 (Same Numbers)

import sys

input = sys.stdin.readline

input_number = int(input())

if input_number % 10 == input_number // 10:
    print(1)
else:
    print(0)
