# 개수 세기

# 정수의 갯수 input
number_amount = int(input())

# 정수 리스트 input
number_list = list(map(int, input().split()))

# 찾는 숫자 input
find_number = int(input())

# 결과 출력
print(number_list.count(find_number))
