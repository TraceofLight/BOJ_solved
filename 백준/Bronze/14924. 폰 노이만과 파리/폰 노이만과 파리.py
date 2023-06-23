# 폰 노이만과 파리

train_speed, fly_speed, distance = map(int, input().split())
result = (distance // (train_speed * 2)) * fly_speed
print(result)
