# 시험 감독

import sys
from math import ceil

input = sys.stdin.readline

# 시험장 갯수, 응시자 수, 감독관 감시 가능 숫자 입력
test_site = int(input())
candidate_list = list(map(int, input().split()))
main_viewer, sub_viewer = map(int, input().split())

# 필요 감독관 수 총감독관 인원수로 초기화
total_viewer = test_site

# 모든 시험장에 대해 체크
for idx in range(test_site):

    # 총감독관이 감독할 수 있는 숫자만큼 인원수 제거
    candidate_list[idx] = max(0, candidate_list[idx] - main_viewer)

    # 남은 응시자를 모두 감독할 수 있는만큼 부감독관을 추가하고 필요 감독관을 카운팅
    total_viewer += ceil(candidate_list[idx] / sub_viewer)

# 결과 출력
print(total_viewer)
