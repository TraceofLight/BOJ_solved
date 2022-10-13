# 펠린드롬

import sys

input = sys.stdin.readline


def is_pelindrome(target_string: str) -> bool:
    '''
    펠린드롬인지 판별 후 T, F를 반환하는 함수
    '''

    # 문자열의 길이 확인
    length = len(target_string)

    # 길이 절반에 대해서만 확인
    for idx in range(length // 2):

        # 반대편 문자와 같지 않다면 False 반환
        if target_string[idx] != target_string[-(idx + 1)]:
            return False

    # 전부 통과했다면 True 반환
    return True


# 테스트 횟수 및 출력 리스트 선언
testcase = int(input())
output = []

for each_case in range(testcase):

    # 문자열 갯수 입력
    string_number = int(input())

    # 문자열 정보 입력
    string_list = []
    for _ in range(string_number):
        string_list.append(input().rstrip('\n'))

    # Flag 선언
    is_got_answer = False

    # 문자열 2개에 대하여 조사
    for first_idx in range(string_number):
        for second_idx in range(string_number):

            # 2개가 동일하지 않을 경우만 확인
            if first_idx != second_idx:
                check_string = string_list[first_idx] + string_list[second_idx]

                # 펠린드롬을 찾았다면 출력 리스트에 추가하고 break
                if is_pelindrome(check_string):
                    output.append(check_string)
                    is_got_answer = True
                    break

        # Flag를 활용하여 반복문 break
        if is_got_answer:
            break

    # 펠린드롬을 찾지 못한 경우 0을 출력 리스트에 추가
    if not is_got_answer:
        output.append(0)

# 출력
for result in output:
    print(result)
