# 10부제

day = int(input())
car_list = list(map(int, input().split()))

result = 0
for each_car in car_list:
    if each_car == day:
        result += 1

print(result)
