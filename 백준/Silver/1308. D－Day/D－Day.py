# D - Day

import sys

input = sys.stdin.readline


def is_leap_year(year_number: int) -> bool:
    '''
    윤년인지 확인하고 윤년이 맞는지 아닌지 반환하는 함수
    '''

    # 400으로 나눠지는 경우
    if not year_number % 400:
        return True

    # 400으로 나눠 떨어지지 않으면서 100으로 나눠지는 경우
    elif not year_number % 100:
        return False

    # 100으로 나눠 떨어지지 않으면서 4로 나눠지는 경우
    elif not year_number % 4:
        return True

    # 모든 경우에 해당하지 않는 경우
    return False


# 날짜 입력
start_year, start_month, start_day = map(int, input().split())
end_year, end_month, end_day = map(int, input().split())

# 달력 정보를 담은 딕셔너리 선언
month_dict = {
    True: [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    False: [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
}

# 1000년을 초과하는 경우
if ((end_year - start_year == 1000 and end_month > start_month)
    or (end_year - start_year == 1000 and end_month >= start_month and end_day >= start_day)
    or (end_year - start_year > 1000)):

    # gg를 출력
    print('gg')

# 1000년을 초과하지 않는 경우
else:

    # 결과값 변수 선언
    result = 0

    # 동일년도일 경우
    if start_year == end_year:

        # 동일월인 경우
        if start_month == end_month:

            # 날짜 차이만 확인
            result = end_day - start_day

            # 조건에 따라 결과 출력
            print(f'D-{result}')

        # 동일월이 아닌 경우
        else:

            # 시작년도가 윤년인지 여부 확인
            check_start_year = is_leap_year(start_year)

            # 윤년 여부에 따른 월별 일수를 합산
            for each_month in range(start_month + 1, end_month):
                result += month_dict[check_start_year][each_month]

            # 남은 일수를 합산
            result += month_dict[check_start_year][start_month] - start_day
            result += end_day

            # 조건에 따라 결과 출력
            print(f'D-{result}')

    # 동일년도가 아닐 경우
    else:

        # 윤년인지에 따라서 연별 일수를 합산
        for each_year in range(start_year + 1, end_year):

            # 윤년이면 366일
            if is_leap_year(each_year):
                result += 366

            # 윤년이 아니라면 365일
            else:
                result += 365

        # 시작년도와 종료년도의 윤년인지 여부 확인
        check_start_year = is_leap_year(start_year)
        check_end_year = is_leap_year(end_year)

        # 윤년 여부에 따른 월별 일수를 합산
        for each_month in range(start_month + 1, 13):
            result += month_dict[check_start_year][each_month]
        for each_month in range(1, end_month):
            result += month_dict[check_end_year][each_month]

        # 남은 일수를 합산
        result += month_dict[check_start_year][start_month] - start_day
        result += end_day

        # 조건에 따라 결과 출력
        print(f'D-{result}')
