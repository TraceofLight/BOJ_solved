# SWEA_1238 Contact

from collections import deque, defaultdict

# 테스트 케이스 10회
testcase = 10
# 결과 리스트 선언
output = []

for each_case in range(testcase):
    # 데이터 길이, 시작점 input
    data_length, start_node = map(int, input().split())
    # 그래프 선언
    graph = [set() for _ in range(100)]
    # 방문 기록 리스트 선언
    is_visited = [False for _ in range(100)]

    # 비상연락망 데이터 가공 후 input
    data = list(map(int, input().split()))
    for idx in range(data_length // 2):
        from_node, to_node = data[2 * idx], data[2 * idx + 1]
        from_node -= 1
        to_node -= 1
        graph[from_node].add(to_node)

    # 거리별 노드를 관리하는 딕셔너리 선언
    distance_dict = defaultdict(list)

    # BFS
    progress_que = deque([])
    progress_que.append([start_node - 1, 0])
    is_visited[start_node] = True
    while progress_que:
        now_node, distance = progress_que.popleft()
        distance_dict[distance].append(now_node)
        for element in graph[now_node]:
            if not is_visited[element]:
                is_visited[element] = True
                progress_que.append([element, distance + 1])

    # 가장 긴 거리에 위치하는 노드 리스트 확인
    counter = 100
    while distance_dict.get(counter) is None:
        counter -= 1
    max_distance_list = distance_dict.get(counter)

    # 그 중에서 가장 큰 노드 번호를 출력 리스트에 추가
    output.append(sorted(max_distance_list)[-1] + 1)

# 문제의 요구 조건에 맞춰서 출력
for output_idx in range(testcase):
    print(f'#{output_idx + 1} {output[output_idx]}')
