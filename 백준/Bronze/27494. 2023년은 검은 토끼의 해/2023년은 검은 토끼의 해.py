# 2023년은 검은 토끼의 해

import sys
import re

input = sys.stdin.readline

ticket_number = int(input())

result = 0

# 패턴 생성
regex = re.compile('.*2.*0.*2.*3.*')

# 2023보다 작은 경우 당첨 티켓은 없음
if ticket_number < 2023:
    print(result)

else:

    # 2023보다 큰 경우 패턴 조사를 통해 당첨 티켓 수를 확인
    for each_ticket in range(2023, ticket_number + 1):
        if regex.match(str(each_ticket)):
            result += 1

    # 결과 출력
    print(result)
    