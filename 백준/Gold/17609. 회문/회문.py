# 회문

import sys

input = sys.stdin.readline


def check_pelindrome(target_string: str, start: int, end: int, is_remove_chr: bool = False) -> int:
    '''
    펠린드롬, 유사 펠린드롬을 확인하고 결과값을 정수로 반환하는 함수
    '''

    # Two Pointer Algorithm

    # 포인터 2개 설정
    cursor_1 = start
    cursor_2 = end

    # 두 포인터가 교차하기 전까지 확인
    while cursor_1 < cursor_2:

        # 포인터가 가리킨 문자가 동일하다면 두 포인터 이동
        if target_string[cursor_1] == target_string[cursor_2]:
            cursor_1 += 1
            cursor_2 -= 1

        # 아직 제거한 문자가 없고 동일하지 않을 경우
        elif not is_remove_chr and target_string[cursor_1] != target_string[cursor_2]:

            # 앞 포인터나 뒷 포인터를 하나 이동시킨 경우에 펠린드롬인지 확인
            if (
                not check_pelindrome(target_string, cursor_1 + 1, cursor_2, True)
                or not check_pelindrome(target_string, cursor_1, cursor_2 - 1, True)
            ):
                # 펠린드롬이라면 유사 펠린드롬
                return 1

            # 펠린드롬이 아닌 경우
            else:

                # 유사 펠린드롬도 펠린드롬도 아님
                return 2

        # 문자열을 1개 배제했으나 여전히 펠린드롬이 아닌 경우
        elif is_remove_chr and target_string[cursor_1] != target_string[cursor_2]:

            # 펠린드롬도 유사 펠린드롬도 아님
            return 2

    # 반복을 정상적으로 통과한 경우 일반적인 펠린드롬
    return 0


# 문자열 갯수 입력 및 출력 리스트 선언
string_number = int(input())
output = []

# 문자열 정보 입력
for _ in range(string_number):
    now_string = input().rstrip('\n')

    # 해당 문자열에 대해서 함수를 호출하여 도출된 결과값을 출력 리스트에 추가
    output.append(check_pelindrome(now_string, 0, len(now_string) - 1))

# 출력
for result in output:
    print(result)
