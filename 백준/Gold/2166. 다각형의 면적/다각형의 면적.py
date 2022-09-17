# 다각형의 면적

import sys

input = sys.stdin.readline

# 꼭지점의 갯수 input
point_number = int(input())

# 좌표를 기록할 리스트 선언
point_x = []
point_y = []

# 좌표 정보 input
for _ in range(point_number):
    each_x, each_y = map(int, input().split())
    point_x.append(each_x)
    point_y.append(each_y)

# 가우스의 면적 공식을 활용
point_x.append(point_x[0])
point_y.append(point_y[0])

sum1 = 0
sum2 = 0
for idx in range(point_number):
    sum1 += point_x[idx] * point_y[idx + 1]
    sum2 += point_x[idx + 1] * point_y[idx]

result = abs(sum1 - sum2) / 2

# 결과 출력
print(result)
