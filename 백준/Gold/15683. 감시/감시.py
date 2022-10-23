# 감시

import sys

input = sys.stdin.readline


def check_blind_spot(matrix: list, y_range: int, x_range: int) -> int:
    '''
    현재 사무실 내 사각지대 갯수를 반환하는 함수
    '''

    # 사각지대 변수 선언
    blind_here = 0

    # 모든 좌표에 대해서 조사
    for y_idx in range(y_range):
        for x_idx in range(x_range):

            # 해당 좌표값이 0일 경우만 카운팅
            if not matrix[y_idx][x_idx]:
                blind_here += 1

    # 결과 반환
    return blind_here


# 사무실 가로 및 세로 크기 입력
height, width = map(int, input().split())

# CCTV 정보 및 사무실 정보를 담을 리스트 선언
cctvs = []
work_space = []

# 초기 사각지대 갯수 확인
blind_spot = 0

# 사무실 정보 입력
for y_idx in range(height):

    # 행 정보 확인
    temp = list(input().split())

    # 모든 요소들에 대해 조사
    for x_idx in range(width):

        # 만약 CCTV가 있다면 리스트에 추가
        if temp[x_idx] in '12345':
            cctvs.append(((y_idx, x_idx), int(temp[x_idx])))

        # CCTV도 아니고 벽도 아니라면 초기 사각지대
        else:
            if temp[x_idx] == '0':
                blind_spot += 1

    # CCTV를 리스트에 추가
    work_space.append(list(map(lambda x: int(x), temp)))

# CCTV 갯수 변수 선언
cctv_amount = len(cctvs)

# CCTV 방향 정보 딕셔너리 선언
cctv_directions = {
    1: {0: [(1, 0)], 1: [(-1, 0)], 2: [(0, 1)], 3: [(0, -1)]},
    2: {0: [(1, 0), (-1, 0)], 1: [(0, 1), (0, -1)]},
    3: {0: [(-1, 0), (0, 1)], 1: [(0, 1), (1, 0)], 2: [(1, 0), (0, -1)], 3: [(0, -1), (-1, 0)]},
    4: {0: [(-1, 0), (0, 1), (0, -1)], 1: [(1, 0), (0, 1), (0, -1)], 2: [(1, 0), (-1, 0), (0, -1)], 3: [(1, 0), (-1, 0), (0, 1)]},
    5: {0: [(1, 0), (-1, 0), (0, 1), (0, -1)]},
}

# 각 CCTV의 방향 정보를 담은 리스트 선언
max_direction = ['dummy', 4, 2, 4, 4, 1]

# CCTV가 존재하지 않는 경우 기존 사각지대의 갯수를 출력
if not cctv_amount:
    print(blind_spot)

# 만약 존재한다면 CCTV 방향에 따른 사각지대의 갯수를 조사
else:

    # 최종 사각지대 갯수 변수 선언
    result = blind_spot

    def min_blind_spot(field: list, cctv_list: list, sight: dict, max_direction: list,
                       now_cctv: int = 0, y_range: int = height, x_range: int = width,
                       limit_cctv: int = cctv_amount) -> None:
        '''
        CCTV를 모두 최적의 상태로 설치할 때 최소 사각지대 갯수를 확인하는 함수
        '''

        # 결과값 전역 변수 등록
        global result

        # Back Tracking

        # 모든 CCTV를 전부 확인한 경우
        if now_cctv == limit_cctv:

            # 현재 사각지대 갯수 확인
            now_result = check_blind_spot(field, y_range, x_range)

            # 기존 최소값보다 작은 경우 갱신
            if result > now_result:
                result = now_result

            return

        # 아직 확인하지 않은 CCTV가 존재하는 경우
        else:

            # 현재 확인할 CCTV 정보 확인
            cctv_idx, cctv_type = cctv_list[now_cctv]

            # 좌표 분리
            y_cctv, x_cctv = cctv_idx

            # CCTV에 종류에 따라 감시 방향의 경우의 수만큼 조사
            for direction_code in range(max_direction[cctv_type]):

                # 현재 주시 방향 확인
                cctv_directions_now = sight[cctv_type][direction_code]

                # 해당 주시 방향에서 볼 수 있는 좌표를 담을 리스트 선언
                now_view = []

                # 깊이 탐색을 진행할 방향 설정
                for direction in cctv_directions_now:

                    # 이동 방향 좌표 분리
                    move_y, move_x = direction

                    # 초기 좌표 설정
                    now_y, now_x = y_cctv, x_cctv

                    # 해당 방향에 대해서 반복 조사
                    while True:

                        next_y, next_x = now_y + move_y, now_x + move_x

                        # 사무실 범위를 벗어나지 않은 경우
                        if 0 <= next_y < y_range and 0 <= next_x < x_range:

                            # 벽을 만났다면 반복 종료
                            if field[next_y][next_x] == 6:
                                break

                            # 벽을 만난 것이 아닐 경우
                            else:

                                # 해당 좌표가 사각지대일 경우
                                if not field[next_y][next_x]:

                                    # 리스트에 기록 후 비사각지대 처리
                                    now_view.append((next_y, next_x))
                                    field[next_y][next_x] = '#'

                                # 현재 좌표 갱신
                                now_y, now_x = next_y, next_x

                        # 사무실 범위를 벗어났다면 반복 종료
                        else:
                            break

                # 수집한 좌표들을 다음 CCTV에 조사
                min_blind_spot(field, cctvs, cctv_directions, max_direction, now_cctv + 1)

                # 초기화
                for y_idx, x_idx in now_view:
                    field[y_idx][x_idx] = 0

    # 함수를 호출하여 결과 도출
    min_blind_spot(work_space, cctvs, cctv_directions, max_direction)

    # 결과값 출력
    print(result)
