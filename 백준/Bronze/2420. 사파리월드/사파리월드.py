# 사파리월드

import sys

# 두 도메인의 유명도 input
num1, num2 = map(int, sys.stdin.readline().split())
# abs 함수를 통해 결과값 도출
result = abs(num1 - num2)
# 출력
print(result)
