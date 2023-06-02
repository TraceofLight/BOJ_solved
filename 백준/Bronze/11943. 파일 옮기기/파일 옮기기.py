# 파일 옮기기

first_apple, first_orange = map(int, input().split())
second_apple, second_orange = map(int, input().split())

print(min(second_apple + first_orange, first_apple + second_orange))
