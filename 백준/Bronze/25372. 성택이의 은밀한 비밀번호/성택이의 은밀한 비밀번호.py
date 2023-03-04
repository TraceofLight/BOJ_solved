# 성택이의 은밀한 비밀번호

import sys

input = sys.stdin.readline

password_amount = int(input())
output = []

for _ in range(password_amount):
    temp = input().rstrip('\n')
    
    if 6 <= len(temp) <= 9:
        output.append('yes')
        
    else:
        output.append('no')
        
for result in output:
    print(result)
