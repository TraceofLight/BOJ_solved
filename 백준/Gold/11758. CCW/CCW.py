# CCW

import sys

# 정보 input
p1x, p1y = map(int, sys.stdin.readline().split())
p2x, p2y = map(int, sys.stdin.readline().split())
p3x, p3y = map(int, sys.stdin.readline().split())

# p1을 기준으로 한 벡터 2개 구하기
vector1 = (p2x - p1x, p2y - p1y)
vector2 = (p3x - p1x, p3y - p1y)

# 벡터의 외적이 0보다 크다면 반시계 방향
if vector1[0] * vector2[1] - vector1[1] * vector2[0] > 0:
    print(1)
# 0보다 작다면 시계 방향
elif vector1[0] * vector2[1] - vector1[1] * vector2[0] < 0:
    print(-1)
# 0이라면 일직선
else:
    print(0)

'''
# 이하 수정 전 코드
line_segment1 = (p2x - p1x, p2y - p1y)
line_segment2 = (p3x - p1x, p3y - p1y)
length1 = sqrt((p2x - p1x) ** 2 + (p2y - p1y) ** 2)
length2 = sqrt((p3x - p1x) ** 2 + (p3y - p1y) ** 2)
vector1 = ((p2x - p1x) / length1, (p2y - p1y) / length1)
vector2 = ((p3x - p1x) / length2, (p3y - p1y) / length2)

# 단위 벡터의 방향이 같거나 정확히 반대인 경우 0 출력
if (
    isclose(vector1[0], vector2[0])
    and isclose(vector1[1], vector2[1])
) or (
    isclose(vector1[0] + vector2[0], 0)
    and isclose(vector1[1] + vector2[1], 0)
):
    print(0)
# 벡터의 외적이 0보다 크다면 반시계 방향, 0보다 작다면 시계 방향
else:
    if vector1[0] * vector2[1] - vector1[1] * vector2[0] > 0:
        print(1)
    else:
        print(0)
'''
