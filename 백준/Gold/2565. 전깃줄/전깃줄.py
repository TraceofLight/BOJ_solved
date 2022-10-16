# 전깃줄 

import sys

input = sys.stdin.readline

# 전깃줄 갯수 입력
cord_number = int(input())

# 전깃줄 정보 입력
cord_list = list()
for _ in range(cord_number):
    cord_list.append(tuple(map(int, input().split())))

cord_list.sort()

# Dynamic Programming

# LCS 확인을 위한 리스트 선언
power_cord = [[0 for _ in range(501)] for _ in range(501)]

# 모든 위치 조사
for start in range(501):
    for end in range(501):

        # 연결이 이루어진 경우
        if (start, end) in cord_list:

            # 기존 연결하기 직전 최댓값보다 1개 더 많은 연결
            power_cord[start][end] = power_cord[start - 1][end - 1] + 1

        # 연결이 이루어지지 않은 경우
        else:

            # 기존 최댓값 중에서 가장 큰 최댓값을 해당 값으로 입력
            power_cord[start][end] = max(
                power_cord[start - 1][end], power_cord[start][end - 1]
            )

# 최대 연결 갯수를 제외한 나머지가 잉여 연결, 따라서 전체 연결 중 최대 연결값을 뺀 나머지를 출력
print(cord_number - power_cord[500][500])
