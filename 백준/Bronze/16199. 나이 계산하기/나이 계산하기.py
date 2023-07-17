# 나이 계산하기

birth_year, birth_month, birth_day = map(int, input().split())
now_year, now_month, now_day = map(int, input().split())

if now_month > birth_month:
    print(now_year - birth_year)
elif now_month < birth_month:
    print(now_year - birth_year - 1)
else:
    if now_day >= birth_day:
        print(now_year - birth_year)
    else:
        print(now_year - birth_year - 1)
print(now_year - birth_year + 1)
print(now_year - birth_year)
