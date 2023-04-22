# Fly me to the Alpha Centauri

import sys

input = sys.stdin.readline

distance_dict = dict()

max_distance = 0
counter = 0
while max_distance < 2200000000:
    counter += 1
    max_distance += (counter + 1) // 2
    distance_dict[counter] = max_distance

testcase = int(input())
output = []
counter = 0

for _ in range(testcase):
    start, end = map(int, input().split())
    distance = end - start

    counter = 1
    while distance_dict[counter] < distance:
        counter += 1

    output.append(counter)

for result in output:
    print(result)
