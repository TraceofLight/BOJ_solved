# 미소녀 컴퓨터 파루빗토 쨩

import re
from math import floor

input_string = input()
number_tokens = re.split(r"[*/+-]", input_string)
operator_tokens = re.split(r"[1234567890]", input_string)

while "" in number_tokens:
    number_tokens.remove("")

while "" in operator_tokens:
    operator_tokens.remove("")

oct_number_tokens = [str(int(number_tokens[i], 8)) for i in range(2)]

try:
    if len(operator_tokens) == 1:
        result = eval(oct_number_tokens[0] + operator_tokens[0] + oct_number_tokens[1])

    elif len(oct_number_tokens) == 2:
        if "*" in operator_tokens:
            if operator_tokens.index("*") == 0:
                result = eval(
                    oct_number_tokens[0]
                    + operator_tokens[0]
                    + operator_tokens[1]
                    + oct_number_tokens[1]
                )
            else:
                result = eval(
                    operator_tokens[0]
                    + oct_number_tokens[0]
                    + operator_tokens[1]
                    + oct_number_tokens[1]
                )

        elif "/" in operator_tokens:
            if operator_tokens.index("/") == 0:
                result = eval(
                    oct_number_tokens[0]
                    + operator_tokens[0]
                    + operator_tokens[1]
                    + oct_number_tokens[1]
                )
            else:
                result = eval(
                    operator_tokens[0]
                    + oct_number_tokens[0]
                    + operator_tokens[1]
                    + oct_number_tokens[1]
                )

        else:
            result = eval(
                operator_tokens[0]
                + oct_number_tokens[0]
                + operator_tokens[1]
                + oct_number_tokens[1]
            )

    elif len(oct_number_tokens) == 3:
        result = eval(
            operator_tokens[0]
            + oct_number_tokens[0]
            + operator_tokens[1]
            + operator_tokens[1]
            + oct_number_tokens[1]
        )

    result = floor(result)

    if result < 0:
        print(-(int(oct(result)[3:])))
    else:
        print(oct(result)[2:])

except:
    print("invalid")
