# 공백 없는 A+B

number = input()

if number[1] != '0':
    result = int(number[0]) + int(''.join(number[1:]))
else:
    result = int(''.join(number[:2])) + int(''.join(number[2:]))

print(result)
