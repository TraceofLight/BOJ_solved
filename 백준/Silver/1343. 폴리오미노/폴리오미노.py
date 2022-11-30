# 폴리오미노

import sys

input = sys.stdin.readline

# 보드판 입력
target_board = input().rstrip('\n')

# 결과값 변수 선언
result = ''

# 정상 결과 확인 Flag 및 카운팅 변수 선언
is_fill_the_board = True
blank_counter = 0

# 모든 문자열에 대해 조사
for each_chr in target_board:

    # X 인 경우 카운팅
    if each_chr == 'X':

        blank_counter += 1

    # .이 나왔을 경우 카운팅 마무리하고 정산
    if each_chr == '.':

        # 4칸은 전부 AAAA로 변환
        while blank_counter >= 4:
            result = result + 'AAAA'
            blank_counter -= 4

        # 남은 2칸에 대해서 BB로 변환
        if blank_counter >= 2:
            result = result + 'BB'
            blank_counter -= 2

        # 만약 변환하고도 남은 칸이 있다면 덮을 수 없음
        if blank_counter:
            is_fill_the_board = False
            break

        # 남은 칸이 없다면 .을 추가하고 다시 이어서 조사
        else:
            result = result + '.'
            continue

# 끊기지 않았을 경우에 대해 한 번 더 확인
if is_fill_the_board:

    while blank_counter >= 4:
        result = result + 'AAAA'
        blank_counter -= 4

    if blank_counter >= 2:
        result = result + 'BB'
        blank_counter -= 2

    if blank_counter:
        is_fill_the_board = False

# 결과가 덮을 수 있는 것으로 나온다면 그대로 출력
if is_fill_the_board:
    print(result)

# 아니라면 -1 출력
else:
    print(-1)
