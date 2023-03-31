# Gnome Sequencing

import sys

input = sys.stdin.readline

gnome_number = int(input())
output = []

for _ in range(gnome_number):
    a, b, c = map(int, input().split())

    if (a < b < c) or (a > b > c):
        output.append(True)
        
    else:
        output.append(False)
        
print('Gnomes:')

for result in output:
    if result:
        print('Ordered')
    else:
        print('Unordered')
