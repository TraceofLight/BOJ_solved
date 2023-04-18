# 멀티버스 Ⅱ

import sys
from itertools import combinations

input = sys.stdin.readline

space_number, planet_number = map(int, input().split())
space_dict = dict()

for _ in range(space_number):
    planets = list(map(int, input().split()))

    planet_information = list(set(planets))
    planet_information.sort()

    planet_size_dict = dict()

    counter = 0
    sort_result = []

    for each_planet in planet_information:
        planet_size_dict.update({each_planet: counter})
        counter += 1

    for each_planet in planets:
        sort_result.append(planet_size_dict.get(each_planet))

    result_tuple = tuple(sort_result)

    if space_dict.get(result_tuple) is None:
        space_dict[result_tuple] = 0

    space_dict[result_tuple] += 1

result = 0

for each_result in space_dict.values():

    if each_result > 1:
        result += each_result * (each_result - 1) // 2

print(result)
