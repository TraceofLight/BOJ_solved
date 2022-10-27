# 앱

import sys

input = sys.stdin.readline

# 앱 갯수, 필요 메모리 입력
app_number, need_memory = map(int, input().split())

# 각 앱의 메모리와 비활성화 시의 비용 입력
app_memories = list(map(int, input().split()))
disable_costs = list(map(int, input().split()))

# 앱의 메모리와 비용 합쳐서 짝지음
memories_and_costs = list(zip(app_memories, disable_costs))

# 최대 필요 비용 연산
sum_cost = sum(disable_costs)

# 각 비용별 최대 절약 가능한 메모리 리스트 선언
cost_list = [0 for _ in range(sum_cost + 1)]

# Knapsack Algorithm

# 모든 앱에 대해 확인
for now_memory, now_cost in memories_and_costs:

    # 최대 필요 비용까지 조사
    for last_cost in range(sum_cost, -1, -1):

        # 최대 비용을 넘지 않는 선에서 확인
        if last_cost + now_cost <= sum_cost:

            # 기존 최대값보다 컸다면 갱신
            cost_list[last_cost + now_cost] = max(
                cost_list[last_cost + now_cost], cost_list[last_cost] + now_memory
            )

# 비용을 0에서부터 조사해서 기준 메모리 이상을 절약한 경우의 비용을 출력
for idx in range(sum_cost + 1):
    if cost_list[idx] >= need_memory:
        print(idx)
        break
