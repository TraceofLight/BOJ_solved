# Poziome serca

line_arr = [
    " @@@   @@@ ",
    "@   @ @   @",
    "@    @    @",
    "@         @",
    " @       @ ",
    "  @     @  ",
    "   @   @   ",
    "    @ @    ",
    "     @     ",
]

print_num = int(input())

for each_line in line_arr:
    for i in range(print_num):
        if i == print_num - 1:
            print(each_line)
        else:
            print(each_line, end=" ")
