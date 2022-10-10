# 큰 수

import sys
from math import log10

input = sys.stdin.readline

# 결과 리스트 선언 및 초기값 설정
result_val = [0, 0, log10(2), log10(6), log10(24)]

# 0을 제외한 리스트 길이 설정
list_length = 4

# 테스트 횟수 입력 및 출력 리스트 선언
testcase = int(input())
output = []

for each_case in range(testcase):

    # 목표 팩토리얼 정보 입력
    target = int(input())

    # 이미 조사가 된 케이스일 경우
    if target <= list_length:

        # 해당 결과를 출력 리스트에 추가
        output.append(int(result_val[target] + 1))

    # 아직 조사가 진행되지 않은 경우
    else:

        # 다이나믹 프로그래밍 : 타뷸레이션 방식을 통한 결과 도출
        for idx in range(list_length + 1, target + 1):

            # 직전값에 해당 수의 로그값을 합산
            result_val.append(result_val[idx - 1] + log10(idx))

            # 길이 1 추가
            list_length += 1

        # 결과를 출력 리스트에 추가
        output.append(int(result_val[target] + 1))

# 출력
for result in output:
    print(result)
