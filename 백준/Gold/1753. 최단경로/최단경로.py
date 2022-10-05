# 최단경로

import sys
from heapq import *

input = sys.stdin.readline

# INF 설정
INF = 2000000000

# 노드, 간선의 갯수와 초기 노드 정보 입력
node_number, line_number = map(int, input().split())
start_node = int(input())

# 그래프 형태의 딕셔너리 생성
graph_dict = {idx: dict() for idx in range(1 ,node_number + 1)}

# 간선 정보 및 가중치 추가, 딕셔너리에 관련 정보 입력
for _ in range(line_number):

    # 출발지, 도착지, 가중치 정보 입력
    depart, arrive, cost = map(int, input().split())

    # 가중치 정보가 없다면 가중치 입력
    if graph_dict[depart].get(arrive) is None:
        graph_dict[depart][arrive] = cost
    
    # 이미 존재한다면 작을 때만 갱신
    else:
        if graph_dict[depart].get(arrive) > cost:
            graph_dict[depart][arrive] = cost

# 최단거리를 저장하는 딕셔너리 생성
distance = {idx: INF for idx in range(1, node_number + 1)}

# 시작점 0 처리
distance[start_node] = 0

# 우선순위 큐 생성 후 초기값 추가
priority_que = []
heappush(priority_que, [distance[start_node], start_node])

# 다익스트라 알고리즘을 통한 목적지까지의 최단거리 확인
while priority_que:

    # 현재 가중치 및 현재 지점 pop
    now_distance, now_point = heappop(priority_que)

    # 이미 다른 경로를 통해 최단 거리가 도출된 경우 조사하지 않음
    if distance[now_point] < now_distance:
        continue

    # 다음 지점 및 다음 간선에 대해 조사
    for next_point, next_distance in graph_dict[now_point].items():

        # 다음 포인트까지의 길이가 현재 지점을 경유해서 갈 경우가 더 짧다면 최단거리 갱신
        if distance[next_point] > now_distance + next_distance:
            distance[next_point] = now_distance + next_distance

            # 갱신된 길이에 따른 변동 사항을 확인하기 위해 다음 간선을 큐에 추가
            heappush(priority_que, [distance[next_point], next_point])

# 결과 출력
for idx in range(1, node_number + 1):

    # 자기 자신은 0으로 출력
    if start_node == idx:
        print(0)

    # 자기 자신이 아닌 경우
    else:

        # 해당 값이 INF에서 변동이 없었을 경우 INF 출력
        if distance.get(idx) == INF:
            print('INF')

        # 아니라면 결과값을 출력
        else:
            print(distance[idx])
