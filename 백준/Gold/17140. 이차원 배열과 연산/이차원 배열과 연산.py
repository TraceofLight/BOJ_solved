# 이차원 배열과 연산

import sys

input = sys.stdin.readline


def dimension_down(target_arr: list) -> list:
    '''
    2차원 리스트를 1차원 리스트로 반환하는 함수
    '''

    # 결과 리스트 선언
    result = []

    # 인덱스 길이 카운팅 변수 선언
    idx_counter = 0

    # 내부 배열의 원소들을 전부 결과 리스트에 추가
    for each_arr in target_arr:
        for element in each_arr:
            result.append(element)

            # 카운팅하면서 100개 이상이 된 경우 그대로 반환
            idx_counter += 1
            if idx_counter == 100:
                return list(result)

    # 결과 리스트를 반환
    return list(result)

def sort_arr(target_arr: list) -> list:
    '''
    문제 규칙에 따라 배열을 정렬하는 함수
    '''

    # 정리 딕셔너리 선언
    target_dict = dict()

    # 배열의 모든 원소를 확인
    for each_element in target_arr:

        # 0이 아닌 경우
        if each_element:

            # 값이 없다면 해당 원소의 갯수는 1이라고 입력
            if target_dict.get(each_element) is None:
                target_dict[each_element] = 1

            # 이미 존재한다면 갯수 1 추가
            else:
                target_dict[each_element] += 1

    # 모든 원소쌍에 대해 확인해서 문제 조건에 따라 정리
    target_info = target_dict.items()
    sorted_target = sorted(list(target_info), key=lambda x: (x[1], x[0]))

    # 함수를 호출하여 1차원 리스트화
    result = dimension_down(sorted_target)

    # 결과 반환
    return result

def add_zero(target_arr: list) -> int:
    '''
    리스트의 모자라는 부분의 0을 채우고 최대 길이를 반환하는 함수
    '''

    # 각 내부 리스트들의 길이를 모은 리스트 선언
    length_info = [len(arr) for arr in target_arr]

    # 최대 길이와 2차원 리스트의 길이 변수 선언
    max_length = max(length_info)
    target_length = len(target_arr)

    # 2차원 리스트의 모든 원소 리스트에 대해 진행
    for idx in range(target_length):

        # 모자라는 길이만큼 0 추가
        for _ in range(max_length - length_info[idx]):
            target_arr[idx].append(0)

    # 최대 길이 반환
    return max_length

def calc_row(target_arr: list, col_len: list) -> list:
    '''
    문제 조건에 따른 행 연산 함수
    '''

    # 결과 리스트 선언
    result_arr = []

    # 함수를 호출하여 각 행에 대해 실행한 값을 결과 리스트에 추가
    for each_arr in target_arr:
        result_arr.append(sort_arr(each_arr))

    # 해당 리스트에 0을 추가하면서 반환된 열의 길이 변화를 기록
    col_len[0] = add_zero(result_arr)

    return result_arr

def calc_col(target_arr: list, row_len: list) -> list:
    '''
    문제 조건에 따른 열 연산 함수
    '''

    # 결과 리스트 선언
    result_arr = []

    # 함수를 호출하여 90도 돌린 목표 리스트에 대해 각 열에 대해 실행한 값을 결과 리스트에 추가
    for each_arr in zip(*target_arr):
        result_arr.append(sort_arr(each_arr))

    # 해당 리스트에 0을 추가하면서 반환된 행의 길이 변화를 기록
    row_len[0] = add_zero(result_arr)

    # 필요에 따라 회전된 리스트를 재회전하여 반환
    return list(zip(*result_arr))


# 목표 행렬 주소, 목표값 입력
target_row, target_col, target_val = map(int, input().split())
target_row -= 1
target_col -= 1

# 주어진 행렬 입력
init_list = [list(map(int, input().split())) for _ in range(3)]

# 현재 리스트 및 연산 횟수 카운터 선언
now_list = init_list
calc_counter = 0

# 결과값을 얻었는지 확인하는 Flag 선언
is_got_answer = False

# 행과 열의 길이 변수 선언
row_length = [3]
col_length = [3]

# 100회까지 반복
while calc_counter <= 100:

    # 만약 길이에 해당하는 주소가 존재하며 해당 주소가 목표값이랑 일치한다면 종료
    if target_row < row_length[0] and target_col < col_length[0] and now_list[target_row][target_col] == target_val:
        is_got_answer = True
        break

    # 목표값을 발견하지 못한 경우
    else:

        # 행이 더 길거나 같은 경우 행 연산
        if row_length[0] >= col_length[0]:
            now_list = calc_row(now_list, col_length)

        # 행이 더 짧은 경우 열 연산
        else:
            now_list = calc_col(now_list, row_length)

        # 횟수 카운팅
        calc_counter += 1

# 값을 구했다면 결과값을 반환
if is_got_answer:
    print(calc_counter)

# 못 구했다면 1을 반환
else:
    print(-1)
