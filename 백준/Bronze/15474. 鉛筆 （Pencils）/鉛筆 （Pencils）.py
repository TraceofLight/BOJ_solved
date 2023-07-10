# 鉛筆 (Pencils)

from math import ceil

n, a, b, c, d = map(int, input().split())
set1_result = ceil(n / a) * b
set2_result = ceil(n / c) * d

print(min(set1_result, set2_result))
