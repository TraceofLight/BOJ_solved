# 가장 긴 증가하는 부분 수열

import sys

# 숫자의 갯수와 숫자 리스트 input
number_amount = int(sys.stdin.readline())
number_list = list(map(int, sys.stdin.readline().split()))

# 해당 숫자가 가장 마지막 숫자인 수열의 최고 길이를 받을 딕셔너리 선언
number_dict = {number_list[index]: 0 for index in range(number_amount)}
# 아무것도 없을 경우 추가
number_dict.update({0: 0})
# 최대 길이 변수 선언
max_length = 0

# 전체 숫자들에 대해서 기존 길이보다 길다면 해당 값으로 딕셔너리 갱신
for idx in range(number_amount):
    for element in number_dict.items():
        last_big_number, length = element
        if last_big_number < number_list[idx]:
            if number_dict[number_list[idx]] < length + 1:
                number_dict[number_list[idx]] = length + 1
                # 만약 그 길이가 최대길이라면 최대길이도 갱신
                if max_length < length + 1:
                    max_length = length + 1

# 결과 출력
print(max_length)

