# Every Second Counts

hour1, minute1, second1 = map(int, input().split(' : '))
hour2, minute2, second2 = map(int, input().split(' : '))

sum_sec1 = hour1 * 3600 + minute1 * 60 + second1
sum_sec2 = hour2 * 3600 + minute2 * 60 + second2

result = sum_sec2 - sum_sec1

if result < 0:
    print(86400 + result)
    
else:
    print(result)
