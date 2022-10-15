# LCS

import sys

input = sys.stdin.readline

# 수열 입력
first_string = [None] + list(input().rstrip('\n'))
second_string = [None] + list(input().rstrip('\n'))

# 전체 수열 길이 확인
first_length = len(first_string) - 1
second_length = len(second_string) - 1

# 부분 수열 정보를 담을 리스트 선언
lcs_status = [[0 for _ in range(second_length + 1)] for _ in range(first_length + 1)]

# 두 문자열의 모든 문자를 대상으로 조사
for check_idx in range(1, first_length + 1):
    for other_idx in range(1, second_length + 1):

        
        # 현 문자열이 같을 경우 1을 추가
        if first_string[check_idx] == second_string[other_idx]:
            lcs_status[check_idx][other_idx] = lcs_status[check_idx - 1][other_idx - 1] + 1

        # 다를 경우 이전 최장 길이를 상속
        else:
            lcs_status[check_idx][other_idx] = max(
                lcs_status[check_idx - 1][other_idx], lcs_status[check_idx][other_idx - 1]
            )

# 문자열 전부 확인 후 결과값을 출력
print(lcs_status[first_length][second_length])
