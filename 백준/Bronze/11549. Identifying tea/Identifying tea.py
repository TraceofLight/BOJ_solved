# Identifying tea

answer = int(input())
result_list = list(map(int, input().split()))

count = 0
for each_answer in result_list:
    if answer == each_answer:
        count += 1
        
print(count)
