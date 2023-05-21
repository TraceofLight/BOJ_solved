# 원 안의 점

from math import sqrt, isclose

testcase = int(input())
output = []

for _ in range(testcase):
    target_size = int(input())

    result_now = 0

    for one_length in range(1, target_size + 1):
        other_length = sqrt(pow(target_size, 2) - pow(one_length, 2))

        result = int(other_length)
        sudo_result = int(other_length) + 1

        if isclose(other_length, sudo_result):
            result_now += sudo_result
        else:
            result_now += result

    total_result = (result_now + target_size) * 4 + 1
    output.append(total_result)

for i in range(testcase):
    print(f"#{i + 1} {output[i]}")
