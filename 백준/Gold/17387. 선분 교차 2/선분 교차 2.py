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

                # 위치 관계가 성립하지 않다면 교차하지 않음
                else:
                    print(0)

            # 한 직선 위에 없다면 교차하지 않음
            else:
                print(0)

    # 평행하지 않을 경우
    else:
        # 문제 조건에 따라 1을 출력
        print(1)

# 함수의 반환값이 거짓일 경우 교차하지 않음
else:
    print(0)
