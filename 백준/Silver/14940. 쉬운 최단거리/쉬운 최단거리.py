# 쉬운 최단거리

import sys
from collections import deque

input = sys.stdin.readline

height, width = map(int, input().split())

map_info = []
for i in range(height):
    temp = list(map(int, input().split()))
    for j in range(width):
        if temp[j] == 2:
            starting_point = [i, j]
    map_info.append(temp)

result = [[None for _ in range(width)] for _ in range(height)]
result[starting_point[0]][starting_point[1]] = 0

progress_queue = deque()
progress_queue.append(starting_point)
moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

while progress_queue:
    now_y, now_x = progress_queue.popleft()
    
    for each_move in moves:
        next_y = now_y + each_move[0]
        next_x = now_x + each_move[1]

        if 0 <= next_y < height and 0 <= next_x < width:
            if not map_info[next_y][next_x]:
                result[next_y][next_x] = 0
            else:
                if result[next_y][next_x] is None:
                    result[next_y][next_x] = result[now_y][now_x] + 1
                    progress_queue.append([next_y, next_x])

for i in range(height):
    for j in range(width):
        if result[i][j] is None:
            if not map_info[i][j]:
                result[i][j] = 0
            else:
                result[i][j] = -1

for each_row in result:
    print(*each_row)
