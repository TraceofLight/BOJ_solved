# Комната

w = int(input())
l = int(input())
h = int(input())

long = max(w, l)
short = min(w, l)

if short >= h * 2 and short * 2 >= long:
    print("good")
else:
    print("bad")
