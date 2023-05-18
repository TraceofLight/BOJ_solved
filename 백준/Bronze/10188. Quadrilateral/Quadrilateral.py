# Quadrilateral

target_number = int(input())

for i in range(target_number):
    width, height = map(int, input().split())
    
    for _ in range(height):
        print('X' * width)
    if i != target_number - 1:
        print('')
