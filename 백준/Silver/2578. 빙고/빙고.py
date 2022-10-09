import sys

bingo_list = []
for _ in range(5):
    bingo_list.append(list(map(int, sys.stdin.readline().split())))

bingo_dict_raw = []
for y_idx in range(5):
    for x_idx in range(5):
        number = bingo_list[y_idx][x_idx]
        bingo_dict_raw.append([number, [y_idx, x_idx]])
bingo_dict = dict(bingo_dict_raw)


def check_bingo(list_bingo):
    count_bingo = 0
    count_diagonal = 0
    for idx in range(5):
        if list_bingo[idx][idx] != '#':
            break
        else:
            count_diagonal += 1
            if count_diagonal == 5:
                count_bingo += 1
    count_diagonal_rev = 0
    for idx in range(5):
        if list_bingo[idx][4 - idx] != '#':
            break
        else:
            count_diagonal_rev += 1
            if count_diagonal_rev == 5:
                count_bingo += 1
    for row in list_bingo:
        if row == ['#','#','#','#','#']:
            count_bingo += 1
    for column in list(zip(*list_bingo)):
        if column == ('#','#','#','#','#'):
            count_bingo += 1
    return count_bingo


check_number = []
for _ in range(5):
    check_number.append(list(map(int, sys.stdin.readline().split())))

is_bingo = False
for y_index in range(5):
    for x_index in range(5):
        point = bingo_dict.get(check_number[y_index][x_index])
        bingo_list[point[0]][point[1]] = '#'
        if check_bingo(bingo_list) >= 3:
            print(y_index * 5 + x_index + 1)
            is_bingo = True
            break
    if is_bingo:
        break