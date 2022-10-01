# 문자열

import sys

input = sys.stdin.readline

# 문자열 갯수 입력 및 출력 리스트 선언
string_number = int(input())
output = []

for _ in range(string_number):

    # 문자열 입력
    input_string = input().rstrip('\n')

    # 첫 글자와 마지막 글자를 출력 리스트에 추가
    output.append([input_string[0], input_string[-1]])

# 문제 조건에 맞춰서 출력
for result in output:
    print(''.join(result))
