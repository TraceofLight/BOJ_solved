import sys

tetromino_move = [
    [[1, 0], [-1, 0], [1, 1]],
    [[1, 0], [-1, 0], [-1, 1]],
    [[1, 0], [-1, 0], [1, -1]],
    [[1, 0], [-1, 0], [-1, -1]],
    [[0, 1], [0, -1], [1, 1]],
    [[0, 1], [0, -1], [-1, 1]],
    [[0, 1], [0, -1], [1, -1]],
    [[0, 1], [0, -1], [-1, -1]],
    [[1, 0], [0, 1], [1, -1]],
    [[1, 0], [0, -1], [1, 1]],
    [[-1, 0], [0, 1], [1, 1]],
    [[1, 0], [0, 1], [-1, 1]],
    [[1, 0], [-1, 0], [0, 1]],
    [[1, 0], [-1, 0], [0, -1]],
    [[1, 0], [0, 1], [0, -1]],
    [[-1, 0], [0, 1], [0, -1]],
]

height, width = map(int, sys.stdin.readline().split())

matrix = []
for _ in range(height):
    matrix.append(list(map(int, sys.stdin.readline().split())))

max_sum = 0

for y_idx in range(height):
    for x_idx in range(width):
        for movement in tetromino_move:
            now_sum = matrix[y_idx][x_idx]
            counter = 0
            for direction in movement:
                check_y = y_idx + direction[0]
                check_x = x_idx + direction[1]
                if check_y >= 0 and check_y < height and check_x >= 0 and check_x < width:
                    now_sum += matrix[check_y][check_x]
                    counter += 1
                    if counter == 3:
                        if now_sum > max_sum:
                            max_sum = now_sum
                else:
                    break

for row in matrix:
    for x_index in range(width - 3):
        sum_number = sum(row[x_index : x_index + 4])
        if sum_number > max_sum:
            max_sum = sum_number

for x_idx in range(width):
    for y_idx in range(height - 3):
        sum_number = 0
        counter = 0
        while counter < 4:
            sum_number += matrix[y_idx + counter][x_idx]
            counter += 1
        if sum_number > max_sum:
            max_sum = sum_number

for y_index in range(height - 1):
    for x_index in range(width - 1):
        sum_number = 0
        for y_counter in range(2):
            for x_counter in range(2):
                sum_number += matrix[y_index + y_counter][x_index + x_counter]
        if sum_number > max_sum:
            max_sum = sum_number

print(max_sum)