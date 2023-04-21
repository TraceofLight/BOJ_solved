# ISBN

isbn_number = '9780921418'

for _ in range(3):
    isbn_number = isbn_number + input()
    
result = 0
counter = 0

for each_digit in isbn_number:
    counter += 1
    if counter % 2:
        result += int(each_digit)
    else:
        result += int(each_digit) * 3

print(f'The 1-3-sum is {result}')
