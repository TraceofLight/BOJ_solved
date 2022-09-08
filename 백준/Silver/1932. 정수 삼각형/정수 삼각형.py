# 정수 삼각형

import sys

# 줄 갯수 input
line_number = int(sys.stdin.readline())
# 합산값을 갱신할 리스트 선언
triangle_list = []
for counter in range(1, line_number + 1):
    now_list = list(map(int, sys.stdin.readline().split()))
    # 1번 줄은 연산이 따로 필요없음
    if not triangle_list:
        triangle_list = now_list
    # 그 외의 경우에 대해서만 연산
    else:
        for idx in range(counter):
            # 맨 앞과 맨 뒤의 index는 내려올 수 있는 경로가 1개
            if not idx:
                now_list[idx] = now_list[idx] + triangle_list[idx]
            elif idx == counter - 1:
                now_list[idx] = now_list[idx] + triangle_list[idx - 1]
            # 그 사이의 값들에 대해서는 경로가 2개 있으며 둘 중 최대값만 기록
            else:
                now_list[idx] = max(
                    now_list[idx] + triangle_list[idx], 
                    now_list[idx] + triangle_list[idx - 1],
                )
        # 반복문 진행 후 다음 반복을 위해 리스트 갱신
        triangle_list = now_list

# 마지막 리스트에서 최대값을 출력
print(max(triangle_list))
