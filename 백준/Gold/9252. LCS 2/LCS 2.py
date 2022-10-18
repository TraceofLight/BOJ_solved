# LCS 2

import sys

input = sys.stdin.readline

# 두 문자열 입력
string1 = input().rstrip('\n')
string2 = input().rstrip('\n')

# 두 문자열의 길이 변수 선언
first_length = len(string1)
second_length = len(string2)

# Dynamic Programming을 활용한 LCS 알고리즘

# LCS 알고리즘의 사용을 위한 다차원 배열 선언
longest_subsequence = [['' for _ in range(second_length + 1)] for _ in range(first_length + 1)]

# 모든 문자열에 대해서 조사
for first_idx in range(1, first_length + 1):
    for second_idx in range(1, second_length + 1):

        # 문자열이 일치하는 경우
        if string1[first_idx - 1] == string2[second_idx - 1]:

            # 현재 공통 문자 바로 직전 최대값에 1 추가로 카운팅
            longest_subsequence[first_idx][second_idx] = (
                longest_subsequence[first_idx - 1][second_idx - 1] + string1[first_idx - 1]
            )

        # 문자열이 일치하지 않는 경우
        else:

            # 이전 최대값 확인
            last_case_1 = len(longest_subsequence[first_idx - 1][second_idx])
            last_case_2 = len(longest_subsequence[first_idx][second_idx - 1])

            # 둘 중에서 크거나 같은 값으로 현재 지점 갱신
            if last_case_1 >= last_case_2:
                longest_subsequence[first_idx][second_idx] = (
                    longest_subsequence[first_idx - 1][second_idx]
                )
            else:
                longest_subsequence[first_idx][second_idx] = (
                    longest_subsequence[first_idx][second_idx - 1]
                )

# 모든 문자열에 대해서 조사를 마친 값 확인
max_subsequence = longest_subsequence[first_length][second_length]

# 길이가 0인 경우 0을 출력
if not max_subsequence:
    print(0)

# 길이가 0이 아닌 경우 길이와 문자열을 출력
else:
    print(len(max_subsequence))
    print(max_subsequence)
