# 주식왕 동호

import sys

input = sys.stdin.readline


def buy_n_sell(price_info: list, stock_number: int, month_info: int, total_money: int):
    '''
    가격 리스트와 월 정보, 현재 자본이 주어졌을 때 최대 이익에서의 총자본을 반환하는 함수
    '''

    # 각 주식별 획득 가능한 순이익과 해당 주식의 원가 정보를 담은 리스트 선언
    # 손해를 보는 경우는 배제
    cost_profit_list = [
        [price_info[idx][month_info + 1] - price_info[idx][month_info], price_info[idx][month_info]] 
        for idx in range(stock_number) 
        if price_info[idx][month_info + 1] - price_info[idx][month_info] > 0
    ]

    # 각 금액별 최대 이윤을 담을 리스트 선언
    profits = [0 for _ in range(total_money + 1)]

    # 이득을 보는 모든 주식에 대해 조사
    for each_profit, each_cost in cost_profit_list:

        # 모든 금액에 대해 확인
        for base_cost in range(total_money + 1):

            # 기존 금액 + 이번에 구매할 주식의 가격이 전체 한도 이하일 때만 가능
            if base_cost + each_cost <= total_money:

                # 기존 금액에서의 순이익 + 이번 주식을 구매할 경우의 순이익이 동일 금액에서 최대 이익이라면 갱신
                if profits[base_cost + each_cost] < profits[base_cost] + each_profit:
                    profits[base_cost + each_cost] = profits[base_cost] + each_profit

    # 현재 자본에 금액 내 최대 순익을 더한 총 자본을 반환
    return total_money + profits[total_money]


# 주식 갯수, 매입 기간, 초기 자본 입력
stock_number, total_month, init_money = map(int, input().split())

# 주식 정보 입력
stock_info = []
for _ in range(stock_number):
    stock_info.append(list(map(int, input().split())))

# 현재 자본 변수 선언
now_money = init_money

# 함수를 호출하여 달마다 보유 가능한 최대 금액을 현재 자본 변수에 입력
for month in range(total_month - 1):
    now_money = buy_n_sell(stock_info, stock_number, month, now_money)

# 결과 출력
print(now_money)
