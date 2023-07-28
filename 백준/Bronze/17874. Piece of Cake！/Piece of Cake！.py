# Piece of Cake!

n, h, v = map(int, input().split())
result = max(h * v, (n - h) * v, h * (n - v), (n - h) * (n - v))
print(result * 4)
