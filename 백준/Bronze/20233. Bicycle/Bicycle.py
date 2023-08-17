# Bicycle

fee_a = int(input())
time_cost_a = int(input())
fee_b = int(input())
time_cost_b = int(input())
total_use = int(input())

month_a = fee_a + max(0, total_use - 30) * time_cost_a * 21
month_b = fee_b + max(0, total_use - 45) * time_cost_b * 21

print(month_a, month_b)
