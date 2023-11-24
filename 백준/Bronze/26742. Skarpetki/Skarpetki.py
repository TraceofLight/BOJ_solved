# Skarpetki

string = input()
b = 0
c = 0
for each_char in string:
    if each_char == 'B':
        b += 1
    else:
        c += 1
result = b // 2 + c // 2
print(result)
