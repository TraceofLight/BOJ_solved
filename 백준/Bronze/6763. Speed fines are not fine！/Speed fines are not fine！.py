# Speed fines are not fine!

limit_speed = int(input())
your_speed = int(input())

if your_speed - limit_speed >= 31:
    print('You are speeding and your fine is $500.')
elif 30 >= your_speed - limit_speed >= 21:
    print('You are speeding and your fine is $270.')
elif 20 >= your_speed - limit_speed >= 1:
    print('You are speeding and your fine is $100.')
else:
    print('Congratulations, you are within the speed limit!')
