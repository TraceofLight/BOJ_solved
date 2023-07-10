# N과 M (9)

import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def custom_combination(number_list: list, max_select: int) -> list:
    '''
    특정 수 집합에서 임의의 갯수만큼 뽑아서 중첩 없이 순서대로 반환하는 함수
    '''

    if not max_select:
        return [[]]

    else:
        result = []

        if max_select:
            for i in range(len(number_list)):
                now_element = number_list[i]

                for each_combination in custom_combination(number_list[:i] + number_list[i + 1:], max_select - 1):
                    now_combination = [now_element] + each_combination
                    heappush(result, now_combination)

        return result


n, m = map(int, input().split())
numbers = list(map(int, input().split()))

combination_result = custom_combination(numbers, m)

last_result = None
while combination_result:
    now_pop = heappop(combination_result)

    if last_result != now_pop:
        print(*now_pop)
        last_result = now_pop
