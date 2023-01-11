# Pyramids

import sys

input = sys.stdin.readline

output = []

while True:

    now_bottom_block = int(input())

    if not now_bottom_block:
        break

    else:

        sum_block = 0

        for block in range(now_bottom_block + 1):
            sum_block += block

        output.append(sum_block)

for result in output:
    print(result)
