# 별 찍기 - 10

import sys

# 한 변의 길이 input 및 별로 채워진 2차원 리스트 선언
star_length = int(sys.stdin.readline())
star_matrix = [['*' for _ in range(star_length)] for _ in range(star_length)]


# 조건에 맞는 별 지우는 함수 선언
def delete_star(list, start_y, start_x, length):
    # 1칸짜리의 경우 따로 공정이 필요하지 않음
    if length == 1:
        return None
    else:
        new_length = length // 3
        for y_index in range(start_y, start_y + length, new_length):
            for x_index in range(start_x, start_x + length, new_length):
                # 전체를 3 * 3 배열의 9칸으로 쪼갤 경우 가운데 칸만 별을 지우게 됨
                if y_index == start_y + new_length and x_index == start_x + new_length:
                    for idx_y in range(start_y + new_length, start_y + new_length * 2):
                        for idx_x in range(start_x + new_length, start_x + new_length * 2):
                            list[idx_y][idx_x] = ' '
                # 가운데 칸이 아닌 경우에 대해서 재귀로 변의 길이를 변경하여 진행
                else:
                    delete_star(list, y_index, x_index, new_length)


# 선언한 함수를 조건들을 바탕으로 호출
delete_star(star_matrix, 0, 0, star_length)

# 출력
for row in star_matrix:
    for idx in range(star_length):
        if idx != star_length - 1:
            print(row[idx], end='')
        else:
            print(row[idx], end='\n')
