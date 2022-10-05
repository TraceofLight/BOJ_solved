# 선분 그룹

import sys

input = sys.stdin.readline


def outer_product(vector: tuple, other_vector: tuple) -> int:
    '''
    2차원 벡터 2개를 입력하면 외적값을 반환하는 함수
    '''

    # x, y 성분 분해
    vector_x, vector_y = vector
    other_vector_x, other_vector_y = other_vector

    # 외적 연산
    result = vector_x * other_vector_y - vector_y * other_vector_x

    # 결과 반환
    return result


def check_ccw(coord_1: list, coord_2: list, coord_3: list, coord_4: list) -> bool:
    '''
    두 선분이 주어졌을 때 교차하는지 확인하는 함수
    '''

    # x, y 성분 분해
    coord_1_x, coord_1_y = coord_1
    coord_2_x, coord_2_y = coord_2
    coord_3_x, coord_3_y = coord_3
    coord_4_x, coord_4_y = coord_4

    # 연산에 필요한 벡터 연산
    vector_1 = (coord_2_x - coord_1_x, coord_2_y - coord_1_y)
    vector_2 = (coord_3_x - coord_1_x, coord_3_y - coord_1_y)
    vector_3 = (coord_4_x - coord_1_x, coord_4_y - coord_1_y)
    vector_4 = (coord_4_x - coord_3_x, coord_4_y - coord_3_y)
    vector_5 = (coord_2_x - coord_3_x, coord_2_y - coord_3_y)
    vector_6 = (coord_1_x - coord_3_x, coord_1_y - coord_3_y)

    # 결과 확인에 필요한 외적 연산
    result1 = outer_product(vector_1, vector_2) * \
        outer_product(vector_1, vector_3)
    result2 = outer_product(vector_4, vector_5) * \
        outer_product(vector_4, vector_6)

    # check_CCW 연산 진행한 값이 둘 다 0일 경우
    if result1 == 0 and result2 == 0:

        # 위치 관계를 만족했을 경우 True 반환
        if (
            min(coord_1_x, coord_2_x) <= max(coord_3_x, coord_4_x)
            and max(coord_1_x, coord_2_x) >= min(coord_3_x, coord_4_x)
            and min(coord_1_y, coord_2_y) <= max(coord_3_y, coord_4_y)
            and min(coord_3_y, coord_4_y) <= max(coord_1_y, coord_2_y)
        ):
            return True

    # 두 외적 연산의 방향이 반대면 선분 교차이므로 True 반환
    elif result1 <= 0 and result2 <= 0:
        return True

    # 조건을 만족하지 못한 경우라면 False 반환
    return False


def find_root(hash_dict: dict, target_hash: list) -> int:
    '''
    해당 선분이 어떤 집합 소속인지 확인하는 함수
    '''

    if hash_dict[target_hash] == target_hash:
        return target_hash

    else:
        hash_dict[target_hash] = find_root(hash_dict, hash_dict[target_hash])
        return hash_dict[target_hash]


def make_connection(hash_dict: dict, hash_1: tuple, hash_2: tuple):
    '''
    선분들의 연결이 있는지 없는지 확인하고 집합을 하나로 합쳐주는 함수
    '''

    # 대표 집합 인덱스 확인
    root_union_1, root_union_2 = find_root(
        hash_dict, hash_1), find_root(hash_dict, hash_2)

    # 이미 같다면 추가 작업 필요 없음
    if root_union_1 == root_union_2:
        return

    # 다르다면 일치화 작업 실행
    else:
        if root_union_2 > root_union_1:
            hash_dict[root_union_2] = root_union_1

        else:
            hash_dict[root_union_1] = root_union_2


# 선분 갯수 입력
line_number = int(input())

# 선분 정보를 담을 딕셔너리 선언
line_dict = dict()

# 선분 그룹 정보를 담을 딕셔너리 선언
union_dict = {idx: idx for idx in range(1, line_number + 1)}

# 선분 정보 입력
for line_idx in range(1, line_number + 1):
    x1, y1, x2, y2 = map(int, input().split())
    line_dict[line_idx] = ((x1, y1), (x2, y2))

# 모든 선분에 대해서 조사
for first_line in range(1, line_number + 1):
    for second_line in range(first_line + 1, line_number + 1):

        # 시작점 및 끝점 정보로 분해
        coord_1, coord_2 = line_dict[first_line]
        coord_3, coord_4 = line_dict[second_line]

        # 만약 연결된 선분이라면 두 선분의 그룹을 합칠 것
        if check_ccw(coord_1, coord_2, coord_3, coord_4):
            make_connection(union_dict, first_line, second_line)

# 그룹 갯수 변수 선언
group_number = 0

# 가장 크기가 큰 그룹의 선분 갯수 변수 선언
max_group = 0

# 카운팅 딕셔너리 선언
count_group = {idx: 0 for idx in range(1, line_number + 1)}

# 모든 선분에 대해서 조회
for each_line in range(1, line_number + 1):

    # 다른 선분들과 이어지지 않은 경우
    if union_dict[each_line] == each_line:
        group_number += 1
        count_group[each_line] += 1

    # 다른 선분과 이어진 경우
    else:
        # 해당하는 그룹 번호에 카운팅
        count_group[find_root(union_dict, each_line)] += 1

    # 최대값보다 커진 경우 갱신
    if max_group < count_group[find_root(union_dict, each_line)]:
        max_group = count_group[find_root(union_dict, each_line)]

# 전체 그룹 갯수 출력
print(group_number)

# 가장 크기가 큰 그룹의 선분 갯수 출력
print(max_group)
