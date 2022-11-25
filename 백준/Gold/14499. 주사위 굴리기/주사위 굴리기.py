# 주사위 굴리기

import sys

input = sys.stdin.readline

# 지도 크기, 주사위 좌표, 명령 갯수 입력
map_height, map_width, dice_y, dice_x, order_number = map(int, input().split())

# 지도 정보 입력
map_info = []
for _ in range(map_height):
    map_info.append(list(map(int, input().split())))

# 명령 리스트 선언
order_list = list(map(int, input().split()))

# 초기 주사위 정보 입력
dice_info = [0, 0, 0, 0, 0, 0]

# 명령에 따른 방향 움직임을 담은 좌표 딕셔너리 선언
direction_dict = {
    1: [1, 0],
    2: [-1, 0],
    3: [0, -1],
    4: [0, 1],
}

# 이동했을 때의 각 면의 위치를 반환하는 해시
dice_hash = {
    1: [2, 1, 5, 0, 4, 3],
    2: [3, 1, 0, 5, 4, 2],
    3: [1, 5, 2, 3, 0, 4],
    4: [4, 0, 2, 3, 5, 1],
}

# 출력 리스트 선언
output = []

# 모든 명령에 대해서 확인
for each_order in order_list:

    # 명령에 따른 다음 좌표 확인
    move_x, move_y = direction_dict[each_order]
    next_x, next_y = dice_x + move_x, dice_y + move_y

    # 이동 가능한 좌표에 대해서만 추가 조사
    if 0 <= next_x < map_width and 0 <= next_y < map_height:

        # 다음 좌표로 이동
        dice_x, dice_y = next_x, next_y

        # 굴림에 따른 주사위 면 정보 반영
        next_dice_info = [0, 0, 0, 0, 0, 0]
        for idx in range(6):
            next_dice_info[dice_hash[each_order][idx]] = dice_info[idx]

        # 바닥에 숫자가 있을 경우 카피 후 좌표값 0으로 변경
        if map_info[next_y][next_x]:
            next_dice_info[5] = map_info[next_y][next_x]
            map_info[next_y][next_x] = 0

        # 없다면 주사위 바닥에서 복사
        else:
            map_info[next_y][next_x] = next_dice_info[5]

        # 주사위 정보 갱신
        dice_info = next_dice_info[:]

        # 이동이 가능했을 경우 최상단 값을 출력 리스트에 추가
        output.append(dice_info[0])

# 출력
for result in output:
    print(result)
