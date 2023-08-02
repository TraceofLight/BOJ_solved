# HOMWRK

testcase = int(input())

for _ in range(testcase):
    problem_number = int(input())
    for _ in range(problem_number):
        a, b = map(int, input().split())
        print(a + b, a * b)
