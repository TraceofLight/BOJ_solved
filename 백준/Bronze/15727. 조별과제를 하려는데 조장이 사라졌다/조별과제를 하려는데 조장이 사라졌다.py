# 조별과제를 하려는데 조장이 사라졌다

import sys

input = sys.stdin.readline

distance = int(input())

result = (distance // 5) if (distance % 5 == 0) else (distance // 5 + 1)

print(result)
