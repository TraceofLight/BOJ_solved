# 스티커

import sys

input = sys.stdin.readline

# 테스트 횟수 input 및 출력 리스트 선언
testcase = int(input())
output = []

for each_case in range(testcase):
    # 스티커 길이 및 정보 input
    length = int(input())
    upper_line = list(map(int, input().split()))
    lower_line = list(map(int, input().split()))

    # Tabulation을 위한 리스트 선언 및 기본값 입력
    result_val = [[0, 0], [upper_line[0], lower_line[0]]]

    # 1줄을 넘는 경우 DP 알고리즘을 통해 원하는 길이까지 연산
    if length > 1:
        for idx in range(2, length + 1):
            result_val.append([
                max(result_val[idx - 1][1], max(result_val[idx - 2])) + upper_line[idx - 1]
                , max(result_val[idx - 1][0], max(result_val[idx - 2])) + lower_line[idx - 1]
            ])

    # 연산 결과를 출력 리스트에 추가
    output.append(max(result_val[length]))

# 출력
for result in output:
    print(result)
