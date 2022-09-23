# 별자리 만들기

import sys
from math import sqrt

input = sys.stdin.readline


# 두 점 사이의 거리를 구하는 함수 선언
def distance(spot1: list, spot2: list):

    spot1_x, spot1_y = spot1
    spot2_x, spot2_y = spot2

    result = sqrt((spot1_x - spot2_x) ** 2 + (spot1_y - spot2_y) ** 2)

    return result

# 사이클을 확인하는 함수 선언
def cycle(graph, start_node, max_number):

    # 노드 방문 리스트 선언
    is_visit = [False for _ in range(max_number)]

    # DFS로 확인
    progress_stack = []
    progress_stack.append([start_node, None])
    is_visit[start_node] = True

    while progress_stack:
        now_node, last_node = progress_stack.pop()

        for next_node in graph[now_node]:

            # 양방향 그래프인 경우 직전 노드 예외 처리
            if next_node == last_node:
                continue

            # 이미 방문한 노드로 간선이 있다는 것은 사이클이 존재한다는 것
            elif is_visit[next_node]:
                return True

            else:
                is_visit[next_node] = True
                progress_stack.append([next_node, now_node])

    # 사이클이 존재하지 않았다면 False 반환
    return False


# 별의 갯수 input
star_number = int(input())

# 별의 좌표 input
star_list = []
for _ in range(star_number):
    star_list.append(list(map(float, input().split())))

# 성간 거리를 입력할 리스트 선언
line_info = []

# 성간 거리 정보 입력
for star_idx in range(star_number):
    for other_star_idx in range(star_number):
        if star_idx != other_star_idx:
            line_info.append([distance(star_list[star_idx], star_list[other_star_idx]), star_idx, other_star_idx])

# 최소 비용 변수 선언
min_constellation = 0

# 사이클 체크 딕셔너리 선언
constellation_graph = {idx: [] for idx in range(star_number)}

# 크루스칼 알고리즘을 사용
for next_distance, start_star, end_star in sorted(line_info, key= lambda x: x[0]):

    # 그래프에 해당 라인 추가
    constellation_graph[start_star].append(end_star)
    constellation_graph[end_star].append(start_star)

    # 사이클이 아닐 경우 거리 확인
    if not cycle(constellation_graph, start_star, star_number):
        
        # 비용 변수에 다음 거리 합산
        min_constellation += next_distance

    else:
        # 사이클이 아닐 경우 다시 제거
        constellation_graph[start_star].pop()
        constellation_graph[end_star].pop()

# 문제 조건에 맞게 출력
print(f'{min_constellation:.2f}')
