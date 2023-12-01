# Граничные клетки

width = int(input())
height = int(input())

if width == 1 and height == 1:
    print(1)
elif width == 1 or height == 1:
    print(width + height - 1)
else:
    print((width + height) * 2 - 4)
