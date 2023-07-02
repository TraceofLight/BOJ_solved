# Hard choice

food1, food2, food3 = map(int, input().split())
people1, people2, people3 = map(int, input().split())

result = max(0, people1 - food1) + max(0, people2 - food2) + max(0, people3 - food3)
print(result)
