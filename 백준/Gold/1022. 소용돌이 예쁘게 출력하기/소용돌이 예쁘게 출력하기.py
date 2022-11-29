# 소용돌이 예쁘게 출력하기

import sys

input = sys.stdin.readline


def make_swirl(target_coordinate: list) -> int:
    '''
    좌표가 주어졌을 때 소용돌이 좌표값을 출력하는 함수
    '''

    target_y, target_x = target_coordinate

    # y = x 위의 좌표의 경우
    if target_x == target_y:

        # 0보다 같거나 클 때
        if target_x >= 0:

            return pow(2 * target_x + 1, 2)

        # 0보다 작을 때
        elif target_x < 0:

            return pow(2 * abs(target_x) + 1, 2) + 4 * target_x

    # y > x 인 경우
    elif target_x < target_y:

        criteria_coord = max(abs(target_x), abs(target_y))

        return pow(2 * criteria_coord + 1, 2) \
                - (abs(criteria_coord - target_x) + abs(criteria_coord - target_y))

    # y < x 인 경우
    elif target_x > target_y:

        criteria_coord = max(abs(target_x), abs(target_y))

        return pow(2 * criteria_coord + 1, 2) \
                - 8 * criteria_coord + (criteria_coord - target_x + criteria_coord - target_y)

def fill_blank(target: str, length: int) -> str:
    '''
    일정 길이에 맞춰 공백을 넣은 문자열로 반환하는 함수
    '''

    target_length = len(target)

    if target_length < length:

        return ' ' * (length - target_length) + target

    else:

        return target


# 목표 출력 좌표값 입력
row_from, col_from, row_to, col_to = map(int, input().split())

# 결과값들을 1차적으로 담을 리스트 선언
result = []

# 함수를 호출하여 결과 확인
for now_y in range(row_from, row_to + 1):
    for now_x in range(col_from, col_to + 1):
        result.append(make_swirl([now_y, now_x]))

# 결과값에 대해 문자열 변환 및 길이 획일화 작업
max_length = len(str(max(result)))
str_result = [fill_blank(str(el), max_length) for el in result]

# 문제 요구 조건에 따라서 출력
for now_y in range(row_to - row_from + 1):
    for now_x in range(col_to - col_from + 1):

        if now_x == col_to - col_from:
            print(str_result[now_y * (col_to - col_from + 1) + now_x], end="\n")

        else:
            print(str_result[now_y * (col_to - col_from + 1) + now_x], end=" ")
