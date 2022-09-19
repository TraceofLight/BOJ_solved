# 거짓말

import sys
from collections import deque

input = sys.stdin.readline

# 사람의 수, 파티의 수 input
people_number, party_number = map(int, input().split())

# 진실을 아는 사람에 대한 정보 input 및 관련 리스트 선언
know_true_list = deque(list(map(int, input().split())))
know_true_number = know_true_list.popleft()

# 진실을 아는지의 여부에 대한 리스트 선언
is_know = [False for _ in range(people_number + 1)]

# 진실을 아는 사람들에 대해서 전부 True 처리
for person in know_true_list:
    is_know[person] = True

# 과장 횟수 카운터 선언
exaggerate_count = 0

# 진실 이야기하고 남은 파티를 넣을 스택 선언
left_party = []

# 관계도 그래프 형성

graph_dict = {idx: set() for idx in range(1, people_number + 1)}

# 파티 참가 인원 정보를 담을 리스트 선언
party_list = []

# 파티의 정보 input
for idx in range(party_number):

    # 데이터 처리
    party_info = deque(list(map(int, input().split())))
    number_of_people = party_info.popleft()

    # 파티 참가 인원 정보 리스트에 담기
    party_list.append(party_info)

    # 관계도 제작
    for person in party_info:
        for other_person in party_info:
            if not person == other_person:
                graph_dict[person].add(other_person)
                graph_dict[other_person].add(person)

# 큐 선언 및 초기값 처음에 진실을 알고 있는 사람들로 설정
progress_que = know_true_list

# BFS를 통해 진실을 들을 수 있는 사람 전부 True 처리
while progress_que:

    now_person = progress_que.popleft()

    for other_person in graph_dict[now_person]:

        if not is_know[other_person]:
            is_know[other_person] = True
            progress_que.append(other_person)

# 모든 파티에 대해 분석
for each_party in party_list:

    # Flag 선언
    allow_exaggerate = True

    # 아는 사람이 있다면 과장 불가
    for person in each_party:
        if is_know[person]:
            allow_exaggerate = False
            break

    # 전부 모른다면 과장 횟수 +1
    if allow_exaggerate:
        exaggerate_count += 1

# 과장 횟수 출력
print(exaggerate_count)
