# 주식왕 동호

def buy_n_sell(price_info: list, stock_number: int, month_info: int, total_money: int):
    '''
    가격 리스트와 월 정보, 현재 잔고가 주어졌을 때 구매하는 방법을 반환하는 함수
    '''

    next_month_price = [price_info[idx][month_info + 1] for idx in range(stock_number)]
    this_month_price = [price_info[idx][month_info] for idx in range(stock_number)]
    profit_list = [[next_month_price[idx] - this_month_price[idx], this_month_price[idx]] for idx in range(stock_number) if next_month_price[idx] - this_month_price[idx] > 0]

    cost_n_profit_list = [0 for _ in range(total_money + 1)]

    for each_profit, each_cost in profit_list:
        for check_cost in range(total_money + 1):
            if check_cost + each_cost <= total_money:
                if cost_n_profit_list[check_cost + each_cost] < cost_n_profit_list[check_cost] + each_profit:
                    cost_n_profit_list[check_cost + each_cost] = cost_n_profit_list[check_cost] + each_profit

    return total_money + cost_n_profit_list[total_money]


stock_number, data_length, first_input = map(int, input().split())

stock_info = []
for _ in range(stock_number):
    stock_info.append(list(map(int, input().split())))

now_money = first_input

for month in range(data_length - 1):
    now_money = buy_n_sell(stock_info, stock_number, month, now_money)

print(now_money)