# 숫자 카드 2

import sys
from bisect import *

input = sys.stdin.readline

# 출력 리스트 선언
output = []

# 가진 카드의 갯수 및 카드 리스트 입력
have_card = int(input())
have_list = list(map(int, input().split()))

# 카드 숫자 크기 순으로 정렬
have_list.sort()

# 몇 개 가지고 있는지 확인할 숫자의 갯수와 목록 입력
need_card = int(input())
need_list = list(map(int, input().split()))

# 이진탐색을 통해 해당 숫자의 갯수 확인
for each_need in need_list:
    output.append(bisect_right(have_list, each_need) - bisect_left(have_list, each_need))

# 출력
print(*output)
