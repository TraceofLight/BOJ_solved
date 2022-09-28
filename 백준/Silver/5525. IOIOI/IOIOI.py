import sys

io_number = int(sys.stdin.readline())
length = int(sys.stdin.readline())
string = list(sys.stdin.readline())
result = 0
counter = 0

for idx in range(length):
    if counter != 0:
        counter -= 1
        continue
    if string[idx] == 'I':
        counter = 0
        if idx + 2 > length - 1:
            break
        while string[idx + (counter + 1)] == 'O' and string[idx + (counter + 2)] == 'I':
            counter += 2
        if counter // 2 < io_number:
            continue
        else:
            result += counter // 2 - io_number + 1

print(result)
