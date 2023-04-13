# 랩실에서 잘 자요

import sys

input = sys.stdin.readline

last_page, page_number = map(int, input().split())

page_set = set(map(int, input().split()))

ink_info = [1000 for _ in range(last_page + 1)]
ink_info[0] = 0

for each_page in range(1, last_page + 1):
    if each_page in page_set:
        ink_info[each_page] = ink_info[each_page - 1]

    else:
        for i in range(each_page):
            ink_info[each_page] = min(ink_info[each_page], ink_info[i] + 5 + 2 * (each_page - i))

print(ink_info[last_page])
