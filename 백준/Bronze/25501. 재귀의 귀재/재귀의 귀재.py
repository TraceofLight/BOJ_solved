# 재귀의 귀재

import sys

input = sys.stdin.readline


def is_palindrome(target_string: str) -> str:
    '''
    회문 판별 후 회문 여부 및 재귀 횟수를 반환하는 함수
    '''

    # 문자열 길이 확인
    length = len(target_string)
    recursion_counter = [0]

    # 재귀 함수를 호출하여 반환된 값을 재반환
    return [
        recursion(target_string, 0, length - 1, recursion_counter), 
        *recursion_counter
    ]

def recursion(target_string: str, start: int, end: int, counter: list):
    '''
    회문 판별을 진행하는 함수
    '''

    # 재귀 횟수 카운팅
    counter[0] += 1

    # 회문인 것으로 확인된 경우
    if start >= end:
        return 1

    # 회문이 아닌 경우
    elif target_string[start] != target_string[end]:
        return 0

    # 아직 확인하지 않은 문자열이 있는 경우 재귀 함수를 호출하여 확인
    else:
        return recursion(target_string, start + 1, end - 1, counter)


# 케이스 갯수 입력 및 출력 리스트 선언
testcase = int(input())
output = []

# 함수를 호출하여 반환된 결과값을 출력 리스트에 추가
for _ in range(testcase):
    output.append(is_palindrome(input().rstrip('\n')))

# 문제 조건에 따라 출력
for result in output:
    print(*result)
