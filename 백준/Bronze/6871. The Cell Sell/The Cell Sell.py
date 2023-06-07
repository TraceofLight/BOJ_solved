# The Cell Sell

daytime = int(input())
evening = int(input())
weekend = int(input())

result_a = max(daytime - 100, 0) * 0.25 + evening * 0.15 + weekend * 0.2
result_b = max(daytime - 250, 0) * 0.45 + evening * 0.35 + weekend * 0.25

print("Plan A costs " + f"{result_a:.2f}")
print("Plan B costs " + f"{result_b:.2f}")

if result_a > result_b:
    print("Plan B is cheapest.")
elif result_a < result_b:
    print("Plan A is cheapest.")
else:
    print("Plan A and B are the same price.")
