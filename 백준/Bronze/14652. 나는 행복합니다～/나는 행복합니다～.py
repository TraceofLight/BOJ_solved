height, width, target = map(int, input().split())

y_index = target // width
x_index = target % width

print(y_index, x_index)