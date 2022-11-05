# 최댓값

import sys

input = sys.stdin.readline

# 최댓값 및 좌표 변수 입력
max_number = -1
target_idx = (0, 0)

# 9개의 줄 입력
for y_idx in range(1, 10):

    # 1개 행에 대해 확인
    temp = list(map(int, input().split()))

    # 모든 원소 확인
    for x_idx in range(1, 10):

        # 기존 최대값보다 크다면 갱신하고 좌표 기록
        if max_number < temp[x_idx - 1]:
            max_number = temp[x_idx - 1]
            target_idx = (y_idx, x_idx)

# 출력
print(max_number)
print(*target_idx)
