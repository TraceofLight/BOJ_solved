# 헌내기는 친구가 필요해

import sys

input = sys.stdin.readline

height, width = map(int, input().split())

matrix = []
for i in range(height):
    temp = input().rstrip('\n')

    for j in range(width):
        if temp[j] == 'I':
            starting_point = [i, j]
    
    matrix.append(temp)

is_visit = [[False for _ in range(width)] for _ in range(height)]
moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

progress_stack = [starting_point]
is_visit[starting_point[0]][starting_point[1]] = True

meeting_people = 0

while progress_stack:
    
    now_y, now_x = progress_stack.pop()

    if matrix[now_y][now_x] == 'P':
        meeting_people += 1

    for each_move in moves:
        next_y = now_y + each_move[0]
        next_x = now_x + each_move[1]

        if (
            0 <= next_y < height and
            0 <= next_x < width and 
            matrix[next_y][next_x] != 'X' and 
            not is_visit[next_y][next_x]
        ):
            is_visit[next_y][next_x] = True
            progress_stack.append([next_y, next_x])

if not meeting_people:
    print('TT')
else:
    print(meeting_people)
