# 2 番目に大きい整数

numbers = list(map(int, input().split()))
numbers.sort()
print(numbers[1])
