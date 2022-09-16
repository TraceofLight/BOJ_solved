# SWEA_1486 장훈이의 높은 선반

from itertools import combinations

# 케이스 횟수 input 및 출력 리스트 선언
testcase = int(input())
output = []

for each_case in range(testcase):
    # 사람 수, 목표 높이 input
    people_amount, target_height = map(int, input().split())
    # 사람들의 키 정보 input
    height_list = list(map(int, input().split()))
    # 목표 높이로부터의 최소 차이값 변수 선언
    min_height = 2000000000
    # 1명 사용부터 전체 사용까지 조사
    for people_number in range(1, people_amount + 1):
        # 사람 그룹을 고르는 경우의 수
        for people_combination in combinations(range(people_amount), people_number):
            # 유망하지 않을 경우 다음 순회로 넘어가기 위한 Flag 선언
            is_over = False
            # 탑의 높이 변수 선언
            sum_height = 0
            for each_people in people_combination:
                sum_height += height_list[each_people]
                # 탑의 높이가 이미 기존 최소값을 넘은 경우 유망하지 않음
                if sum_height > target_height + min_height:
                    is_over = True
                    break
            # 유망하지 않다면 다음 순회
            if is_over:
                continue
            # 연산이 마무리되었으며 기존 결과보다 작았으며 목표 높이보다 높을 경우 차이값 갱신
            elif sum_height < target_height + min_height and sum_height >= target_height:
                min_height = sum_height - target_height

    # 케이스 내에서 최소 차이값을 확인 후 출력 리스트에 추가
    output.append(min_height)

# 문제의 요구 조건에 맞춰 출력
for output_idx in range(testcase):
    print(f'#{output_idx + 1} {output[output_idx]}')
