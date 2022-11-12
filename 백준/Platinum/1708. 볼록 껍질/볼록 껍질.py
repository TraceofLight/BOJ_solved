# 볼록 껍질

import sys
from math import sqrt

input = sys.stdin.readline


def cos_angle(target_vector: list) -> float:
    '''
    0에서 Pi 범위에 대해 두 벡터의 cos 값을 반환하는 함수
    '''
    target_x, target_y = target_vector
    target_length = sqrt(pow(target_x, 2) + pow(target_y, 2))

    return target_x / target_length

def distance(point_1: list, point_2: list) -> int:
    '''
    두 점 사이의 거리를 반환하는 함수
    '''

    result = sqrt(pow(point_1[0] - point_2[0], 2) + pow(point_1[1] - point_2[1], 2))

    return result

def external_product(vector_1: list, vector_2: list) -> int:
    '''
    외적값을 반환하는 함수
    '''

    calc_result = vector_1[0] * vector_2[1] - vector_2[0] * vector_1[1]

    return calc_result

def ccw(spot_1: list, spot_2: list, spot_3: list) -> int:
    '''
    첫 선분을 기준으로 다음 선분이 어느 방향을 가리키는지 확인하는 함수
    '''

    vector_1 = [spot_2[0] - spot_1[0], spot_2[1] - spot_1[1]]
    vector_2 = [spot_3[0] - spot_1[0], spot_3[1] - spot_1[1]]

    ccw_result = external_product(vector_1, vector_2)

    if ccw_result > 0:
        return 1

    elif ccw_result < 0:
        return -1

    elif not ccw_result:
        return 0


# 정점의 갯수 입력 및 정점 리스트 선언
vertex_number = int(input())
vertex_list = []

# 기준점의 좌표를 담을 변수 선언
min_y_val = None
min_x_val = None

# 정점 좌표 입력
for _ in range(vertex_number):
    vertex_x, vertex_y = map(int, input().split())

    # 기준점 좌표가 없을 경우 지정
    if min_x_val is None:
        min_x_val = vertex_x
        min_y_val = vertex_y

    # 기준점보다 동일하거나 하단에 위치할 경우
    elif min_y_val >= vertex_y:

        # 동일한 y 좌표, 좌측인 경우 혹은 하단에 위치한 경우
        if (min_y_val == vertex_y and min_x_val > vertex_x) or min_y_val > vertex_y:

            # 기존 기준점은 리스트로 방출
            vertex_list.append([min_x_val, min_y_val])

            # 기준점을 새로 지정
            min_x_val = vertex_x
            min_y_val = vertex_y

        # 조건 미달이라면 정점 리스트에 추가
        else:
            vertex_list.append([vertex_x, vertex_y])

    # 기준점보다 위에 있다면 정점 리스트에 추가
    else:
        vertex_list.append([vertex_x, vertex_y])

# 기준점을 제외한 모든 정점의 cos값과 기준점으로부터의 거리를 정점 정보로 추가
for idx in range(vertex_number - 1):
    vertex_list[idx].append(cos_angle([vertex_list[idx][0] - min_x_val, vertex_list[idx][1] - min_y_val]))

# 각도에 따라서 정렬
vertex_list.sort(key= lambda x: x[2])

# 볼록 껍질에 해당하는 좌표들을 담을 리스트 선언
vertex_stack = [[min_x_val, min_y_val]]

# 볼록 껍질에 담긴 꼭지점의 갯수 변수 선언
convex_hull = 1

# CCW 방향 기준 변수 선언
ccw_constant = 1

# 모든 정점에 대해 체크
while vertex_list:

    # 조사할 정점 선택
    now_vertex = vertex_list.pop()

    # 선분 구성
    if convex_hull < 2:
        vertex_stack.append(now_vertex)
        convex_hull += 1

    else:

        # 기존 변에 대한 방향 확인
        check_ccw = ccw(vertex_stack[-2], vertex_stack[-1], now_vertex)

        # 기존 변과 완벽하게 동일한 방향을 가리키는 경우
        if not check_ccw:

            # 거리가 먼 점만 남기고 다른 점은 배제
            if distance(vertex_stack[-2], now_vertex) > distance(vertex_stack[-2], vertex_stack[-1]):
                vertex_stack.pop()
                vertex_stack.append(now_vertex)

        # 방향이 같다면 스택에 추가
        elif ccw_constant == check_ccw:
            vertex_stack.append(now_vertex)
            convex_hull += 1

        # 방향이 어긋난 경우
        elif ccw_constant != check_ccw:

            # 스택의 최상단이 볼록껍질에 적합한 좌표가 될 때까지 제거
            vertex_stack.pop()
            convex_hull -= 1

            # 사용하지 않은 현 좌표는 리스트로 반환
            vertex_list.append(now_vertex)

# 마지막 각도에 존재할 수 있는 한 직선 위의 지점들 배제
while vertex_stack[-1][2] == vertex_stack[-2][2]:
    vertex_stack.pop()
    convex_hull -= 1

# 결과 출력
print(convex_hull)
