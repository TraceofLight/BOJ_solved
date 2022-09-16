# 물통

import sys

input = sys.stdin.readline

# 물통 3개의 용량 input
bottle_a, bottle_b, bottle_c = map(int, input().split())

# DFS로 전수조사
progress_stack = []
progress_stack.append((0, 0, bottle_c))

# 방문 기록 리스트 선언
is_visited = set()
is_filled = [False for _ in range(bottle_c + 1)]

# 초기값 기록
is_filled[bottle_c] = True

# DFS 진행하면서 방문기록 계속 체크
while progress_stack:

    now_a, now_b, now_c = progress_stack.pop()

    # A 물병에 채우는 경우, 다 채울 수 있는 경우와 아닌 경우로 구분

    # C에서 A으로
    if now_c - (bottle_a - now_a) >= 0:
        if (bottle_a, now_b, now_c - (bottle_a - now_a),) not in is_visited:
            progress_stack.append((bottle_a, now_b, now_c - (bottle_a - now_a),))
            is_visited.add((bottle_a, now_b, now_c - (bottle_a - now_a),))

    else:
        if (now_a + now_c, now_b, 0,) not in is_visited:
            progress_stack.append((now_a + now_c, now_b, 0,))
            is_visited.add((now_a + now_c, now_b, 0,))

    # B에서 A으로
    if now_b - (bottle_a - now_a) >= 0:
        if (bottle_a, now_b - (bottle_a - now_a), now_c,) not in is_visited:
            progress_stack.append((bottle_a, now_b - (bottle_a - now_a), now_c,))
            is_visited.add((bottle_a, now_b - (bottle_a - now_a), now_c,))
    else:
        if (now_a + now_b, 0, now_c,) not in is_visited:
            progress_stack.append((now_a + now_b, 0, now_c,))
            is_visited.add((now_a + now_b, 0, now_c,))

    # B 물병에 채우는 경우

    # C에서 B로
    if now_c - (bottle_b - now_b) >= 0:
        if (now_a, bottle_b, now_c - (bottle_b - now_b),) not in is_visited:
            progress_stack.append((now_a, bottle_b, now_c - (bottle_b - now_b),))
            is_visited.add((now_a, bottle_b, now_c - (bottle_b - now_b),))
            if not is_filled[now_c - (bottle_b - now_b)] and not now_a:
                is_filled[now_c - (bottle_b - now_b)] = True
    else:
        if (now_a, now_b + now_c, 0,) not in is_visited:
            progress_stack.append((now_a, now_b + now_c, 0,))
            is_visited.add((now_a, now_b + now_c, 0,))

    # A에서 B로
    if now_a - (bottle_b - now_b) >= 0:
        if (now_a - (bottle_b - now_b), bottle_b, now_c,) not in is_visited:
            progress_stack.append((now_a - (bottle_b - now_b), bottle_b, now_c,))
            is_visited.add((now_a - (bottle_b - now_b), bottle_b, now_c,))
    else:
        if (0, now_a + now_b, now_c,) not in is_visited:
            progress_stack.append((0, now_a + now_b, now_c,))
            is_visited.add((0, now_a + now_b, now_c,))

    # C 물병에 채우는 경우

    # A에서 C로
    if now_a - (bottle_c - now_c) >= 0:
        if (now_a - (bottle_c - now_c), now_b, bottle_c,) not in is_visited:
            progress_stack.append((now_a - (bottle_c - now_c), now_b, bottle_c,))
            is_visited.add((now_a - (bottle_c - now_c), now_b, bottle_c,))
    else:
        if (0, now_b, now_a + now_c,) not in is_visited:
            progress_stack.append((0, now_b, now_a + now_c,))
            is_visited.add((0, now_b, now_a + now_c,))

    # B에서 C로
    if now_b - (bottle_c - now_c) >= 0:
        if (now_a, now_b - (bottle_c - now_c), bottle_c,) not in is_visited:
            progress_stack.append((now_a, now_b - (bottle_c - now_c), bottle_c,))
            is_visited.add((now_a, now_b - (bottle_c - now_c), bottle_c,))
    else:
        if (now_a, 0, now_b + now_c,) not in is_visited:
            progress_stack.append((now_a, 0, now_b + now_c,))
            is_visited.add((now_a, 0, now_b + now_c,))

# 모든 방문 기록 중에서 A가 비어있고 C의 양이 아직 기록된 값이 아니라면 전부 기록
for visit_log in is_visited:
    visit_a, visit_b, visit_c = visit_log
    if not visit_a and not is_filled[visit_c]:
        is_filled[visit_c] = True

# 기록 리스트를 체크하면서 C 물병에 존재했던 물의 양을 출력
for idx in range(bottle_c + 1):
    if is_filled[idx]:
        print(idx, end=' ')
