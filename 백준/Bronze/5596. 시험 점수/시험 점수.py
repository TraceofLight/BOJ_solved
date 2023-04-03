# 시험 점수

import sys

input = sys.stdin.readline

score_a = sum(list(map(int, input().split())))
score_b = sum(list(map(int, input().split())))

print(max(score_a, score_b))
