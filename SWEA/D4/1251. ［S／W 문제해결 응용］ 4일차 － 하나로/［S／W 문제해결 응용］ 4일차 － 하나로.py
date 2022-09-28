# SWEA_1251 하나로

from heapq import *

# 테스트 횟수 및 출력 리스트 선언
testcase = int(input())
output = []


# 해당 노드의 집합을 확인하는 함수 선언
def find_node(node_dict: dict, node_num: int) -> int:
    if node_dict[node_num] == node_num:
        return node_num
    else:
        node_dict[node_num] = find_node(node_dict, node_dict[node_num])
        return node_dict[node_num]

# 노드 집합을 합쳐주는 함수 선언
def union_node(node_dict: dict, node_1: int, node_2: int) -> None:
    root_node_1, root_node_2 = find_node(node_dict, node_1), find_node(node_dict, node_2)
    if root_node_1 == root_node_2:
        return False
    else:
        if root_node_1 < root_node_2:
            node_dict[root_node_2] = root_node_1
        else:
            node_dict[root_node_1] = root_node_2
        return True

# 두 섬을 연결할 때의 환경 부담금을 계산하는 함수 선언
def environmental_cost(island_1: list, island_2: list, constant_val: int) -> int:
    distance_square = (island_1[0] - island_2[0]) ** 2 + (island_1[1] - island_2[1]) ** 2
    result = constant_val * distance_square
    return result


for each_case in range(testcase):

    # 섬의 갯수 input
    island_number = int(input())

    # 각 섬들의 좌표 input
    coord_x = list(map(int, input().split()))
    coord_y = list(map(int, input().split()))

    # 섬들의 좌표를 담은 리스트 선언
    coord_list = [[coord_y[idx], coord_x[idx]] for idx in range(island_number)]

    # 환경 부담 세율 실수 E
    constant = float(input())

    # 우선 순위 큐 선언
    priority_que = []

    # 각 섬들과 환경 부담금에 대한 데이터를 가공하여 큐에 추가
    for idx in range(island_number):
        for other_idx in range(idx + 1, island_number):
            heappush(priority_que, [
                environmental_cost(coord_list[idx], coord_list[other_idx], constant),
                idx, 
                other_idx,
            ])

    # 각 섬의 소속 집합 정보를 담을 딕셔너리 선언
    set_dict = {idx: idx for idx in range(island_number)}

    # 최소 환경 부담금 변수 및 간선 갯수 카운팅 변수 선언
    total_min_cost = 0
    connection_count = 0

    # 크루스칼 알고리즘을 활용하여 최소 스패닝 트리를 구축
    while priority_que and connection_count <= island_number - 1:

        # 비용이 적게 드는 터널부터 pop
        now_cost, island_1, island_2 = heappop(priority_que)

        # 유니온 파인드 함수를 호출하여 아직 이어지지 않은 섬이라면 연결
        # 환경 부담금 합산 및 간선 카운팅
        if union_node(set_dict, island_1, island_2):
            total_min_cost += now_cost
            connection_count += 1

    # 최종 환경 부담금을 조건에 맞춰 출력 리스트에 추가
    output.append(round(total_min_cost))

# 문제 조건에 따라서 출력
for output_idx in range(testcase):
    print(f'#{output_idx + 1} {output[output_idx]}')
