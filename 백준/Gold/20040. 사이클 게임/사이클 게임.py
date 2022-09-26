# 사이클 게임

import sys
from collections import deque

input = sys.stdin.readline

# 재귀 한도 상향 조정
sys.setrecursionlimit(1000000)

# 점의 갯수, 간선의 갯수 input
node_number, line_number = map(int, input().split())

# 라인 정보를 담을 큐 선언
line_que = deque()

# 라인 정보 input
for _ in range(line_number):
    line_que.append(list(map(int, input().split())))

# 집합 정보를 담을 리스트 선언
union_group = [idx for idx in range(node_number)]


# 집합의 대표 노드를 찾는 함수 선언
def find_node(node_info: list, init_node: int) -> int:
    if node_info[init_node] == init_node:
        return init_node
    else:
        node_info[init_node] = find_node(node_info, node_info[init_node])
        return node_info[init_node]

# 이어져서 같은 집합에 존재하는지 체크하는 함수 선언
def union_node(node_info: list, node_1: int, node_2: int) -> bool:
    result_1, result_2 = find_node(node_info, node_1), find_node(node_info, node_2)
    if result_1 == result_2:
        return False
    node_info[result_2] = node_info[result_1]
    return True


# 결과값 변수 선언
result = 0

# 최대 라인 갯수만큼 반복
for count in range(1, line_number + 1):
    now_start, now_end = line_que.popleft()

    # 함수를 호출하여 같은 집합에 있는지 체크
    if not union_node(union_group, now_start, now_end):

        # 같은 집합에 있다면 사이클이 발생하므로 break
        result = count
        break

# 결과 출력
print(result)
