# 과자

snack, amount, balance = map(int, input().split())
print(max(snack * amount - balance, 0))
