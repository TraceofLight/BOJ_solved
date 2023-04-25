# Body Mass Index

weight = float(input())
height = float(input())

bmi_result = weight / pow(height, 2)

if bmi_result > 25:
    print('Overweight')
elif 18.5 <= bmi_result <= 25:
    print('Normal weight')
else:
    print('Underweight')
