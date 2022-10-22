# 알고리즘 수업 - 병합 정렬 1

import sys

input = sys.stdin.readline


def merge_sort(target: list, start: int, end: int, goal: int) -> list:
    '''
    입력된 대상 리스트에 대해서 병합정렬을 진행하고 결과를 반환하는 함수 
    '''

    # 정렬할 요소가 있는 경우에만 실행
    if start < end:

        # 중앙 좌표 확인
        mid = (start + end) // 2

        # 중앙 좌표 좌, 우에 대해서 리스트 정렬
        merge_sort(target, start, mid, goal)
        merge_sort(target, mid + 1, end, goal)

        # 해당 리스트들을 대소 관계에 맞춰 병합
        combine(target, start, mid, end, goal)

    # 결과 리스트를 반환
    return target


def combine(target: list, start: int, mid: int, end: int, goal: int) -> None:
    '''
    정렬된 두 리스트를 병합하는 함수
    '''

    # 전역 변수 반영
    global save_counter
    global result

    # 정렬된 값들을 임시로 저장할 리스트 선언
    temp = []

    # 포인터 2개 선언
    cursor_1 = start
    cursor_2 = mid + 1

    # 해당 포인터들이 둘 중 하나라도 마무리 지점까지 이동하기 전까지 반복
    while cursor_1 <= mid and cursor_2 <= end:

        # 리스트의 포인터가 가리키는 주소값 대소 비교해서 임시 리스트에 추가
        if target[cursor_1] < target[cursor_2]:
            temp.append(target[cursor_1])
            cursor_1 += 1
        else:
            temp.append(target[cursor_2])
            cursor_2 += 1

    # 포인터가 하나라도 마무리 지점에 닿은 경우 나머지 리스트 남은 값 전부 임시 리스트에 추가
    while cursor_1 <= mid:
        temp.append(target[cursor_1])
        cursor_1 += 1
    while cursor_2 <= end:
        temp.append(target[cursor_2])
        cursor_2 += 1

    # 모든 임시값을 실제 리스트에 반영
    counter = 0
    for each_element in temp:
        target[start + counter] = each_element
        counter += 1

        # 저장 횟수를 카운팅하고 목표 저장 횟수와 동일할 경우 출력 후 프로그램 종료
        save_counter += 1
        if save_counter == goal:
            result = each_element


# 배열 크기, 목표 저장 횟수 입력
list_length, target_saving = map(int, input().split())

# 리스트 입력
target_list = list(map(int, input().split()))

# 저장 횟수 카운터 및 결과값 선언
save_counter = 0
result = None

# 리스트에 대해서 병합 정렬을 진행하면서 저장 횟수 카운팅
merge_sort(target_list, 0, list_length - 1, target_saving)

# 정렬하는 동안 목표 저장 횟수에 도달하지 못한 경우 -1 출력
if result is None:
    print(-1)

# 도달한 경우 결과값 출력
else:
    print(result)
