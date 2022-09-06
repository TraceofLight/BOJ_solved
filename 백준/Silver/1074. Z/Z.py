# Z

import sys


# 재귀를 통한 분할정복 함수 선언
def z_function(idx_x, idx_y, length, counter):
    # 가장 작은 2 * 2 사각형 단위에 대해서 순서 확인
    if length == 1:
        if idx_x <= 0:
            if idx_y <= 0:
                counter += 0
            else:
                counter += 2
        else:
            if idx_y <= 0:
                counter += 1
            else:
                counter += 3
        return counter
    # 나머지 사각형 단위의 경우 4분할 index 체크
    # 범위에 따라 변 길이가 절반인 함수 반환해서 재귀
    else:
        # 2, 3 사분면일 경우
        if idx_x <= 2 ** (length - 1) - 1:
            # 2 사분면
            if idx_y <= 2 ** (length - 1) - 1:
                counter += ((2 ** (length - 1)) ** 2) * 0
            # 3 사분면
            else:
                counter += ((2 ** (length - 1)) ** 2) * 2
                idx_y -= (2 ** (length - 1))
        # 1, 4 사분면일 경우
        else:
            idx_x -= (2 ** (length - 1))
            # 1 사분면
            if idx_y <= 2 ** (length - 1) - 1:
                counter += ((2 ** (length - 1)) ** 2) * 1
            # 4 사분면
            else:
                counter += ((2 ** (length - 1)) ** 2) * 3
                idx_y -= (2 ** (length - 1))
        return z_function(idx_x, idx_y, length - 1, counter)


# 2차원 배열의 너비 정보와 좌표 input 및 방문 순서 결과값 변수 선언
side_info, index_y, index_x = map(int, sys.stdin.readline().split())
counter = 0

# 함수 실행 후 결과값 출력
print(z_function(index_x, index_y, side_info, counter))
