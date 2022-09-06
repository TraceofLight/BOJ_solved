# 명령 프롬프트

import sys

# 단어의 갯수 input
string_number = int(sys.stdin.readline().rstrip('\n'))

# 첫 단어 받기 및 길이 확인
first_string = list(sys.stdin.readline().rstrip('\n'))
length = len(first_string)

# 다음 단어부터 모든 단어에 대해서 체크
for _ in range(string_number - 1):
    this_string = list(sys.stdin.readline().rstrip('\n'))
    for idx in range(length):
        # 이미 다른 값 확인해서 ? 인 경우 continue
        if first_string[idx] == '?':
            continue
        else:
            # 다른 값이 확인이 될 경우 ? 로 변경
            if this_string[idx] != first_string[idx]:
                first_string[idx] = '?'

# 변경된 문자열 출력
print(''.join(first_string))
