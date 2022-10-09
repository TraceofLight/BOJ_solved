# 용돈 관리

import sys

input = sys.stdin.readline


def calc_withdrawal(spending_plan: list, max_money: int) -> int:
    '''
    1회 충전 시 보유 금액에 따라 얼마나 출금이 필요한지 반환하는 함수
    '''

    # 1회 선지급 (0원 소비가 없음)
    now_money = max_money
    result_count = 1

    # 모든 소비 계획에 대하여 조사
    for spent_today in spending_plan:

        # 현재 가진 돈보다 많은 돈을 소비할 경우
        if now_money < spent_today:

            # 1회 출금 후 소비
            result_count += 1
            now_money = max_money - spent_today

        # 현재 가진 돈으로 해결될 경우
        else:

            # 그냥 가진 돈으로 소비
            now_money -= spent_today

    # 출금 횟수를 반환
    return result_count

def spend_money(spending_plan: list, withdrawal: int) -> int:
    '''
    소비 계획과 인출 횟수가 주어질 때 최소 인출액을 반환하는 함수
    '''

    # 탐색 범위 변수 선언
    start = max(spending_plan)
    end = sum(spending_plan)

    # 두 값이 같아질 때까지 반복
    while start < end:

        # 중간값 변수 선언
        mid = (start + end) // 2
        
        # 중간값에 대하여 조사했을 때 인출 횟수가 적을 경우
        if calc_withdrawal(spending_plan, mid) <= withdrawal:

            # 1회 인출 금액을 줄임
            end = mid

        # 인출 횟수가 많을 경우
        else:

            # 1회 인출 금액을 늘림
            start = mid + 1

    # 범위로 잡아낸 인출액을 반환
    return start


# 소비할 날짜, 인출 횟수 입력
day_number, withdrawal_count = map(int, input().split())

# 소비 계획 입력
pay_plan = []
for _ in range(day_number):
    pay_plan.append(int(input()))

# 함수를 호출하여 최소 인출액 출력
print(spend_money(pay_plan, withdrawal_count))
