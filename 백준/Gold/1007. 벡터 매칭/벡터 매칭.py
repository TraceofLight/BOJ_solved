# 벡터 매칭

import sys
from math import sqrt
from itertools import combinations

input = sys.stdin.readline

# 테스트 횟수 및 출력 리스 선언
testcase = int(input())
output = []

for each_case in range(testcase):

    # 벡터 최소 길이 변수 선언
    min_vector = 300000

    # 좌표 갯수 입력
    coord_number = int(input())

    # x, y 전체 합산값과 좌표들을 담을 리스트 선언
    total_x = 0
    total_y = 0
    coord_list = []

    # 좌표 정보 입력
    for _ in range(coord_number):
        now_x, now_y = map(int, input().split())
        total_x += now_x
        total_y += now_y
        coord_list.append((now_x, now_y))

    # 해당 좌표들에 대해서 절반으로 나누고 해당 x, y 전체 합산
    for coord_set in combinations(coord_list, coord_number // 2):
        x_sum = sum([coord[0] for coord in coord_set])
        y_sum = sum([coord[1] for coord in coord_set])

        # 벡터 길이 연산값 확인
        vector_result = sqrt((total_x - 2 * x_sum) ** 2 + (total_y - 2 * y_sum) ** 2)

        # 기존 최소값보다 작다면 갱신
        if min_vector > vector_result:
            min_vector = vector_result

    # 결과값 출력 리스트에 추가
    output.append(min_vector)

# 출력
for result in output:
    print(result)
