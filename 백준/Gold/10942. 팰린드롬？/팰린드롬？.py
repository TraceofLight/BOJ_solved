# 팰린드롬?

import sys

input = sys.stdin.readline

# 재귀 상한 수정
sys.setrecursionlimit(100001)

# 수열의 크기 및 수열 정보 입력
arr_number = int(input())
number_list = ['*'] + list(map(int, input().split()))

# Dynamic Programming

# 펠린드롬 정보를 담을 리스트 선언
pelindrome_info = [[None for _ in range(arr_number + 1)] for _ in range(arr_number + 1)]


def check_pelindrome(target_list: list, result_list: list, start: int, end: int) -> int:
    '''
    임의의 배열의 시작점과 끝점이 주어졌을 때 펠린드롬인지 아닌지 확인하는 함수
    '''

    # 값이 이미 존재하는 경우 조사하지 않음
    if result_list[start][end] is None:

        # 배열 길이가 1인 경우 무조건 펠린드롬
        if start == end:
            result_list[start][start] = 1
            result = 1

        # 배열 범위가 2인 경우
        elif start + 1 == end:

            # 두 수가 같다면 펠린드롬
            if target_list[start] == target_list[end]:
                result_list[start][end] = 1
                result = 1

            # 다르다면 펠린드롬이 아님
            else:
                result_list[start][end] = 0
                result = 0

        # 배열 범위가 2 이상인 경우
        else:

            # 앞뒤로 1칸씩 줄인 범위에 대해 조사
            last_result = check_pelindrome(target_list, result_list, start + 1, end - 1)

            # 해당 범위가 펠린드롬이 아니라면 당연히 펠린드롬이 아님
            if not last_result:
                result_list[start][end] = 0
                result = 0

            # 해당 범위에 대해 펠린드롬일 경우
            else:

                # 맨 앞과 맨 뒤가 같다면 펠린드롬
                if target_list[start] == target_list[end]:
                    result_list[start][end] = 1
                    result = 1

                # 다르다면 펠린드롬이 아님
                else:
                    result_list[start][end] = 0
                    result = 0

    # None이 아니라면 기존에 입력된 값을 반환
    else:
        result = result_list[start][end]

    # 결과를 반환
    return result

# 질문의 갯수 입력 및 출력 리스트 선언
qustion_number = int(input())
output = []

# 질문에 대한 결과를 함수를 호출하여 확인 후 출력 리스트에 추가
for _ in range(qustion_number):
    q_start, q_end = map(int, input().split())
    output.append(check_pelindrome(number_list, pelindrome_info, q_start, q_end))

# 출력
for result in output:
    print(result)
