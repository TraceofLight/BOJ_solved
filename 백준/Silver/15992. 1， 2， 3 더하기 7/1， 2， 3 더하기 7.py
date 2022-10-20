# 1, 2, 3 더하기 7

import sys

input = sys.stdin.readline

# 케이스 횟수 입력 및 출력 리스트 선언
testcase = int(input())
output = []

# 결과값 리스트 범위 변수 선언
max_number = 4
max_amount = 4

target_list = []
for _ in range(testcase):

    # 목표 숫자, 합산 숫자 갯수 입력
    target_number, target_amount = map(int, input().split())
    target_list.append([target_number, target_amount])

    # 최대값보다 크다면 갱신
    if max_number < target_number:
        max_number = target_number
    if max_amount < target_amount:
        max_amount = target_amount

# Dynamic Programming

# 결과값 리스트 선언
result_list = [[0 for _ in range(max_amount + 1)] for _ in range(max_number + 1)]

# 초기값 입력
result_list[1][1] = 1
result_list[2][1] = 1
result_list[2][2] = 1
result_list[3][1] = 1
result_list[3][2] = 2
result_list[3][3] = 1

# 초기값 이후의 모든 합에 대해 확인
for each_max_number in range(4, max_number + 1):

    # 사용한 숫자 가능성에 대해서 전체 확인
    for used_number in range(1, max_amount + 1):

        # 현재 대상 숫자 및 합산 갯수 정보에 대해서 더하기 전 숫자의 경우의 수를 합산
        for last_number in range(1, 4):
            result_list[each_max_number][used_number] += (
                result_list[each_max_number - last_number][used_number - 1]
            )
            result_list[each_max_number][used_number] %= 1000000009

# 결과값 출력 리스트에 추가
for number, amount in target_list:
    output.append(result_list[number][amount])

# 출력
for result in output:
    print(result)
