# Pizza Deal

from math import pi

a1, p1 = map(int, input().split())
r1, p2 = map(int, input().split())
slice_price = p1 / a1
full_price = p2 / (pow(r1, 2) * pi)

if slice_price < full_price:
    print('Slice of pizza')
elif slice_price > full_price:
    print('Whole pizza')
