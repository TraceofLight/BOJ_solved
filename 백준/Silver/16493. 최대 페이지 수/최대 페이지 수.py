# 최대 페이지 수

import sys

input = sys.stdin.readline

# 남은 기간, 챕터의 수 입력
left_day, chapter_number = map(int, input().split())

# 챕터 정보 입력
chapter_info = []
for _ in range(chapter_number):
    chapter_info.append(list(map(int, input().split())))

# Knapsack Algorithm

# 해당 기간이 지났을 때 읽었을 최대의 페이지 수를 저장하는 리스트 선언
max_page_list = [0 for _ in range(left_day + 1)]

# 모든 챕터에 대해 조사
for cost_day, read_page in chapter_info:

    # 모든 기간에 대해 체크, 중복 체크 방지를 위해 역방향으로 추가
    for last_day in range(left_day + 1, -1, -1):

        # 기간을 넘지 않는 경우에만 확인
        if last_day + cost_day <= left_day:

            # 이전 임의의 날짜에서 현재 읽은 챕터의 페이지만큼을 더한 값이 해당 날짜의 최대값보다 크다면 갱신
            max_page_list[last_day + cost_day] = max(
                max_page_list[last_day + cost_day], max_page_list[last_day] + read_page
            )

# 마지막날까지의 최대값을 출력
print(max_page_list[left_day])
