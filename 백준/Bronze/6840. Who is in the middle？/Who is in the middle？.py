# Who is in the middle?

import sys

input = sys.stdin.readline

bear_Arr = []

for _ in range(3):
    bear_Arr.append(int(input()))

bear_Arr.sort()

print(bear_Arr[1])
