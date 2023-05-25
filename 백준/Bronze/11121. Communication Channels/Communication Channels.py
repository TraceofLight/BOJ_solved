# Communication Channels

testcase = int(input())

for _ in range(testcase):
    input_val, output_val = input().split()
    if input_val == output_val:
        print('OK')
    else:
        print('ERROR')
