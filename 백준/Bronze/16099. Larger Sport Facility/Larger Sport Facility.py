# Larger Sport Facility

import sys

input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):

    length_1, height_1, length_2, height_2 = map(int, input().split())

    if length_1 * height_1 == length_2 * height_2:
        print("Tie")

    elif length_1 * height_1 > length_2 * height_2:
        print("TelecomParisTech")

    else:
        print("Eurecom")
