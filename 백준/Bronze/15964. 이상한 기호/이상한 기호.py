# 이상한 기호

import sys

input = sys.stdin.readline

# 숫자 2개 input
num1, num2 = map(int, input().split())

# 연산 결과 출력
print((num1 + num2) * (num1 - num2))
