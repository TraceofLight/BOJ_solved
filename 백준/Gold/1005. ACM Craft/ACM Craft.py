# ACM Craft

import sys
from collections import deque

input = sys.stdin.readline

# 케이스 횟수 input 및 출력 리스트 선언
testcase = int(input())
output = []

for each_case in range(testcase):

    # 건물 갯수 및 건설 규칙 input
    building_number, rule_amount = map(int, input().split())

    # 건설 시간 해시 테이블 생성
    build_time_list = list(map(int, input().split()))
    build_time_hash = {idx: build_time_list[idx - 1] for idx in range(1, building_number + 1)}

    # 관계 그래프 딕셔너리 선언
    graph = {idx: [] for idx in range(1, building_number + 1)}

    # 도착 노드 기준으로 간선 카운트 딕셔너리 생성
    count_line = {idx: 0 for idx in range(1, building_number + 1)}

    # 관계 정보 input
    for _ in range(rule_amount):
        precede, follow = map(int, input().rstrip('\n').split())
        graph[precede].append(follow)
        count_line[follow] += 1

    # 목적 건물 input
    goal_building = int(input())

    # 위상 정렬을 위한 큐 선언
    progress_que = deque()

    # 도착지가 아닌 노드들을 큐에 추가
    for idx in range(1, building_number + 1):
        if not count_line[idx]:
            progress_que.append([idx, build_time_hash[idx]])

    # 각 건물을 짓기까지 최대 시간을 기록할 딕셔너리 선언
    time_cost = {idx: 0 for idx in range(1, building_number + 1)}

    # 위상 정렬
    while progress_que:
        now_idx, now_cost = progress_que.popleft()

        # 목적 건물을 완성했다면 출력 리스트에 추가하고 반복문 break
        if now_idx == goal_building:
            output.append(now_cost)
            break

        # 간선 제거
        for next_idx in graph[now_idx]:
            count_line[next_idx] -= 1
            # 간선을 제거하면서 기존 조건 빌딩보다 더 시간 소모가 많은 케이스가 존재한다면 갱신
            time_cost[next_idx] = max(now_cost + build_time_hash[next_idx], time_cost[next_idx])

            # 간선 갯수가 0이 되었다면 큐에 추가
            if not count_line[next_idx]:
                progress_que.append([next_idx, time_cost[next_idx]])

# 출력
for result in output:
    print(result)
