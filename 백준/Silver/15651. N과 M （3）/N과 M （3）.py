# N과 M (3)

import sys

input = sys.stdin.readline


def product(target_list: list, list_length: int, target_select: int, now_seleted: int = 0):
    '''
    Cartesian Product Function
    '''

    # 원하는 갯수의 숫자를 전부 선택한 경우
    if target_select == now_seleted:

        # 결과로 빈 리스트 1개 반환
        result = [[]]

    # 아직 다 선택하지 않은 경우
    elif target_select > now_seleted:

        # 결과 리스트 선언
        result = []

        # 모든 원소에 대해 반복
        for idx in range(list_length):

            # 현재 원소 선택
            now_number = target_list[idx]

            # 남은 갯수만큼 고른 리스트들 중 하나와 조합한 결과를 결과 리스트에 추가
            for next_selection in product(target_list, list_length, target_select, now_seleted + 1):
                result.append([now_number] + next_selection)

    # 결과 반환
    return result


# 고르는 수의 범위와 고를 갯수 입력
total_number, selection = map(int, input().split())

# 조건에 따라 결과 출력
for each_production in product(list(range(1, total_number + 1)), total_number, selection):
    print(*each_production)
