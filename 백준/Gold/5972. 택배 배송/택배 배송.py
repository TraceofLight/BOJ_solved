# 택배 배송

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

# 상한값 설정
INF = 2000000000

# 정점 및 간선 갯수 입력
vertex_number, edge_number = map(int, input().split())

# 그래프 생성
graph = [[] for _ in range(vertex_number + 1)]

# 그래프 정보 입력
for _ in range(edge_number):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))

# 최단 거리를 담을 리스트 선언
dist = [INF for _ in range(vertex_number + 1)]

# 우선순위 큐에 초기값 입력
priority_que = []
heappush(priority_que, (1, 0))

# 최초 지점 최소거리 0으로 초기화
dist[1] = 0

# Dijkstra Algorithm

while priority_que:
    
    # 현재 지점과 누적 최소거리 확인
    now_idx, now_cost = heappop(priority_que)

    # 현재 지점에서 갈 수 있는 다음 정점들에 대해 조사
    for next_idx, next_cost in graph[now_idx]:

        # 현재 지점을 거쳐서 가는 경우가 더 비용이 적게 든다면 갱신
        if dist[next_idx] > dist[now_idx] + next_cost:
            dist[next_idx] = dist[now_idx] + next_cost

            # 큐에 해당 지점을 추가
            heappush(priority_que, (next_idx, dist[next_idx]))

# 목적지까지의 최소 비용 출력
print(dist[vertex_number])
