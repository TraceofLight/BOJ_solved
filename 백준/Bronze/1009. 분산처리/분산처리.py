# 분산 처리

import sys

# 케이스 횟수 input 및 출력 리스트 선언
testcase = int(input())
output = []

for each_case in range(testcase):
    # 문제 조건에 제시된 a와 b input
    num1, num2 = map(int, sys.stdin.readline().split())
    # 10대의 컴퓨터로만 체크하므로 10으로 모듈러 연산
    num1 %= 10
    # 1의 자리 순환 사이클을 담을 리스트 선언
    multiple_cycle = []
    # 카운팅 변수 input
    counter = 0
    while counter <= num2:
        # 기존에 있던 값이 나온다면 break
        calc_result = (num1 ** (counter + 1)) % 10
        if calc_result in multiple_cycle:
            break
        # 아니라면 사이클 리스트에 새로 추가
        else:
            multiple_cycle.append(calc_result)
            counter += 1
    # 결과값을 출력 리스트에 추가
    output.append(multiple_cycle[num2 % counter - 1])

# 출력
for result in output:
    # 0은 마지막 10번 컴퓨터에서 처리
    if result == 0:
        print(10)
    else:
        print(result)
