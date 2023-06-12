# Zero or One

a, b, c = map(int, input().split())

if a == b and b == c:
    print('*')
elif b == c:
    print('A')
elif a == c:
    print('B')
elif a == b:
    print('C')
