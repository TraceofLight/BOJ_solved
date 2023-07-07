# A Simple Problem.

testcase = int(input())
output = []

for _ in range(testcase):
    target_number = int(input())
    result = pow(target_number, 2)
    output.append(result)
    
for result in output:
    print(result)
