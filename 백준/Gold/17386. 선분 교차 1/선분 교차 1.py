# 선분 교차 1

import sys

# 두 선분의 좌표 input
x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())

# 좌표 기반의 두 선분의 기울기 벡터 연산
vector1 = [x2 - x1, y2 - y1]
vector2 = [x4 - x3, y4 - y3]

# 벡터의 외적이 0이라면 평행이므로 교차하지 않음
if not (vector1[0] * vector2[1] - vector1[1] * vector2[0]):
    print(0)

# CCW를 활용한 문제 풀이
else:
    def ccw(spot1: list, spot2: list, spot3: list, spot4: list):
        vector1 = [spot2[0] - spot1[0], spot2[1] - spot1[1]]
        vector2 = [spot3[0] - spot1[0], spot3[1] - spot1[1]]
        vector3 = [spot4[0] - spot1[0], spot4[1] - spot1[1]]
        vector4 = [spot4[0] - spot3[0], spot4[1] - spot3[1]]
        vector5 = [spot1[0] - spot3[0], spot1[1] - spot3[1]]
        vector6 = [spot2[0] - spot3[0], spot2[1] - spot3[1]]
        if (((vector1[0] * vector2[1] - vector1[1] * vector2[0]) * (vector1[0] * vector3[1] - vector1[1] * vector3[0]) <= 0)
            and ((vector4[0] * vector5[1] - vector4[1] * vector5[0]) * (vector4[0] * vector6[1] - vector4[1] * vector6[0]) <= 0)):
            return 1
        else:
            return 0

    print(ccw([x1, y1], [x2, y2], [x3, y3], [x4, y4]))
