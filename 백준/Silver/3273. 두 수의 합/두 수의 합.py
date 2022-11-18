# 두 수의 합

import sys

input = sys.stdin.readline

# 수열 길이 입력
arr_length = int(input())

# 수열 정보 입력
arr_list = list(map(int, input().split()))

# 목표 숫자 입력
target_number = int(input())

# 수열 정렬
arr_list.sort()

# Two Pointer Algorithm

# 두 개의 포인터가 가리키는 인덱스 설정
cursor_1 = 0
cursor_2 = arr_length - 1

# 카운팅 변수 선언
result = 0

# 포인터가 교차하기 전까지 반복
while cursor_1 < cursor_2:

    # 합이 목표값보다 작다면 1번 커서 전진
    if arr_list[cursor_1] + arr_list[cursor_2] < target_number:
        cursor_1 += 1

    # 합이 목표값보다 크다면 2번 커서 후진
    elif arr_list[cursor_1] + arr_list[cursor_2] > target_number:
        cursor_2 -= 1

    # 목표값과 일치한다면 카운팅 후 1번 전진, 2번 후진
    elif arr_list[cursor_1] + arr_list[cursor_2] == target_number:
        cursor_1 += 1
        cursor_2 -= 1
        result += 1

# 결과 출력
print(result)
