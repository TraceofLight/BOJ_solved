# Betygsättning

x, y, z = map(int, input().split())
x_, y_, z_ = map(int, input().split())

if z == z_ and y == y_ and x == x_:
    print("A")
elif z == z_ and y == y_ and x <= x_ * 2:
    print("B")
elif z == z_ and y == y_:
    print("C")
elif z == z_ and y <= y_ * 2:
    print("D")
elif z == z_:
    print("E")
