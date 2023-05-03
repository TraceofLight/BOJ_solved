# Silnia

target_number = int(input())

result = 1
for i in range(1, target_number + 1):
    result *= i
    result %= 10
    
print(result)