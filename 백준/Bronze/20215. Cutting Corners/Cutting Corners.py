# Cutting Corners

from math import sqrt

width, height = map(int, input().split())
diagonal = sqrt(pow(width, 2) + pow(height, 2))

result = width + height - diagonal
print(result)
