# Winning Score

sum_a = 0
for i in range(3):
    sum_a += (3 - i) * int(input())
sum_b = 0
for i in range(3):
    sum_b += (3 - i) * int(input())
    
if sum_a > sum_b:
    print('A')
elif sum_a < sum_b:
    print('B')
else:
    print('T')
