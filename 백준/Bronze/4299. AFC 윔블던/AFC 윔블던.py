# AFC 윔블던

import sys

input = sys.stdin.readline

a, b = map(int, input().split())
team_1 = (a + b) // 2
team_2 = (a - b) // 2

if (a + b) % 2 or team_1 < 0 or team_2 < 0:
    print(-1)
    
else:
    print(team_1, team_2)
