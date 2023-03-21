# 팩토리얼 3

import sys

input = sys.stdin.readline

result = 1
target = int(input())

for num in range(1, target + 1):
    result *= num
    
print(result)
