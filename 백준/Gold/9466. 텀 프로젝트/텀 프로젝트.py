# 텀 프로젝트

import sys

input = sys.stdin.readline

# 케이스 횟수 및 출력 리스트 선언
testcase = int(input())
output = []

for each_case in range(testcase):

    # 학생 수 및 고른 팀원 리스트 입력
    student_number = int(input())
    target_people = list(map(int, input().split()))

    # 관계도 리스트 선언
    graph = [None for _ in range(student_number + 1)]

    # 관계 입력
    for idx in range(1, student_number + 1):
        graph[idx] = target_people[idx - 1]

    # 그룹에 속한 사람인지 아닌지 확인하는 리스트 선언
    is_checked = [False for _ in range(student_number + 1)]

    # 그룹에 속한 인원수를 카운팅하는 변수 선언
    result_count = student_number

    # 전체 학생에 대해서 조사
    for idx in range(1, student_number + 1):

        # 이미 그룹원이라면 진행하지 않음
        if is_checked[idx]:
            continue

        # 그룹원이 아닌 경우
        else:

            # 이동 기록을 담을 집합 선언
            move_log = set()

            # 탐색을 위한 스택 선언 및 초기값 입력
            progress_stack = []
            progress_stack.append(idx)

            # 탐색 진행
            while progress_stack:

                # 현재 학생 정보
                now_student = progress_stack.pop()

                # 이미 그룹이 있는 학생이면 중복이므로 break
                if is_checked[now_student]:

                    # 유망하지 않은 그룹원 전체 방문 처리
                    for each_person in move_log:
                        is_checked[each_person] = True
                    break

                # 혼자서 팀을 구성하는 경우
                if graph[now_student] == now_student:
                    is_checked[now_student] = True
                    result_count -= 1

                    # 모든 인원에 대해 방문 처리
                    for each_person in move_log:
                        is_checked[each_person] = True
                    break

                # 사이클을 완성한 경우
                elif move_log and now_student == idx:

                    # 모든 그룹원 그룹 처리
                    for each_person in move_log:
                        result_count -= 1
                        is_checked[each_person] = True
                    break
                
                # 사이클이 전체가 아닌 일부로 완성된 경우
                elif move_log and now_student in move_log:
                    
                    # 완성한 목록에 대해서만 그룹 처리
                    next_student = now_student

                    # 로그에 있으면서 사이클로 이어지는 부분만 그룹 추가
                    while graph[next_student] in move_log:

                        result_count -= 1
                        next_student = graph[next_student]

                        # 사이클 완성했다면 break
                        if next_student == now_student:
                            break

                    # 모든 인원에 대해 방문 처리
                    for each_person in move_log:
                        is_checked[each_person] = True
                    break

                # 전부 아니라면 집합에 현재 학생 정보 입력 후 다음 학생 확인
                else:
                    move_log.add(now_student)
                    progress_stack.append(graph[now_student])

    # 그룹이 아닌 학생 인원수를 출력 리스트에 추가
    output.append(result_count)

# 출력
for result in output:
    print(result)
