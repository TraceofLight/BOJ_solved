# 과자 나눠주기

import sys

input = sys.stdin.readline


def give_cookie(snack_list: list, target_size: int) -> int:
    '''
    과자 크기와 갯수가 주어지고 길이가 주어질 때 만족하는 쿠키 갯수 반환하는 함수
    '''

    # 결과값 변수 선언
    result = 0

    # 모든 과자들에 대해서 조사
    for snack in snack_list:

        # 1개의 과자로 최대한 목표 사이즈의 과자 갯수 만들기
        result += snack // target_size

    # 결과값 반환
    return result

def find_snack_size(snack_list: list, snack_amount: int, target_amount: int) -> int:
    '''
    과자들의 크기와 나눠줄 사람 수가 주어질 때 과자의 최대 길이를 반환하는 함수
    '''

    # 과자 길이 범위 설정
    start = 1
    end = 1000000000

    # 포인터가 하나로 좁혀질 때까지 반복
    while start <= end:

        # 중간값 선택
        mid_length = (start + end) // 2

        # 중간값에서의 과자 갯수를 확인
        now_snack = give_cookie(snack_list, mid_length)

        # 목표보다 같거나 많이 나왔다면 길이를 늘림
        if now_snack >= target_amount:
            start = mid_length + 1

        # 목표보다 적게 나왔다면 길이를 줄임
        else:
            end = mid_length - 1

    # 결과 반환
    return end


# 조카의 수, 과자의 갯수 입력
cousin_number, snack_number = map(int, input().split())

# 과자 길이 정보 입력
snacks = list(map(int, input().split()))

# 함수를 호출하여 결과 확인
result = find_snack_size(snacks, snack_number, cousin_number)

# 출력
print(result)
