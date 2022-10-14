
testcase = int(input())
output = []

for _ in range(testcase):

    # 입력
    tree_number = int(input())
    tree_list = list(map(int, input().split()))

    # 최대 높이
    max_height = max(tree_list)

    # 남은 높이
    left_list = [max_height - tree_list[idx] for idx in range(tree_number)]

    odd_day = 0
    even_day = 0

    for each_left in left_list:
        even_day += each_left // 2
        odd_day += each_left % 2

    total_date = 0

    if even_day > odd_day:
        limit_val = (even_day - odd_day) // 3
        even_day -= limit_val
        odd_day += limit_val * 2
    
    while even_day >= odd_day + 2:
        even_day -= 1
        odd_day += 2

    max_day = max(odd_day * 2 - 1, even_day * 2)
    output.append(max_day)

# 출력
for output_idx in range(testcase):
    print(f'#{output_idx + 1} {output[output_idx]}')