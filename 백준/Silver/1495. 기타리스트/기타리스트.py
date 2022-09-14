# 기타리스트

import sys

song_number, start_volume, max_volume = map(int, sys.stdin.readline().split())
change_volume_list = list(map(int, sys.stdin.readline().split()))
volume_dict = {idx: -1 for idx in range(max_volume + 1)}

for each_number in range(song_number + 1):
    if not each_number:
        volume_dict[start_volume] = each_number
    else:
        is_changed = False
        change_list = []
        for idx in range(max_volume + 1):
            if volume_dict.get(idx) == each_number - 1:
                if volume_dict.get(idx + change_volume_list[each_number - 1]) is not None:
                    change_list.append(
                        idx + change_volume_list[each_number - 1])
                    is_changed = True
                if volume_dict.get(idx - change_volume_list[each_number - 1]) is not None:
                    change_list.append(
                        idx - change_volume_list[each_number - 1])
                    is_changed = True
        if not is_changed:
            break
        else:
            for next_volume in change_list:
                volume_dict[next_volume] = each_number

if not is_changed:
    print(-1)
else:
    for idx in range(max_volume + 1):
        if volume_dict.get(idx) == song_number:
            end_volume = idx
    print(end_volume)
