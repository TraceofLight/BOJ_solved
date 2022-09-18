# Triathlon

import sys

input = sys.stdin.readline

# 참가자 수 input
participant_number = int(input())

# 최고 점수 변수 선언
max_score = -2000000000

for _ in range(participant_number):

    # 문제 유형별 점수 input
    ad_hoc, dp, greedy = map(int, input().split())

    # 점수 계산
    score = ad_hoc * (dp + greedy)

    # 특정 조건 만족 시 점수 2배
    if ad_hoc == dp + greedy:
        score *= 2

    # 기존 최고 점수를 넘었다면 갱신
    if score > max_score:
        max_score = score

# 결과 출력
print(max_score)
