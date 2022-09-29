# PPAP

import sys
from collections import deque

input = sys.stdin.readline

# 문자열 input
string = deque(input().rstrip('\n'))

# 완료된 문자열을 담을 스택 선언
stack = []

# 스택의 길이 변수 선언
stack_length = 0

# 체크할 문자열이 남아있는 동안에만 반복
while string:

    # 스택에 문자열 1개 담고 확인
    stack.append(string.popleft())
    stack_length += 1

    # PPAP 문자열을 아직 확인할 수 없는 경우 continue
    if stack_length < 4:
        continue

    # PPAP 문자열에 대하여 점검
    else:
        # 스택 최상단에 대하여 반복 확인
        while stack_length >= 4 and (
            stack[-4] == 'P'
            and stack[-3] == 'P'
            and stack[-2] == 'A'
            and stack[-1] == 'P'
        ):
            # PPAP 문자열인 경우 P 1개만 남기고 전부 pop
            stack_length -= 3
            for _ in range(3):
                stack.pop()

# 문제 조건을 만족한다면 PPAP를 출력
if stack == ['P']:
    print('PPAP')

# 아니라면 NP를 출력
else:
    print('NP')
