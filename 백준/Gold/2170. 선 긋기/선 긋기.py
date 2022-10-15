# 선 긋기

import sys

input = sys.stdin.readline

# 그은 선의 갯수 입력
line_number = int(input())

# 그은 선 정보 입력
line_list = []
for _ in range(line_number):
    line_list.append(tuple(map(int, input().split())))

# 선 정렬
line_list.sort()

# 총 길이 변수 선언
complete_line = 0

# 현재 선의 좌우 지점 변수 선언
line_start = None
line_end = None

for left, right in line_list:

    # 기존에 선이 없는 경우
    if line_start is None:

        # 좌우 지점 설정 후 선분 전체 길이 합산
        line_start = left
        line_end = right
        complete_line += line_end - line_start
        continue

    # 현재 선분과 만나지 않는 경우의 선분이 입력된 경우
    if right < line_start or left > line_end:

        # 총 길이에 합산 후 입력된 선분을 기준으로 다음 선분들 조사
        complete_line += right - left
        line_start = left
        line_end = right

    # 현재 선분과 만나는 경우
    else:

        # 좌측 기준 정렬이므로 우측 지점에 대해서만 조사
        if right > line_end:

            # 만나면서 우측 지점이 더 멀어진 경우 길이 추가 및 지점 갱신
            complete_line += right - line_end
            line_end = right

# 총 길이 출력
print(complete_line)
