# 줄번호

import sys

input = sys.stdin.readline

# 줄 번호 입력
line_number = int(input())

# 출력 리스트 선언
output = []

# 출력 리스트에 줄 번호 정보를 더한 문자열을 추가
for line_idx in range(1, line_number + 1):
    output.append(f'{line_idx}. ' + input().rstrip('\n'))

# 순서대로 출력
for result in output:
    print(result)
