# PIZZA ALVOLOC

import sys

input = sys.stdin.readline

# 좌표 입력
(point_1_x, point_1_y, point_2_x, point_2_y, 
point_3_x, point_3_y, point_4_x, point_4_y) = map(int, input().split())

# 각 좌표 변수 분리
point_1 = [point_1_x, point_1_y]
point_2 = [point_2_x, point_2_y]
point_3 = [point_3_x, point_3_y]
point_4 = [point_4_x, point_4_y]


def outer_product(vector_1: list, vector_2: list) -> int:
    '''
    외적을 연산한 값을 반환하는 함수
    '''

    product_result = vector_1[0] * vector_2[1] - vector_1[1] * vector_2[0]

    return product_result

def check_cross(vertex_1: list, vertex_2: list, vertex_3: list, vertex_4: list) -> int:
    '''
    두 선분이 교차하는지 확인하는 함수
    '''

    vector_1 = [vertex_2[0] - vertex_1[0], vertex_2[1] - vertex_1[1]]
    vector_2 = [vertex_3[0] - vertex_1[0], vertex_3[1] - vertex_1[1]]
    vector_3 = [vertex_4[0] - vertex_1[0], vertex_4[1] - vertex_1[1]]
    vector_4 = [vertex_4[0] - vertex_3[0], vertex_4[1] - vertex_3[1]]
    vector_5 = [vertex_1[0] - vertex_3[0], vertex_1[1] - vertex_3[1]]
    vector_6 = [vertex_2[0] - vertex_3[0], vertex_2[1] - vertex_3[1]]

    result_one = outer_product(vector_1, vector_2) * outer_product(vector_1, vector_3)
    result_another = outer_product(vector_4, vector_5) * outer_product(vector_4, vector_6)

    if result_one < 0 and result_another < 0:
        return True

    else:
        return False


# 함수를 호출하여 교차 여부를 확인, 교차한 경우 나눠먹을 수 있음
if (
    check_cross(point_1, point_2, point_3, point_4)
):
    print(1)

# 그렇지 않다면 나눠먹을 수 없음
else:
    print(0)
