# 문자와 문자열

import sys

input = sys.stdin.readline

string = input().rstrip('\n')
target_index = int(input())

print(string[target_index - 1])
