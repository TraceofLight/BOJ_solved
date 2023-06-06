# 뉴턴과 사과

people_list = list(map(int, input().split()))
x, y, r = map(int, input().split())

result = 0
for i in range(1, 5):
    if x == people_list[i - 1]:
        result = i

print(result)
