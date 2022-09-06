# 평범한 배낭

import sys

# 물건의 갯수, 최대 무게 input
stuff_number, max_weight = map(int, sys.stdin.readline().split())
# 물건 목록 리스트 선언
stuff_list = []

# 각 물건의 무게와 가치 input
for _ in range(stuff_number):
    weight, value = map(int, sys.stdin.readline().split())
    unit_value = value / weight
    stuff_list.append([weight, value, unit_value])

# 단위 가치에 대해 우선순위 부여
stuff_list.sort(key=lambda x:(x[0]))

# 최대 value 변수 선언
max_value = 0

# 해당 무게에서의 최대 value를 값으로 가지는 딕셔너리 선언
weight_dict = {idx: 0 for idx in range(max_weight + 1)}

for idx in range(stuff_number):
    # 넣을 물건의 정보 변수 선언
    current_weight, current_value, *args = stuff_list[idx]
    # 딕셔너리의 모든 값에 대해 조사
    # 갱신된 값이 다음 조건에 반영되지 않도록 역순 리스트에 대해서 실행
    for element in reversed(weight_dict.items()):
        # 기존 weight에 대한 최대값 변수 선언
        last_weight, last_value = element
        # 해당 물건을 넣었을 때의 무게에서 기존에 있었던 가치의 최댓값보다 크다면 갱신
        if last_weight + current_weight <= max_weight:
            if weight_dict[last_weight + current_weight] < last_value + current_value:
                weight_dict[last_weight + current_weight] = last_value + current_value
                # 해당 값이 전체 최댓값보다 크다면 마찬가지로 갱신
                if last_value + current_value > max_value:
                    max_value = last_value + current_value

# 최댓값 출력
print(max_value)
