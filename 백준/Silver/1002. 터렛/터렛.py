# 터렛

import sys
from math import sqrt

input = sys.stdin.readline

testcase = int(input())
output = []

for _ in range(testcase):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance_square = pow(x1 - x2, 2) + pow(y1 - y2, 2)

    if r1 > r2:
        
        if distance_square < pow(r1, 2):
            
            if distance_square < pow(r1 - r2, 2):
                result = 0

            elif distance_square == pow(r1 - r2, 2):
                result = 1

            else:
                result = 2

        elif distance_square == pow(r1, 2):
            result = 2

        else:
            if distance_square < pow(r1 + r2, 2):
                result = 2

            elif distance_square == pow(r1 + r2, 2):
                result = 1

            else:
                result = 0

    elif r1 == r2:

        if distance_square == 0:

            if r1 == 0:
                result = 1

            else:
                result = -1

        elif distance_square < pow(2 * r1, 2):
            result = 2

        elif distance_square == pow(2 * r1, 2):
            result = 1

        else:
            result = 0

    else:
        
        if distance_square < pow(r2, 2):
            
            if distance_square < pow(r2 - r1, 2):
                result = 0

            elif distance_square == pow(r2 - r1, 2):
                result = 1

            else:
                result = 2

        elif distance_square == pow(r2, 2):
            result = 2

        else:
            if distance_square < pow(r1 + r2, 2):
                result = 2

            elif distance_square == pow(r1 + r2, 2):
                result = 1

            else:
                result = 0

    output.append(result)

for result in output:
    print(result)
