# 운동

import sys

input = sys.stdin.readline

# INF 값 지정
INF = 2000000000

# 마을 갯수, 간선 갯수 input
town_number, line_number = map(int, input().split())

# INF 값 설정
INF = 100000000

# 지점 사이 최단 거리를 담을 딕셔너리 선언
distance = {idx: {other_idx: INF for other_idx in range(1, town_number + 1)} 
                                        for idx in range(1, town_number + 1)}

# 간선 정보 입력
for _ in range(line_number):
    depart, arrive, dist = map(int, input().split())
    distance[depart][arrive] = dist

# 모든 출발지, 도착지, 경유지에 대해서 경유지를 거쳐간 값이 더 작다면 갱신
for start_point in range(1, town_number + 1):
    for way_point in range(1, town_number + 1):
        for end_point in range(1, town_number + 1):
            if distance[start_point][end_point] > distance[start_point][way_point] + distance[way_point][end_point]:
                distance[start_point][end_point] = distance[start_point][way_point] + distance[way_point][end_point]

# 결과값 변수 선언
result = INF

# 모든 사이클 중 최소값을 체크
for each_town in range(1, town_number + 1):
    now_cycle = distance[each_town][each_town]
    if result > now_cycle:
        result = now_cycle

# 사이클이 없다면 -1 출력
if result == INF:
    print(-1)

# 사이클이 있다면 그 값을 반환
else:
    print(result)
