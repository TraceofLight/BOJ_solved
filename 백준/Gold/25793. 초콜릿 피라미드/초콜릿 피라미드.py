# 초콜릿 피라미드

import sys

input = sys.stdin.readline

# 케이스 횟수 및 출력 리스트 선언
testcase = int(input())
output = []

for _ in range(testcase):

    # 가로, 세로 길이 입력
    height, width = map(int, input().split())

    # 둘의 길이 차 확인
    short_edge = min(height, width)
    long_edge = max(height, width)
    sub = long_edge - short_edge

    # 규칙에 따른 갯수 합연산
    dark_chocolate = (
        (short_edge * (short_edge + 1) * (2 * short_edge + 1)) // 3
        + short_edge * (short_edge + 1) * (sub - 1) - sub * short_edge
    )

    # 길이 차 반영 후 식에 의한 연산
    white_chocolate = dark_chocolate + short_edge

    # 결과값 출력 리스트에 추가
    output.append([white_chocolate, dark_chocolate])

# 출력
for result in output:
    print(*result)
