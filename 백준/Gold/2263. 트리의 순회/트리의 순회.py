# 트리의 순회

import sys

# 재귀 한도 초과를 대비한 한계치 변경
sys.setrecursionlimit(1000000)

# 이진 트리의 노드 수 input
node_number = int(sys.stdin.readline())
# inorder 리스트 input
tree_inorder = list(map(int, sys.stdin.readline().split()))
# postorder 리스트 input
tree_postorder = list(map(int, sys.stdin.readline().split()))

# inorder 리스트를 기반으로 하는 딕셔너리 선언
inorder_dict = {tree_inorder[idx]: idx for idx in range(node_number)}


# postorder와 inorder를 기반으로 한 preorder 정렬 방식 함수 선언
def tree_preorder(inorder_dict:dict, postorder_list:list, start_inorder:int, start_postorder:int, length:int, result_list:list):
    # 길이가 1 이상인 경우에 대해서만 진행
    if length >= 1:
        # 후위순회의 경우 리스트의 Top이 root node
        root_node = postorder_list[start_postorder + length - 1]
        # root node를 출력
        result_list.append(root_node)
        # root node를 중위 순회에서 찾은 index를 기준으로 좌우가 갈리게 됨
        root_index = inorder_dict[root_node] - start_inorder
        # 좌우 노드에 대해서 재귀 실행
        tree_preorder(inorder_dict, postorder_list, start_inorder, start_postorder, root_index, result_list)
        tree_preorder(inorder_dict, postorder_list, start_inorder + root_index + 1, start_postorder + root_index, length - root_index - 1, result_list)


# 출력 리스트 선언
result = []

# 함수를 호출한 이후 결과 출력
tree_preorder(inorder_dict, tree_postorder, 0, 0, node_number, result)
print(*result)
