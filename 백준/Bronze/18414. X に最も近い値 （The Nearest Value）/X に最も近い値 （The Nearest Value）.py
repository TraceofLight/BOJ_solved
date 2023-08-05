# X に最も近い値 (The Nearest Value)

x, l, r = map(int, input().split())

if r < x:
    print(r)
elif x < l:
    print(l)
else:
    print(x)
