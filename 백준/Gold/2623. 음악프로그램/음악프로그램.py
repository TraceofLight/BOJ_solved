# 음악프로그램

import sys
from collections import deque

input = sys.stdin.readline

# 가수 숫자 및 보조 PD 숫자 입력
singer_number, pd_number = map(int, input().split())

# 관계 그래프 딕셔너리 선언
graph = {idx: [] for idx in range(1, singer_number + 1)}

# 위상 정렬을 위한 딕셔너리 선언
topology_sort = {idx: 0 for idx in range(1, singer_number + 1)}

# PD 정보 입력
for _ in range(pd_number):

    # 순서 갯수 및 순서 리스트 입력
    order_number, *order_list = map(int, input().split())

    # 그래프 및 위상 정렬 데이터로 가공
    for idx in range(order_number - 1):
        graph[order_list[idx]].append(order_list[idx + 1])
        topology_sort[order_list[idx + 1]] += 1

# 우선순위 큐 선언
progress_que = deque()

# 후순위가 아닌 가수들 전부 큐에 추가
for each_singer in range(1, singer_number + 1):
    if not topology_sort[each_singer]:
        progress_que.append(each_singer)

# 순서 배정 결과 리스트 선언 및 배정 인원 카운팅 변수 선언
order_list = []
sing_count = 0

# 위상 정렬 알고리즘을 통한 순서 배정
while progress_que:

    # 현재 가수 확인
    now_singer = progress_que.popleft()

    # 가수 카운팅 및 순서 배정 리스트에 추가
    sing_count += 1
    order_list.append(now_singer)

    # 현재 가수로부터 연결된 순서 간선 제거
    for next_singer in graph[now_singer]:
        topology_sort[next_singer] -= 1

        # 간선이 0개가 되었다면 큐에 추가
        if not topology_sort[next_singer]:
            progress_que.append(next_singer)

# 모든 가수의 순서를 배정한 경우 문제 조건에 맞게 출력
if sing_count == singer_number:
    for singer in order_list:
        print(singer)

# 그렇지 못한 경우 0을 출력
else:
    print(0)
