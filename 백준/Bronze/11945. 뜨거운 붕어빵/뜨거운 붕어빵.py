# 뜨거운 붕어빵

height, width = map(int, input().split())
output = []

for _ in range(height):
    output.append(input()[::-1])

for each_line in output:
    print(each_line)
