# 색종이

import sys

input = sys.stdin.readline

# 흰색 도화지 상태 리스트 선언
total_paper = [[0 for _ in range(100)] for _ in range(100)]

# 색종이 갯수 입력
color_papers = int(input())

# 색종이 정보 입력
for _ in range(color_papers):
    start_x, start_y = map(int, input().split())
    start_x -= 1
    start_y -= 1

    # 색종이만큼 검은 영역 표시
    for y_idx in range(start_y, start_y + 10):
        for x_idx in range(start_x, start_x + 10):
            total_paper[y_idx][x_idx] = 1

# 결과 변수 선언
result = 0

# 칸마다 체크 후 표시된 영역이라면 카운팅
for y_idx in range(100):
    for x_idx in range(100):
        if total_paper[y_idx][x_idx]:
            result += 1

# 결과 출력
print(result)
