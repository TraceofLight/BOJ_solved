# 기타콘서트

import sys
from itertools import combinations

input = sys.stdin.readline

guitar_number, song_number = map(int, input().split())

play_info = []

for _ in range(guitar_number):
    guitar_name, play_list = input().rstrip('\n').split()
    new_play_list = []
    for chr in play_list:
        if chr == 'Y':
            new_play_list.append('1')
        else:
            new_play_list.append('0')
    play_info.append(int('0b' + ''.join(new_play_list), 2))

sum_songs = 0b0

for idx in range(guitar_number):
    sum_songs = sum_songs | play_info[idx]

song_info = bin(sum_songs)
max_song = song_info[2:].count('1')

if not max_song:
    print(-1)

else:

    is_got_ans = False

    for guitar_amount in range(1, guitar_number + 1):
        for guitars in combinations(play_info, guitar_amount):
            union_result = 0b0
            for guitar in guitars:
                union_result = union_result | guitar
            if song_info == bin(union_result):
                result = guitar_amount
                is_got_ans = True
                break
        if is_got_ans:
            break

    print(result)
