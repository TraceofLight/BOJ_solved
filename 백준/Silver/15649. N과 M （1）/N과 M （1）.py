# N과 M (1)

import sys

input = sys.stdin.readline


def permutation(target_list: list, target_limit: int, now_selected: int = 1) -> list:
    '''
    순열 함수
    '''

    # 이미 다 고른 경우 빈 리스트를 반환
    if now_selected > target_limit:
        return [[]]

    # 아직 고르지 않은 경우
    else:

        # 결과 리스트 선언
        result_list = []

        for idx in range(len(target_list)):

            # 아직 고르지 않은 것들 중에서 하나를 선택
            now_number = target_list[idx]

            # 그 하나를 제외한 나머지 숫자 리스트에 대해 순열 재귀 함수를 사용하여 나머지 숫자들에 대해 고른 리스트 중 하나씩 선택
            for next_list in permutation(target_list[:idx] + target_list[idx + 1:], target_limit, now_selected + 1):

                # 현재 고른 원소 1개 + 재귀 함수를 통해 반환한 (N - 1)개의 원소를 합친 리스트를 결과 리스트에 추가
                result_list.append([now_number] + next_list)

        # 결과 리스트를 반환
        return result_list


# 전체 숫자 범위, 선택할 갯수 입력
target_numbers, select_number = map(int, input().split())

# 함수를 호출하여 결과 반환
results = permutation(list(range(1, target_numbers + 1)), select_number)

# 문제 조건에 맞춰서 출력
for result in results:
    print(*result)
