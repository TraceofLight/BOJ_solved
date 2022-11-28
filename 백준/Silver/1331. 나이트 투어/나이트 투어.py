# 나이트 투어

import sys

input = sys.stdin.readline

# 나이트 이동 경로 입력
move_log = []
for _ in range(36):
    coord_1, coord_2 = input().rstrip('\n')
    coord_1 = ord(coord_1) - 65
    coord_2 = int(coord_2)
    move_log.append((coord_1, coord_2))

# 마지막 1회 반복 확인
move_log.append(move_log[0])

# 나이트 투어 확인 Flag 선언
is_knight_tour = True

# 중복 좌표가 존재할 경우 나이트 투어가 아님
if len(list(set(move_log))) != 36:
    is_knight_tour = False

# 중복 좌표가 존재하지 않는 경우 추가 조사
if is_knight_tour:

    # 모든 좌표에 대해서 나이트가 이동이 가능한지 확인
    for idx in range(36):
        now_coord, next_coord = move_log[idx], move_log[idx + 1]

        if not (
            (abs(now_coord[0] - next_coord[0]) == 2 and abs(now_coord[1] - next_coord[1]) == 1)
            or (abs(now_coord[0] - next_coord[0]) == 1 and abs(now_coord[1] - next_coord[1]) == 2)
        ):
            is_knight_tour = False
            break

# 문제 조건에 따라 결과 출력
if is_knight_tour:
    print('Valid')

else:
    print('Invalid')
