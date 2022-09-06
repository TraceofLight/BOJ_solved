import sys
counter0 = [0 for i in range(41)]
counter1 = [0 for i in range(41)]
result = [0 for i in range(41)]
output = []

counter0[0] = 1
counter1[0] = 0
counter0[1] = 0
counter1[1] = 1
result[0] = 0
result[1] = 1
for i in range(2, 41) : 
    counter0[i] = counter0[i - 1] + counter0[i - 2]
    counter1[i] = counter1[i - 1] + counter1[i - 2] 
    result[i] = result[i - 1] + result[i - 2] 

number = int(sys.stdin.readline())
for i in range(number) :
    x = int(sys.stdin.readline())
    output.append(x)
for i in output :
    print(counter0[i], counter1[i])