# 게리맨더링

import sys
from itertools import combinations

input = sys.stdin.readline

# 상한값 선언
INF = 2000000000

# 구역 갯수 입력
area_number = int(input())

# 구역별 인구 정보 입력
people_number = [0] + list(map(int, input().split()))

# 인접 구역 관계 그래프 입력
graph = [[] for _ in range(area_number + 1)]
for area_idx in range(1, area_number + 1):
    near_area, *graph[area_idx] = map(int, input().split())

# 총 인구수 확인
max_people = sum(people_number)

# 최소 차이값 변수 선언
min_difference = INF

# 한 선거구의 포함될 모든 구역 수에 대해 체크 
for areas in range(1, area_number // 2 + 1):

    # 모든 구역 중에서 한 선거구에 포함될 구역 확정
    for target_areas in combinations(range(1, area_number + 1), areas):

        # 해당 선거구에 포함되는 구역 집합 선언 및 해당 선거구 인원수 변수 선언
        target_set = set(target_areas)
        sum_areas = 0

        # Depth First Search

        # 집합에 포함된 한 구역에서 시작하는 깊이 탐색
        for first_area in target_set:

            # 선거구 내 구역 수 체크 카운터 선언
            counter = 1

            # 방문 리스트 선언
            is_visited = [False for _ in range(area_number + 1)]

            # 깊이 탐색을 진행할 스택 선언 및 초기 조건 입력
            progress_stack = [first_area]
            sum_areas += people_number[first_area]
            is_visited[first_area] = True

            # 탐색 진행
            while progress_stack:

                # 현재 구역 확인
                now_area = progress_stack.pop()

                # 모든 인접 구역에 대해 확인
                for next_area in graph[now_area]:

                    # 같은 선거구에 속해있고 방문하지 않았을 경우만 조사
                    if next_area in target_set:
                        if not is_visited[next_area]:

                            # 방문 처리, 인구수 합산, 선거구 카운팅
                            is_visited[next_area] = True
                            sum_areas += people_number[next_area]
                            counter += 1

                            # 다음 구역 스택에 추가
                            progress_stack.append(next_area)

            # 1회의 조사로 선거구의 모든 정보를 획득하므로 반복하지 않음
            break

        # 남은 구역들에 대해서 다른 하나의 선거구라 가정하고 깊이 탐색 진행

        other_set = set(range(1, area_number + 1)) - set(target_set)
        sum_other_areas = 0

        for first_other_area in other_set:

            other_counter = 1
            sum_other_areas += people_number[first_other_area]

            progress_stack = [first_other_area]
            is_visited[first_other_area] = True

            while progress_stack:
                
                now_area = progress_stack.pop()

                for next_area in graph[now_area]:
                    if next_area in other_set:
                        if not is_visited[next_area]:
                            is_visited[next_area] = True
                            sum_other_areas += people_number[next_area]
                            progress_stack.append(next_area)
                            other_counter += 1

            break

        # 양쪽 선거구를 조사했을 때 남는 구역이 없을 경우만 성립
        if counter + other_counter == area_number:

            # 두 선거구의 인구 차이를 확인하여 기존값보다 작다면 갱신
            now_min = abs(sum_areas - sum_other_areas)
            if min_difference > now_min:
                min_difference = now_min

# 한 번도 갱신하지 못했다면 선거구 분할 실패이므로 -1 출력
if min_difference == INF:
    print(-1)

# 갱신한 경우 결과를 출력
else:
    print(min_difference)
