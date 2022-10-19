# 파티가 끝나고 난 뒤

import sys

input = sys.stdin.readline

# 파티 밀도, 파티장 넓이 입력
party_density, party_people = map(int, input().split())

# 실제 파티 참석 인원 확인
real_party_number = party_density * party_people

# 신문 파티 참가자 정보 입력
party_peaple_list = list(map(int, input().split()))

# 결과 출력
for each_party in party_peaple_list:
    print(each_party - real_party_number, end=' ')
