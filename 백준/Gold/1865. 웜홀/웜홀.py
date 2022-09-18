# 웜홀

import sys

input = sys.stdin.readline

# 케이스 횟수 input
testcase = int(input())
# 출력 리스트 선언
output = []

for each_case in range(testcase):

    # 노드 갯수, 라인 갯수, 웜홀 갯수 input
    node_number, line_number, hole_number = map(int, input().split())
    # 경로 간 소요 시간을 기록하는 딕셔너리 선언 (default INF)
    cost_dict = {idx: [] for idx in range(1, node_number + 2)}

    # 라인 정보 입력
    for _ in range(line_number):
        start_node, end_node, time_cost = map(int, input().split())
        cost_dict[start_node].append((time_cost, end_node))
        cost_dict[end_node].append((time_cost, start_node))
    # 웜홀 정보 입력
    for _ in range(hole_number):
        start_node, end_node, time_back = map(int, input().split())
        cost_dict[start_node].append((-time_back, end_node))

    # 결과 체크용 Flag 선언
    is_go_past = False

    # 거리 갱신을 위한 리스트 선언
    distance = [2000000000 for _ in range(node_number + 2)]

    # 벨만 - 포드 알고리즘을 활용한 음수 사이클 체크

    # 인접 노드에 대해서 전체 순회하면서 갱신
    for counter in range(1, node_number + 1):
        for waypoint in range(1, node_number + 1):
            for now_cost, arrive in cost_dict[waypoint]:
                    if distance[arrive] > distance[waypoint] + now_cost:
                        distance[arrive] = distance[waypoint] + now_cost

                        # 마지막 순회 시 기록이 변경되었다면 음수 사이클 존재
                        if counter == node_number:
                            is_go_past = True
                            break

        # Flag를 통해 반복문 탈출
        if is_go_past:
            break

    # 음수 사이클이 존재하면 YES, 아닐 경우 NO를 출력 리스트에 추가
    if is_go_past:
        output.append('YES')
    else:
        output.append('NO')

# 출력
for result in output:
    print(result)
