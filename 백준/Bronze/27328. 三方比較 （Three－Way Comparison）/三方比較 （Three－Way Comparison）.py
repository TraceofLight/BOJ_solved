# 三方比較 (Three-Way Comparison)

import sys

input = sys.stdin.readline

a = int(input())
b = int(input())

if a > b:
    print(1)
    
elif a == b:
    print(0)
    
elif a < b:
    print(-1)
