# 최단경로

from heapq import *
import sys
from collections import defaultdict

# 노드, 라인의 갯수와 초기 노드 정보 input()
node_number, line_number = map(int, sys.stdin.readline().split())
start_node = int(sys.stdin.readline()) - 1

# 그래프 형태의 딕셔너리 생성
graph_dict = {idx: dict() for idx in range(node_number)}

# 라인 정보 및 가중치 추가, 딕셔너리에 관련 정보 입력
for _ in range(line_number):
    depart, arrive, cost = map(int, sys.stdin.readline().split())
    depart -= 1
    arrive -= 1
    if graph_dict[depart].get(arrive) is None:
        graph_dict[depart][arrive] = cost
    else:
        if graph_dict[depart].get(arrive) > cost:
            graph_dict[depart][arrive] = cost

# 최단거리를 저장하는 딕셔너리 생성
distance = {node: float('inf') for node in graph_dict}
# 시작점 0 처리
distance[start_node] = 0

# 우선순위 큐 생성 후 초기값 추가
priority_que = []
heappush(priority_que, [distance[start_node], start_node])
while priority_que:
    now_distance, now_point = heappop(priority_que)
    # 현재 길이만으로도 기록 최단거리보다 길면 더 이상 체크 안함
    if distance[now_point] > now_distance:
        continue
    for next_point, next_distance in graph_dict[now_point].items():
        # 다음 포인트까지의 길이가 현재 지점을 경유해서 갈 경우가 더 짧다면 최단거리 갱신
        if distance[next_point] > now_distance + next_distance:
            distance[next_point] = now_distance + next_distance
            heappush(priority_que, [now_distance + next_distance, next_point])

# 결과 출력
for idx in range(node_number):
    if start_node == idx:
        print(0)
    else:
        if distance.get(idx) == float('inf'):
            print('INF')
        else:
            print(distance[idx])
