# CAPS

input_string = input()

output = []
for each_chr in input_string:
    output.append(chr(ord(each_chr) - 32))

print("".join(output))
