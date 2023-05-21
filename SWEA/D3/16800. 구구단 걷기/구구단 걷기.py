# 구구단 걷기

from math import sqrt

testcase = int(input())
output = []

for _ in range(testcase):
    target_number = int(input())

    for i in range(int(sqrt(target_number)) + 1, 0, -1):
        if not target_number % i:
            output.append((target_number // i) + i - 2)
            break

for i in range(testcase):
    print(f"#{i + 1} {output[i]}")
