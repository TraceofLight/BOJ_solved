# Congruent Numbers

from math import isclose

p1, q1, p2, q2 = map(int, input().split())

result = p1 * p2 / q1 / q2 / 2
int_result = int(result)

if isclose(result, int_result) or isclose(result, int_result + 1):
    print(1)

else:
    print(0)
