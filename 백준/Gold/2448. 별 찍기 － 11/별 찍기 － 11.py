# 별찍기 - 11

import sys

# 높이 input 및 배열을 넣을 리스트 선언
height = int(sys.stdin.readline())
triange_list = []

# 필요한 범위의 asterisk에 대하여 전부 작성
for y_index in range(1, height + 1):
    triange_list.append(['*' for _ in range(2 * y_index - 1)])


# 조건에 따라서 별을 제거하는 함수 선언
def delete_star(list, y_idx, x_idx, length):
    if length == 3:
        list[y_idx + 1][x_idx + 1] = ' '
    else:
        new_length = length // 2
        counter = 1
        for target_y in range(y_idx + new_length, y_idx + length):
            for target_x in range(x_idx + counter * 2 - 1, x_idx + length):
                list[target_y][target_x] = ' '
            counter += 1
        delete_star(list, y_idx, x_idx, new_length)
        delete_star(list, y_idx + new_length, x_idx, new_length)
        delete_star(list, y_idx + new_length, x_idx + length, new_length)


# 함수를 통해 선언한 리스트에서 별을 제거
delete_star(triange_list, 0, 0, height)

# 출력
for idx in range(height):
    print(*(
        [' ' for _ in range(height - idx - 1)] 
        + triange_list[idx] 
        + [' ' for _ in range(height - idx - 1)]
    ), sep='')