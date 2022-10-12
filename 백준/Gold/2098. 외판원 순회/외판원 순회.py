# 외판원 순회

import sys

input = sys.stdin.readline

# INF 설정
INF = 2000000000

# 도시 갯수 입력
city_number = int(input())

# 간선 정보 입력
graph = []
for _ in range(city_number):
    graph.append(list(map(int, input().split())))

# 거리값을 담을 리스트 설정
dist = [[None for _ in range(1 << city_number)] for _ in range(city_number)]

def traveling_salesman(graph_info: list, distance_list: list, now_city: int, visited: int, max_visit: int = city_number):
    '''
    외판원의 최소 이동거리를 확인하는 함수
    '''

    # 모든 지점을 방문한 경우
    if visited == (1 << max_visit) - 1:

        # 경로가 존재한다면 결과값 반환
        if graph[now_city][0]:
            return graph_info[now_city][0]

        # 경로가 존재하지 않는 경우 INF 반환
        else:
            return INF

    # 이미 계산된 최소값이 존재한다면 그대로 반환
    if distance_list[now_city][visited] is not None:
        return distance_list[now_city][visited]

    # 그 이외의 경우
    else:

        # 임시 거리 변수 선언
        temp = INF

        # 출발점을 제외한 나머지 점들에 대해서 조사
        for check_city in range(1, max_visit):

            # 현재 노드에서 방문이 불가능한 경우
            if not graph[now_city][check_city]:
                continue

            # 이미 지난 도시의 경우 조사하지 않음
            if visited & (1 << check_city):
                continue

            # 다른 도시를 지나서 올 때 최소값이 작아지는 경우 갱신
            else:

                way_point_here = traveling_salesman(graph_info, distance_list, check_city, visited | (1 << check_city))

                if temp > way_point_here + graph_info[now_city][check_city]:
                    temp = way_point_here + graph_info[now_city][check_city]

        # 가장 작은 값 입력
        distance_list[now_city][visited] = temp

        # 최소 이동거리를 반환
        return temp

# 함수를 호출하여 결과 확인 후 출력
print(traveling_salesman(graph, dist, 0, 1))
