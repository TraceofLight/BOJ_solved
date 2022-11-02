# 종이 접기

import sys

input = sys.stdin.readline

# 테스트 횟수 입력 및 출력 리스트 선언
testcase = int(input())
output = []

for _ in range(testcase):

    # 종이 정보 입력 및 길이 변수 선언
    paper_info = input().rstrip('\n')
    length = len(paper_info)

    # 접을 수 있다고 가정
    can_wrap = True

    # 가운데를 기준으로 접었을 때 겹쳐지는지 확인
    while True:

        # 커서 및 중간 인덱스 변수 선언
        cursor = 0
        mid = length // 2

        # 커서를 옮기면서 겹치는지 확인
        while cursor < mid:

            # 겹치는 방향이 틀렸다면 접을 수 없음
            if paper_info[cursor] == paper_info[length - cursor - 1]:
                can_wrap = False
                break

            # 해당 커서에서 가능하다면 추가 조사 진행
            cursor += 1

        # 못 접었다면 반복문 break
        if not can_wrap:
            break

        # 접었다면 길이 절반으로 줄여서 절반에 대해 접히는지 조사
        else:
            length = mid

            # 더 이상 접을 수 없다면 조사 종료
            if not length:
                break

    # Flag 값에 따라 출력 리스트에 결과 추가
    if can_wrap:
        output.append('YES')
    else:
        output.append('NO')

# 출력
for result in output:
    print(result)
