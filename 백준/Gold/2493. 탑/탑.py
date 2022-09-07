# 탑

import sys
from collections import deque

tower_number = int(sys.stdin.readline())
tower_list = deque(list(map(int, sys.stdin.readline().rstrip('\n').split())))
progress = []
result = []

counter = 1
while tower_list:
    now_height = tower_list.popleft()
    if not progress:
        progress.append([now_height, counter])
        result.append(0)
    else:
        if now_height > progress[-1][0]:
            while progress and now_height > progress[-1][0]:
                progress.pop()
            if not progress:
                result.append(0)
            else:
                result.append(progress[-1][1])
            progress.append([now_height, counter])
        else:
            result.append(progress[-1][1])
            progress.append([now_height, counter])
    counter += 1

print(*result)