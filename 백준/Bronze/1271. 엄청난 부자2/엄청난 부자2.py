# 엄청난 부자2

import sys

input = sys.stdin.readline

# 가진 돈, 나누어 가질 사람수 입력
total_money, div_number = map(int, input().split())

# 몫과 나머지를 출력
print(total_money // div_number)
print(total_money % div_number)
