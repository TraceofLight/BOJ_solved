# 행렬 제곱

import sys


# 행렬을 횟수만큼 곱하는 함수 선언
def multiple(procession_list:list, width_int, count_int, result_dict:dict):
    # 이미 있는 값은 그대로 반환
    if result_dict.get(count_int) is not None:
        return result_dict[count_int]
    # 없는 값에 대하여 연산
    else:
        # 0 혹은 1에 대해서는 1000에 대해 모듈러 연산을 진행한 기본값 반환
        if not count_int:
            elementary_matrix = [[0 for _ in range(width_int)] for _ in range(width_int)]
            for y_idx in range(width_int):
                for x_idx in range(width_int):
                    elementary_matrix[y_idx][x_idx] = 1
            result_dict[0] = elementary_matrix
            return result_dict[0]
        elif count_int == 1:
            rev_procession_list = [[element % 1000 for element in row] for row in procession_list]
            result_dict[1] = rev_procession_list
            return result_dict[1]
        else:
            # 분할 정복을 통한 연산
            result_proc = [[] for _ in range(width_int)]
            proc_1 = multiple(procession_list, width_int, count_int // 2, result_dict)
            proc_2 = multiple(procession_list, width_int, count_int - (count_int // 2), result_dict)
            for y_idx in range(width_int):
                for x_idx in range(width_int):
                    sum_element = sum([proc_1[y_idx][number] * proc_2[number][x_idx] for number in range(width_int)])
                    result_proc[y_idx].append(sum_element % 1000)
            result_dict[count_int] = result_proc
            return result_dict[count_int]

# 행렬의 너비, 곱셈 횟수, 행렬 input
width, count = map(int, sys.stdin.readline().split())
proc = []
for _ in range(width):
    proc.append(list(map(int, sys.stdin.readline().rstrip('\n').split())))
proc_dict = dict()

# 선언한 함수를 통해 결과 연산
result = multiple(proc, width, count, proc_dict)

# 문제 조건에 맞게 출력
for row in result:
    print(*row)
