# Equality

target_string = input()
equation = target_string.replace("=", "==")
result = eval(equation)

if result:
    print("YES")
else:
    print("NO")
