# 17배

import sys

input = sys.stdin.readline

# 입력 2진수 숫자를 17배 연산
input_number = int(input(), 2)
multiple_number = 17 * input_number

# 결과를 2진수로 변환
result = str(bin(multiple_number))[2:]

# 출력
print(result)
