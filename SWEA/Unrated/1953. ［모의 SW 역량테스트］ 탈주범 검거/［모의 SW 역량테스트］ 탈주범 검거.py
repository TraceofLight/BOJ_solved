# SWEA_1953 탈주범 검거

from collections import deque, defaultdict

# 테스트 케이스 10회
testcase = int(input())
# 출력 리스트 선언
output = []
# 델타이동 리스트 선언 (파이프 종류에 따라 다르게 분류)
directions = ['#',
            [[1, 0], [-1, 0], [0, 1], [0, -1]],
            [[1, 0], [-1, 0]],
            [[0, 1], [0, -1]],
            [[-1, 0], [0, 1]],
            [[1, 0], [0, 1]],
            [[1, 0], [0, -1]],
            [[-1, 0], [0, -1]]]

# 케이스 횟수만큼 반복
for each_case in range(testcase):

    # 전체 행렬의 너비 input
    height, width, hole_y, hole_x, max_time = map(int, input().split())

    # 파이프 연결을 기록할 그래프 딕셔너리 선언
    graph = defaultdict(set)
    for y_idx in range(height):
        row_number = list(map(int, input().split()))
        for x_idx in range(width):
            # 파이프가 있는 좌표에 한하여 가능한 통로 딕셔너리에 추가
            if row_number[x_idx]:
                for direction in directions[row_number[x_idx]]:
                    move_y, move_x = direction
                    next_y = y_idx + move_y
                    next_x = x_idx + move_x
                    if next_y >= 0 and next_y < height and next_x >= 0 and next_x < width:
                        graph[(y_idx, x_idx)].add((next_y, next_x))

    # 방문 기록 리스트 선언
    is_visited = [[False for _ in range(width)] for _ in range(height)]
    # 결과값 변수 선언
    available_spot = 0

    # 맨홀이 있는 지점에서부터 진행
    progress_que = deque([])
    progress_que.append([(hole_y, hole_x), 1])
    available_spot += 1
    is_visited[hole_y][hole_x] = True

    # BFS (시간 내의 가능 경로에 대해서 전수 조사)
    while progress_que:
        now_point, time = progress_que.popleft()
        if time < max_time:
            for connection in graph[now_point]:
                connect_y, connect_x = connection
                # 방문하지 않았던 점으로 한정(이미 방문한 점은 추가됨)
                if not is_visited[connect_y][connect_x]:
                    # 파이프가 양방향으로 연결된 경우에만 큐에 시간을 1 더하여 추가
                    if now_point in graph[(connect_y, connect_x)]:
                        progress_que.append([(connect_y, connect_x), time + 1])
                        is_visited[connect_y][connect_x] = True
                        available_spot += 1

    # 결과값을 출력 리스트에 추가
    output.append(available_spot)


# 문제의 요구 조건에 맞춰서 출력
for output_idx in range(testcase):
    print(f'#{output_idx + 1}', output[output_idx])
