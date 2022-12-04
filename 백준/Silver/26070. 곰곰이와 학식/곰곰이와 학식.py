# 곰곰이와 학식

# 먹고 싶은 음식 종류와 티켓 입력
goms = list(map(int, input().split()))
tickets = list(map(int, input().split()))

# 결과 변수 선언
result = 0

# 현재 가진 티켓으로 해결 가능한만큼 식사
for each_idx in range(3):
    eat_gom = min(goms[each_idx], tickets[each_idx])
    goms[each_idx] -= eat_gom
    tickets[each_idx] -= eat_gom
    result += eat_gom

# 남은 티켓을 바꿔가면서 식사
for eat_counter in range(9):

    # 티켓 변환
    tickets[(eat_counter + 1) % 3] += tickets[eat_counter % 3] // 3
    tickets[eat_counter % 3] = tickets[eat_counter % 3] % 3

    # 식사
    eat_gom = min(goms[(eat_counter + 1) % 3], tickets[(eat_counter + 1) % 3])
    goms[(eat_counter + 1) % 3] -= eat_gom
    tickets[(eat_counter + 1) % 3] -= eat_gom
    result += eat_gom

# 결과 출력
print(result)
