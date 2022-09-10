# 도어매

import sys
from collections import deque

remember_limit = int(sys.stdin.readline())
row = deque(list(sys.stdin.readline().rstrip('\n')))

count_man = 0
count_woman = 0

# 줄이 존재할 때, 성별 인원 차이를 기억할 수 있는 한도 내에서만 입장 
while row and abs(count_man - count_woman) <= remember_limit:
    # 맨 앞 사람에 대해 확인
    front = row.popleft()
    # 한계치에 도달한 경우 확인
    if abs(count_man - count_woman) == remember_limit:
        # 남자가 많을 경우
        if count_man > count_woman:
            # 여자라면 입장
            if front == 'W':
                count_woman += 1
                continue
            # 아니라면 두 번째 사람에 대해서 체크
            else:
                if row:
                    next_person = row.popleft()
                    if next_person == 'W':
                        count_woman += 1
                        row.appendleft(front)
                        continue
                # 입장 가능 상한선에 도달했기 때문에 break
                    else:
                        break
                else:
                    break
        # 여자가 많을 경우
        elif count_woman > count_man:
            # 남자라면 입장
            if front == 'M':
                count_man += 1
            # 아니라면 두 번째 사람에 대해서 체크
            else:
                if row:
                    next_person = row.popleft()
                    if next_person == 'M':
                        count_man += 1
                        row.appendleft(front)
                        continue
                # 입장 가능 상한선에 도달했기 때문에 break
                    else:
                        break
                else:
                    break
    # 한계치에 도달하지 않았다면 계속 입장
    else:
        if front == 'M':
            count_man += 1
        else:
            count_woman += 1

print(count_man + count_woman)
