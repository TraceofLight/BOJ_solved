# 트리 순회

import sys

input = sys.stdin.readline


def make_tree(graph: dict, parent: int, left_child: int, right_child: int) -> None:
    '''
    정보를 담을 딕셔너리와 노드 정보를 입력하면 트리를 만들어주는 함수
    '''

    # 양쪽이 전부 존재하는 케이스
    if left_child != -1 and right_child != -1:
        graph[parent] = [left_child, right_child]

    # 한 쪽만 존재하는 케이스
    elif left_child != -1:
        graph[parent] = [left_child, None]

    elif right_child != -1:
        graph[parent] = [None, right_child]

    # 둘 다 없는 케이스
    else:
        graph[parent] = [None, None]


def tree_inorder(tree: dict, root_node: int) -> list:
    '''
    중위 순회를 진행 후 순서를 반환하는 함수
    '''

    # 결과 리스트 선언
    result = []

    # 순회에 필요한 스택 선언
    stack = []

    # 확인할 노드 선언 및 초기값 루트로 설정
    now_root = root_node

    # 스택에 노드가 존재하거나 현재 노드가 값이 존재할 동안 진행
    while stack or now_root:

        # 현재 노드가 존재할 경우
        if now_root:

            # 해당 노드를 스택에 넣고 좌측 노드로 이동
            stack.append(now_root)
            now_root = tree[now_root][0]

        # 현재 노드의 값이 존재하지 않을 경우
        else:

            # 스택에 저장된 노드값으로 회귀
            now_root = stack.pop()

            # 해당 노드 순회 리스트에 추가
            result.append(now_root)

            # 이후 우측 노드로 이동
            now_root = tree[now_root][1]

    # 순회 결과를 반환
    return result


def find_stage(tree_dict: dict, root_node: int) -> dict:
    '''
    각 노드의 위계를 담은 딕셔너리를 반환하는 함수
    '''

    # 결과를 담을 딕셔너리 선언
    result_dict = dict()

    # 깊이 탐색을 진행할 스택 선언 및 초기값 입력
    progress_stack = []
    progress_stack.append((root_node, 1))

    # 깊이 탐색을 진행하면서 위계 기록
    while progress_stack:

        # 현재 노드 및 위계 정보 확인
        now_node, now_stage = progress_stack.pop()

        # 정보 기록
        result_dict[now_node] = now_stage

        # 자식 노드들에 대해 조사
        for child in tree_dict[now_node]:

            # 존재하는 노드라면 스택에 추가
            if child is not None:
                progress_stack.append((child, now_stage + 1))

    # 결과 딕셔너리를 반환
    return result_dict


# 노드 갯수 입력
node_number = int(input())

# 트리 그래프 선언
tree_dict = dict()

# 트리 정보 입력
for _ in range(node_number):
    now_parent, now_left, now_right = map(int, input().split())
    make_tree(tree_dict, now_parent, now_left, now_right)

# 함수를 호출하여 중위 순회 및 위계 확인
inorder = tree_inorder(tree_dict, 1)
stage_dict = find_stage(tree_dict, 1)

# 이동 카운팅 변수 선언 및 루트에서 첫 순회값까지 이동하는 값을 초기값으로 지정
move_counter = stage_dict[inorder[0]] - 1

# 다음 순회 노드랑 현재 노드와의 위계 차이를 합산
for idx in range(node_number - 1):
    move_counter += abs(stage_dict[inorder[idx]] -
                        stage_dict[inorder[idx + 1]])

# 결과 출력
print(move_counter)
