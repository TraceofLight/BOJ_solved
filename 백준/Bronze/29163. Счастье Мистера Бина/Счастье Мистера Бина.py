# Счастье Мистера Бина

number_amount = int(input())

number_info = map(int, input().split())

count_even = 0
count_odd = 0
for number in number_info:
    if number % 2:
        count_odd += 1
    else:
        count_even += 1

if count_even > count_odd:
    print('Happy')
else:
    print('Sad')
