# 회사 문화 1

import sys

input = sys.stdin.readline

sys.setrecursionlimit(100001)

# 직원 수, 칭찬 횟수 입력
employee_number, compliment_number = map(int, input().split())

# 직속 상사 정보 입력
parent = list(map(int, input().split()))

# 관계 그래프 리스트 선언
graph = [[] for _ in range(employee_number + 1)]

# 유향 그래프의 형태로 그래프에 정보 입력
for now_employee in range(employee_number):
    if parent[now_employee] != -1:
        graph[parent[now_employee]].append(now_employee + 1)

# 칭찬 정도를 기록하는 리스트 선언
compliment_list = [0 for _ in range(employee_number + 1)]

# 칭찬 정보 입력
for _ in range(compliment_number):
    compliment_target, compliment_amount = map(int, input().split())
    compliment_list[compliment_target] += compliment_amount


def dfs(graph: list, compliment_info: int, now_vertex: int = 1):
    '''
    깊이 탐색을 진행하면서 내리칭찬하는 함수
    '''
    for next_vertex in graph[now_vertex]:
        compliment_info[next_vertex] += compliment_info[now_vertex]
        dfs(graph, compliment_info, next_vertex)


# 함수를 호출하여 내리칭찬 진행
dfs(graph, compliment_list)

# 결과 출력
print(*compliment_list[1:])
