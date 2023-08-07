# The Walking Adam

testcase = int(input())

for _ in range(testcase):
    count = 0
    temp = input()
    for each_char in temp:
        if each_char != 'D':
            count += 1
        else:
            break
    print(count)
