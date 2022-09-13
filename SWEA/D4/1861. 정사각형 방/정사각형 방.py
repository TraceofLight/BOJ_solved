# SWEA_1861 정사각형 방

from collections import deque, defaultdict

# 테스트 횟수 input
testcase = int(input())
# 출력 리스트 선언
output = []
# 델타이동 리스트 선언
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for each_case in range(testcase):

    # 전체 행렬의 너비 input
    length = int(input())
    # 좌표 숫자의 최대값을 기록할 변수 선언
    max_number = float('-inf')
    # 방 좌표별 숫자를 기록하는 딕셔너리 선언
    point_dict = dict()
    # 연결된 숫자로 이어진 방에 대한 그래프를 저장할 딕셔너리 선언
    point_line_dict = defaultdict(set)

    # 딕셔너리에 좌표별 숫자값을 추가
    for y_idx in range(length):
        row_number = list(map(int, input().split()))
        for x_idx in range(length):
            point_dict[(y_idx, x_idx)] = row_number[x_idx]

    # 행렬을 벗어나지 않는 범위 내에서 다음 방의 숫자값이 현재 방보다 1보다 클 경우 그래프에 추가
    for now_y in range(length):
        for now_x in range(length):
            for direction in directions:
                move_y, move_x = direction
                next_y = move_y + now_y
                next_x = move_x + now_x
                if next_y >= 0 and next_y < length and next_x >= 0 and next_x < length:
                    if point_dict[(next_y, next_x)] == point_dict[(now_y, now_x)] + 1:
                        point_line_dict[(now_y, now_x)].add((next_y, next_x))

    # 최대 길이와 시작점의 값을 저장할 변수 선언
    max_length = 0
    max_start_point_number = 0

    # 모든 방에 대해서 진행
    for start_y in range(length):
        for start_x in range(length):

            # 출발점 입력
            progress_que = deque([])
            progress_que.append([(start_y, start_x), 1])

            # BFS (모든 방에 대해서 진행)
            while progress_que:
                now_index, distance = progress_que.popleft()
                now_y, now_x = now_index

                # 미리 만들어 둔 그래프에 따라 1 증가한 좌표를 큐에 추가
                for next_point in point_line_dict[now_index]:
                    progress_que.append([next_point, distance + 1])

                    # 만약 최대 길이와 같을 경우, 출발점의 값만 최소값으로 갱신
                    if distance + 1 == max_length:
                        max_start_point_number = min(point_dict[(start_y, start_x)], max_start_point_number)
                    # 최고 길이를 갱신했을 경우, 최대 길이와 출발점의 값을 전부 갱신
                    elif distance + 1 > max_length:
                        max_length = distance + 1
                        max_start_point_number = point_dict[(start_y, start_x)]

    # 결과값을 출력 리스트에 추가
    output.append([max_start_point_number, max_length])

# 문제의 요구 조건에 맞춰서 출력
for output_idx in range(testcase):
    print(f'#{output_idx + 1}', *output[output_idx])
