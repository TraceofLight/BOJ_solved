# 이칙연산

a, b, c = map(int, input().split())
result = int(max(a * b / c, a / b * c))

print(result)
