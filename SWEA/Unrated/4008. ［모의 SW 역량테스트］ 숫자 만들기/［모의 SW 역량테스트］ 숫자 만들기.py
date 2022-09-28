# SWEA_4008 숫자 만들기

from heapq import *

# 테스트 횟수 및 출력 리스트 선언
testcase = int(input())
output = []

# INF 변수 선언
INF = 100000001

for each_case in range(testcase):

    # 숫자의 갯수 input
    number_amount = int(input())

    # 연산자 갯수는 숫자보다 1 적음
    max_calc = number_amount - 1

    # 연산자 정보 및 숫자 정보 input
    operator_list = list(map(int, input().split()))
    number_list = list(map(int, input().split()))

    # 연산 최소값, 최대값 변수 선언
    max_number = -INF
    min_number = INF

    # DFS 진행할 스택 선언 및 초기값 입력
    progress_stack = []
    progress_stack.append([number_list[0], 0, operator_list])

    while progress_stack:

        # 현재 숫자, 연산 횟수, 연산자 정보 pop
        now_number, calc_count, operator_status = progress_stack.pop()

        # 연산을 끝냈을 때 최대, 최소값을 넘어섰다면 갱신
        if calc_count == max_calc:
            if max_number < now_number:
                max_number = now_number
            if min_number > now_number:
                min_number = now_number

        # 연산이 마무리되지 않은 경우
        else:

            # 남은 연산자 정보 확인
            sum_count, sub_count, mul_count, div_count = operator_status

            # 덧셈이 가능한 경우
            if sum_count > 0:
                progress_stack.append([
                    now_number + number_list[calc_count + 1],
                    calc_count + 1,
                    [sum_count - 1, sub_count, mul_count, div_count],
                ])

            # 뺄셈이 가능한 경우
            if sub_count > 0:
                progress_stack.append([
                    now_number - number_list[calc_count + 1],
                    calc_count + 1,
                    [sum_count, sub_count - 1, mul_count, div_count],
                ])

            # 곱셈이 가능한 경우
            if mul_count > 0:
                progress_stack.append([
                    now_number * number_list[calc_count + 1],
                    calc_count + 1,
                    [sum_count, sub_count, mul_count - 1, div_count],
                ])

            # 나눗셈이 가능한 경우
            if div_count > 0:
                progress_stack.append([
                    int(now_number / number_list[calc_count + 1]),
                    calc_count + 1,
                    [sum_count, sub_count, mul_count, div_count - 1],
                ])

    # 연산의 최댓값과 최소값의 차이를 출력 리스트에 추가
    output.append(max_number - min_number)

# 문제 조건에 따라서 출력
for output_idx in range(testcase):
    print(f'#{output_idx + 1} {output[output_idx]}')
