# The Merchant of Venice

testcase = int(input())
output = []

for _ in range(testcase):
    ships, speed, day_left = map(int, input().split())
    limit_dist = speed * day_left

    total_money = 0
    for _ in range(ships):
        distance, each_load = map(int, input().split())
        if limit_dist >= distance:
            total_money += each_load

    output.append(total_money)

for i in range(testcase):
    print(f'Data Set {i + 1}:')
    print(output[i])

    if i != testcase - 1:
        print()
