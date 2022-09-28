# SWEA_7465 창용 마을 무리의 개수

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


for each_case in range(testcase):

    # 사람의 수, 관계의 수 input
    person_number, line_number = map(int, input().split())

    # 각 인원의 소속 집합 정보를 담을 딕셔너리 선언
    set_dict = {idx: idx for idx in range(1, person_number + 1)}

    # 관계 정보 input
    for _ in range(line_number):
        person_1, person_2 = map(int, input().split())

        # 유니온 파인드 함수를 호출하여 두 사람을 하나의 무리로 만듦
        union_node(set_dict, person_1, person_2)

    # 무리의 갯수 체크를 위한 변수들 선언
    set_num_set = set()
    set_count = 0

    # 각 인원별 현재 속한 무리의 번호를 확인
    for each_person in range(1, person_number + 1):
        set_number = find_node(set_dict, each_person)

        # 현재 소속된 무리의 번호가 지금까지 확인된 적이 없다면 집합에 추가하고 카운팅
        if set_number not in set_num_set:
            set_count += 1
            set_num_set.add(set_number)

    # 무리의 수를 카운팅한 결과값을 출력 리스트에 추가
    output.append(set_count)

# 문제 조건에 따라서 출력
for output_idx in range(testcase):
    print(f'#{output_idx + 1} {output[output_idx]}')
