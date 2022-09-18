# 선분 교차 2

import sys
from math import isclose

# 두 선분의 좌표 input
x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())

# 좌표 기반의 두 선분의 기울기 벡터 연산
vector1 = [x2 - x1, y2 - y1]
vector2 = [x4 - x3, y4 - y3]


# CCW 알고리즘을 활용한 교차 여부 체크 함수 선언
def ccw(spot1: list, spot2: list, spot3: list, spot4: list):
    vector1 = [spot2[0] - spot1[0], spot2[1] - spot1[1]]
    vector2 = [spot3[0] - spot1[0], spot3[1] - spot1[1]]
    vector3 = [spot4[0] - spot1[0], spot4[1] - spot1[1]]
    vector4 = [spot4[0] - spot3[0], spot4[1] - spot3[1]]
    vector5 = [spot1[0] - spot3[0], spot1[1] - spot3[1]]
    vector6 = [spot2[0] - spot3[0], spot2[1] - spot3[1]]
    if (((vector1[0] * vector2[1] - vector1[1] * vector2[0]) * (vector1[0] * vector3[1] - vector1[1] * vector3[0]) <= 0)
            and ((vector4[0] * vector5[1] - vector4[1] * vector5[0]) * (vector4[0] * vector6[1] - vector4[1] * vector6[0]) <= 0)):
        return True
    else:
        return False


# CCW를 활용한 문제 풀이

# 함수의 반환값이 참일 경우 교차
if ccw([x1, y1], [x2, y2], [x3, y3], [x4, y4]):

    # 벡터의 외적이 0이라면 평행할 경우
    if not (vector1[0] * vector2[1] - vector1[1] * vector2[0]):
        # 기울기 변수 선언 (x축에 수직인 경우가 아닐 경우)
        if vector1[0]:
            angle1 = vector1[1] / vector1[0]
            # 한 직선 위에 있는지 체크
            if isclose(y3, angle1 * (x3 - x1) + y1):
                # 한 직선 위에 있다면 위치 관계가 성립하는지 확인
                if (
                    (min(x1, x2) <= min(x3, x4) and max(x1, x2) >= min(x3, x4))
                    or (min(x3, x4) <= min(x1, x2) and max(x3, x4) >= min(x1, x2))
                ):
                    print(1)

                    # 한 점에서만 겹치는 경우 좌표 출력
                    x_list = sorted([x1, x2, x3, x4])
                    y_list = sorted([y1, y2, y3, y4])

                    # 평행하고 한 직선 위에 있는 네 점을 순서대로 나열했을 때 가운데 2개가 동일하다면 한 점에서만 교차
                    if x_list[1] == x_list[2]:
                        print(x_list[1], y_list[1])

                # 평행하지만 순서가 적절하게 성립하지 않은 경우 만나지 않음
                else:
                    print(0)

            # 한 직선 위에 있는 게 아니라면 만나지 않음
            else:
                print(0)

        # x축에 대해서 수직일 경우
        elif not vector1[0]:
            # 한 직선 위에 존재하는지 (x 좌표가 동일하다면 한 직선 위에 존재함)
            if x1 == x3:
                # 위치 관계가 성립하는지 확인
                if (
                    (min(y1, y2) <= min(y3, y4) and max(y1, y2) >= min(y3, y4))
                    or (min(y3, y4) <= min(y1, y2) and max(y3, y4) >= min(y1, y2))
                ):
                    print(1)

                    # 한 점에서만 겹치는 경우 좌표 출력
                    y_list = sorted([y1, y2, y3, y4])

                    # 평행하고 한 직선 위에 있는 네 점을 순서대로 나열했을 때 가운데 2개가 동일하다면 한 점에서만 교차
                    if y_list[1] == y_list[2]:
                        print(x1, y_list[1])

                # 위치 관계가 성립하지 않다면 교차하지 않음
                else:
                    print(0)

            # 한 직선 위에 없다면 교차하지 않음
            else:
                print(0)

    # 평행하지 않을 경우
    else:
        # 문제 조건에 따라 1을 출력 후 교차점 좌표 연산
        print(1)

        # 기울기 변수 선언 (x축에 수직인 경우가 아닐 경우)
        if vector1[0] and vector2[0]:
            angle1 = vector1[1] / vector1[0]
            angle2 = vector2[1] / vector2[0]

            # 교점의 x좌표 선언
            cross_x = ((angle1 * x1 - angle2 * x3) -
                       (y1 - y3)) / (angle1 - angle2)
            # 교점의 y좌표 선언
            cross_y = angle1 * (cross_x - x1) + y1

        # x축에 수직인 직선이 있는 경우 해당 x좌표를 포함한 경우만 교차
        elif not vector1[0]:
            angle2 = vector2[1] / vector2[0]
            cross_x = x1
            cross_y = angle2 * (cross_x - x3) + y3

        elif not vector2[0]:
            angle1 = vector1[1] / vector1[0]
            cross_x = x3
            cross_y = angle1 * (cross_x - x1) + y1

        # 정수형이면 정수형태로 정리
        if isclose(cross_x, int(cross_x)):
            cross_x = int(cross_x)
        elif isclose(cross_x, int(cross_x + 1)):
            cross_x = int(cross_x + 1)
        elif isclose(cross_x, int(cross_x - 1)):
            cross_x = int(cross_x - 1)
        if isclose(cross_y, int(cross_y)):
            cross_y = int(cross_y)
        elif isclose(cross_y, int(cross_y + 1)):
            cross_y = int(cross_y + 1)
        elif isclose(cross_y, int(cross_y - 1)):
            cross_y = int(cross_y - 1)

        # 좌표 출력
        print(cross_x, cross_y)

# 함수의 반환값이 거짓일 경우 교차하지 않음
else:
    print(0)
