# 대소문자 바꾸기

import sys

input = sys.stdin.readline

# 문자열 input
string = input().rstrip('\n')

# 받은 문자열 각 문자에 대해 조사
for each_chr in string:

    # 소문자에 포함되는 경우 대문자로 출력
    if each_chr in 'abcdefghijklmnopqrstuvwxyz':
        print(each_chr.upper(), end='')

    # 아닌 경우 소문자로 출력
    else:
        print(each_chr.lower(), end='')

# 마지막 문자에 대해서 줄바꿈 처리
print('\n')
