# 와글와글 숭고한

participation_list = list(map(int, input().split()))

if sum(participation_list) >= 100:
    print('OK')
elif min(participation_list) == participation_list[0]:
    print('Soongsil')
elif min(participation_list) == participation_list[1]:
    print('Korea')
elif min(participation_list) == participation_list[2]:
    print('Hanyang')
