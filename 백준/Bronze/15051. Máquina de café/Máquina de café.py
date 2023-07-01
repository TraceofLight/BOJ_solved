# Máquina de café

floor1 = int(input())
floor2 = int(input())
floor3 = int(input())

result1 = 2 * floor1 + floor2
result2 = floor1 + floor3
result3 = 2 * floor3 + floor2

print(2 * min(result1, result2, result3))
