# 母音を数える (Counting Vowels)

import sys

input = sys.stdin.readline

chr_number = int(input())
input_word = input().rstrip('\n')

result = 0
for each_chr in input_word:
    if each_chr in 'aeiou':
        result += 1
        
print(result)
