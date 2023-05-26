# IT Passport Examination

participant_number = int(input())

for _ in range(participant_number):
    code, score1, score2, score3 = map(int, input().split())
    limit1 = 35 * 0.3
    limit2 = 25 * 0.3
    limit3 = 40 * 0.3
    
    if (
        (score1 + score2 + score3 < 55) 
        or (score1 < limit1 or score2 < limit2 or score3 < limit3)
    ):
        print(code, score1 + score2 + score3, 'FAIL')
        
    else:
        print(code, score1 + score2 + score3, 'PASS')
