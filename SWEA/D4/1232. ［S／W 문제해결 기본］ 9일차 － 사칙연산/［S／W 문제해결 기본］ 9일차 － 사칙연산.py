# SWEA_1232 사칙 연산

# 케이스 횟수 input 및 출력 리스트 선언
testcase = 10
output = []

for each_case in range(testcase):

    # 노드 갯수 input
    node_number = int(input())
    # 노드에 대응하는 문자 혹은 숫자값을 반환하는 hash
    node_dict = {idx: None for idx in range(1, node_number + 1)}
    # 그래프 딕셔너리 선언
    graph_dict = {str(idx): [] for idx in range(1, node_number + 1)}
    for _ in range(node_number):
        node_info = list(input().split())
        node_dict[node_info[0]] = node_info[1]
        # 자식 노드가 있다면 그래프에 추가
        if len(node_info) >= 3:
            graph_dict[node_info[0]].append(node_info[2])
        if len(node_info) >= 4:
            graph_dict[node_info[0]].append(node_info[3])

    # 계산을 위한 함수 선언
    def calculate(val_dict: dict, graph: dict, parent_node: str):
        # 자식 노드를 체크
        child1, child2 = graph[parent_node]
        # 자식 노드가 연산자라면 하위 노드들에 대해서 재귀 함수 호출
        if not val_dict[child1].isnumeric():
            num1 = float(calculate(val_dict, graph, child1))
        else:
            num1 = float(val_dict[child1])
        if not val_dict[child2].isnumeric():
            num2 = float(calculate(val_dict, graph, child2))
        else:
            num2 = float(val_dict[child2])
        # 부모 노드의 연산자에 따른 결과값을 반환
        if val_dict[parent_node] == '+':
            return str(num1 + num2)
        elif val_dict[parent_node] == '-':
            return str(num1 - num2)
        elif val_dict[parent_node] == '*':
            return str(num1 * num2)
        elif val_dict[parent_node] == '/':
            return str(num1 / num2)

    # 함수 호출하여 결과값 확인 및 출력 리스트에 추가
    result = calculate(node_dict, graph_dict, '1')
    output.append(int(float(result)))

# 문제 조건에 맞춰서 출력
for output_idx in range(testcase):
    print(f'#{output_idx + 1}', output[output_idx])
