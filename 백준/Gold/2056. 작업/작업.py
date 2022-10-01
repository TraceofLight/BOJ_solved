# 작업

import sys
from collections import deque

input = sys.stdin.readline

# 작업의 갯수 입력
work_number = int(input())

# 그래프 딕셔너리 선언
line_dict = {idx: [] for idx in range(1, work_number + 1)}

# 위상정렬을 위한 딕셔너리 선언
topology_sort = {idx: 0 for idx in range(1, work_number + 1)}

# 해당 작업이 완료 가능한 최소 시간을 기록하는 딕셔너리 선언
min_time = {idx: 0 for idx in range(1, work_number + 1)}

# 작업 정보 입력
for now_work in range(1, work_number + 1):

    # 작업 소요 시간, 선행되는 작업 수 및 선행되는 작업 정보 입력
    take_time, precede_work_number, *works = map(int, input().split())

    # 위상 정렬 딕셔너리에 선행되는 작업 정보 입력
    topology_sort[now_work] = precede_work_number

    # 선행되는 작업이 없다면 처음에 바로 시작이 가능
    if not topology_sort[now_work]:
        min_time[now_work] = take_time

    # 간선 정보를 그래프에 입력
    for each_work in works:
        line_dict[each_work].append([take_time, now_work])

# 위상 정렬을 위한 큐 선언
progress_que = deque()

# 바로 진행할 수 있는 작업들을 큐에 추가
for work in range(1, work_number + 1):
    if not topology_sort[work]:
        progress_que.append(work)

# 위상 정렬 진행
while progress_que:

    # 현재 작업 pop
    now_work = progress_que.popleft()

    # 현재 작업이 선행되는 다음 작업들에 대하여 간선 제거
    for time_cost, next_work in line_dict[now_work]:
        topology_sort[next_work] -= 1

        # 만약 다음 작업의 최소 시간이 현 작업을 진행한 경우가 더 길다면 갱신
        # 선행 작업이 완료된 경우에만 진행할 수 있기 때문
        if min_time[next_work] < min_time[now_work] + time_cost:
            min_time[next_work] = min_time[now_work] + time_cost

        # 간선이 전부 제거된 작업은 큐에 추가
        if not topology_sort[next_work]:
            progress_que.append(next_work)

# 작업들의 최단 소요 시간 중에서 최대값을 출력
print(max(list(min_time.values())))
