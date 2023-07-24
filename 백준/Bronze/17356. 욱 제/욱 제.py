# 욱 제

a, b = map(int, input().split())
m = (b - a) / 400
winning_possibility = 1 / (1 + pow(10, m))

print(winning_possibility)
